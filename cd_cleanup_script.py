import shutil
import os, os.path

##CLEANUP###########
finished_cd = "0902"
driveletter = "C:"   #VDI users?
##CLEANUP############


#Matt! 3/13

print "\n Starting cleanup\n"

driveroot = driveletter + "\\113th_CD_Wall_Maps\CD_Based_Maps\Production\Map_Creation\\"
state = finished_cd[:2]
cd = finished_cd[-2:]

#check that path is valid
if not os.path.isdir(driveroot + "Editing\Initial_MXD\ST" + state + "\\"):
    print "\n Path looks bogus.  Check your finished_cd entry that you typed in, maybe its wrong?\n"
    print "\n--> " + driveroot + "Editing\Initial_MXD\ST" + state + "\\ <--"
    raise Exception("Exiting")

#check if there are 1+ mxds and warn if yes
localmxds = os.listdir(driveroot + "Editing\Initial_MXD\ST" + state + "\\")

if len(localmxds) > 1:
    print "\n WARNING: You have " + str(len(localmxds)) + " local mxds for state " + state + "\n"

#remove input shp directory
#may fail if the user has the shps open in arcgis, or if no exist
    
input_shp = driveroot + "Input_SHP\ST" + state
#check that path exists
if not os.path.isdir(input_shp):
    print "\n Input shp path does not exist.  Check your finished_cd entry, maybe its wrong?\n"
    raise Exception("Exiting")     

try:
    shutil.rmtree(input_shp, ignore_errors=False)
except:
    print "\n Removal of input shps failed, I think you might have them open in arcmap\n"
    raise Exception("Exiting") 


#remove output shp directory
#may fail if the user has the shps open in arcgis, or if no exist

output_shp = driveroot + "Output_SHP\ST" + state + "\CD" + cd
#check that path exists
if not os.path.isdir(output_shp):
    print "\n Output shp path does not exist.  Check your finished_cd entry, maybe its wrong?\n"
    raise Exception("Exiting")

try:
    shutil.rmtree(output_shp, ignore_errors=False)
except:
    print "\n Removal of output shps failed, I think you might have them open in arcmap\n"
    raise Exception("Exiting")

print "\nTa da! Clean as a whistle.\n"



