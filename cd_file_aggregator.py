#Matt! 4/11/13
#Script to aggregate and format ST, PLACE, COU, CD lists from census website
#Desired output is ST|PLACE|C, CD|Y like
#    13|00184|8|N
#    13|04000|5, 6, 11|Y



import urllib2

#some setup vars
output_path = 'C:/temp/places_by_cd.txt'
delim = '|'

#set up url string. We will replace state codes for {0} and {1}
target_url = "http://www2.census.gov/geo/relfiles/cdsld13/{0}/pl_cd_delim_{1}.txt"

#list of states with more than 1 CD
#state_list = [13]
state_list = ['01', '04', '05', '06', '08', '09', '12', '13', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '31', '32', '33', '34', '35', '36', '37', '39', '40', '41', '42', '44', '45', '47', '48', '49', '51', '53', '54', '55']

place = "xx"

###########################################
#subroutine to do individual line jockeying

def format_line(st, place, delim, cd_list):
    #sort CD list first, while leading zeroes are present
    cd_list.sort()

    #remove leading seroes
    cd_list2 = []
    for eachcd in cd_list:
       cd_list2.append(eachcd.lstrip('0'))
                     
    string_cds = ", "

    #start the line, up through cds
    mynewline = st + delim + place + delim + string_cds.join(cd_list2) + delim

    if len(cd_list) > 1:
        mynewline = mynewline + 'Y' + "\n"
    else:
        mynewline = mynewline + 'N' + "\n"
                    
    return mynewline

#end subroutine
###########################################


# loop through states

for state in state_list:

    firstst_line = True

    for line in urllib2.urlopen(target_url.format(state,state)):
        
        #strip whitespace, some sort of line feed in the txt file
        stripline = line.rstrip()

        #ignore the first two lines like
        #GEORGIA CONGRESSIONAL DISTRICTS BY PLACE
        #State,Place,County,CongressionalDistrict

        if (stripline[0] + stripline[1]) == str(state):

            #check that line length is as expected

            if len(stripline) != 15:
                raise Exception("Weird length on " + stripline)

            #pull state, place, CD from current line
            currentlist = stripline.split(",")
            #print currentlist[0]

            if currentlist[1] == place and currentlist[0] == st:
                
                #continuing the same output
                #check if the CD is in our running CD list
                #if it isnt, add it
                if currentlist[3] not in cd_list:
                    cd_list.append(currentlist[3])
                

            else:
                
                if firstst_line == False:
                    
                    newline = format_line(st, place, delim, cd_list)
                    
                    try:
                        output.append(newline)
                    except:
                        #for first item
                        output = [newline]              

                #set state place CD for next set
                st = currentlist[0]
                place = currentlist[1]
                cd_list = [currentlist[3]]
                firstst_line = False

    #append the last line, embarassing                
    newline = format_line(st, place, delim, cd_list)
    output.append(newline)
    
                
#done with states 

f = open(output_path,'w')

for outputline in output:
    f.write(outputline)

f.close()

print "Output is at " + output_path
print "Adios\n"




