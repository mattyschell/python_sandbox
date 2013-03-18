import shutil
import os.path

##############
mycd = "0901"
##############

#Matt!
#updated 2/26 with better error handling
#Updated 3/7 with final checks that all files were copied

state = mycd[:2]
cd = mycd[-2:]

frommxd = "\\\\batch4.geo.census.gov\mtdata004\mapping\\113th_CD_Wall_Maps\CD_Based_Maps\Production\Map_Creation\Editing\Initial_MXD\ST" + state + "\\" + mycd + '_Map.mxd'
tomxd = "C:\\113th_CD_Wall_Maps\CD_Based_Maps\Production\Map_Creation\Editing\Initial_MXD\ST" + state + "\\" + mycd + "_Map.mxd"

#check for existence of mxd to avoid accidental overwrites of work
if os.path.isfile(tomxd):
    print "\nmxd already exists at " + tomxd + "\n"
    raise Exception("Exiting")   

print "\n copying mxd from " + frommxd + "\n"
shutil.copyfile(frommxd,tomxd)


fromshp = "\\\\batch4.geo.census.gov\mtdata004\mapping\\113th_CD_Wall_Maps\CD_Based_Maps\Production\Map_Creation\Input_SHP\ST" + state
toshp = "C:\\113th_CD_Wall_Maps\CD_Based_Maps\Production\Map_Creation\Input_SHP\ST" + state

print "\ncopying input SHPs from " + fromshp + "\n"

#may fail if the user has the shps open in arcgis, or if no exist
shutil.rmtree(toshp, ignore_errors=True)
#may fail if rmtree failed due to shps already open, in which case weve got all shps already
try:
    shutil.copytree(fromshp,toshp)
except:
    print "\n Copy of input shps failed, I think you already have them AND you have them open in ArcMap"
    raise Exception("Exiting") 

fromoutshp = "\\\\batch4.geo.census.gov\mtdata004\mapping\\113th_CD_Wall_Maps\CD_Based_Maps\Production\Map_Creation\Output_SHP\ST" + state + "\CD" + cd
tooutshp = "C:\\113th_CD_Wall_Maps\CD_Based_Maps\Production\Map_Creation\Output_SHP\ST" + state + "\CD" + cd

print "\ncopying output SHPs from " + fromoutshp + "\n"

shutil.rmtree(tooutshp, ignore_errors=True)
try:
    shutil.copytree(fromoutshp,tooutshp)
except:
    print "\n Copy of input shps failed, I think you already have them AND you have them open in ArcMap"
    raise Exception("Exiting") 

#check if all files copied. Use listdir, glob includes full path
#first set
fromshplist = os.listdir(fromshp)
toshplist = os.listdir(toshp)
if set(fromshplist) != set(toshplist):
    print "\nFailed to copy some of the files from " + fromshp + "\n"
    raise Exception("Exiting")
#output shps
fromshplist = os.listdir(fromoutshp)
toshplist = os.listdir(tooutshp)
if set(fromshplist) != set(toshplist):
    print "\nFailed to copy some of the files from " + fromoutshp + "\n"
    raise Exception("Exiting")

print "\nAll done, now let's make an award-winning map!\n"
