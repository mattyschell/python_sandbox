import arcpy #slow
import glob

mytotal = 0
mydirlist = glob.glob('V:/gz/dads/acs/acs12/qa/z6/st*')
for mydir in mydirlist:
   #print "peeking into " + mydir
   #print mydir + '\geo_2012_g_' + '*' + '080_00_py_z6.shp'
   myshp = glob.glob(mydir + '\geo_2012_g_' + '*' + '080_00_py_z6.shp')
   
   #print "found " + myshp[0]
   infeatures = myshp[0]
   #print "infeatures is " + infeatures
   result = arcpy.management.GetCount(infeatures)
   mykount = result.getOutput(0) 
   mytotal += int(mykount)

print "total kount is " + str(mytotal)
   
