

def one_tenth_file(original_filename):
	# write every 10th line of the original file to a new file
	One_Tenth_file = open(original_filename[:-4] + "_oneTenth.txt", 'w')
	x = 1
	with open(original_filename, "r") as fileobject:
		for line in fileobject:
			if x < 10:
				x += 1
			elif x == 10:
				One_Tenth_file.write(line)
				x = 1
			else:
				break

	One_Tenth_file.close()
	print (original_filename + " reduced by 1 : 10")
	print ("and saved as > " + One_Tenth_file)
	print ("> Done")


def first_one_hundred(filename):
	# write the first 100 lines of the original file to a new file
	x = 1
	One_Tenth_file = open("One_Hundred_Lines_of_" + filename, 'w')
	with open(filename, "r") as fileobject:
		for line in fileobject:
			if x <= 100:
				x += 1
				One_Tenth_file.write(line)
			else:
				break

	One_Tenth_file.close()
	
	# print ("first 100 lines of " + filename + " stored as > " + One_Tenth_file)
	print ("Done")



def strip_data(filename):

# search through shortened file and store only the data points

	Only_Data = open("Only_Data_One_Tenth_File.txt", 'w')

	with open("One_Tenth_File.txt", "r") as handle:
		for line in handle:
			if line[0] == '%':
				print ("Not the starting place")
			else:
				start_position = line.find('-')
				end_position = line.find('SHORT')
				Only_Data.write(line[start_position:end_position-1] + "\n")

	Only_Data.close()

	print ("data stripped from " + filename + " and stored as > " + Only_Data)
	print ("Done")
	
def add_neg_space(filename):
# add one extra space before every " - " for proper matlab import 
    print ('achieved function call')
    Final_File = open(filename[:-4] + "_Final_Data_File.txt", 'w')
    
    
    print ('created new document')
    
    original_file = open(filename, "r")
    print ('opened' + filename )
    
    for i in original_file:
        print (i)
        if i == '-':
            Final_File.write('  -')
            print ('  -')
        else:
                #print('no - detected')
                Final_File.write(i)
                
    Final_File.close()
	
    print ("Done")

def proper_spacing(filename):
    Final_File = open(filename[:-4] + "_Final_Data_File.txt", 'w')

    
    with open(filename, "r") as handle:
        for line in handle:
            x = str(line)
            #print (x)
            new_line = ""
            for char in x:
                #print (type(char))
                if char == '-':
                    new_line += ' -'
                elif char == '	':
                    print ('tab found')
                    new_line += ' '
                else:
                    new_line += char
            Final_File.write(new_line)
    Final_File.close()

    print ('Done')

		
#proper_spacing('Only_Data_One_Tenth_File.txt')

first_one_hundred('Only_Data_One_Tenth_File_Final_Data_File.txt')
