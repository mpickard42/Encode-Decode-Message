import csv

###################################################################################

def selectInputType():
    input_type = ""
    invalid_input = True
    while invalid_input:
        input_type = raw_input("Would you like to import from the terminal or a csv? ")
        input_type = input_type.strip()
        input_type = input_type.upper()
        if input_type == "TERMINAL":
            invalid_input = False
        elif input_type == "CSV":
            invalid_input = False
        else:
            print "Sorry, that is not a valid option"
    get_and_verify_integers(input_type.upper())

###################################################################################


def get_and_verify_integers(input_type):
    if input_type == "TERMINAL":
        integers = get_integers_from_terminal()
    elif input_type == "CSV":
        file_name = raw_input("Enter the file name or path: ")
        integers = get_integers_from_csv(file_name)

    #verify that the input is integers
    for i in integers:
        try:
            i = int(i)
        except ValueError:
            pass
        
        if isinstance(i, int):
            i = i #just a placeholder
        else:
            print "The data entered is not an integer type.  Repeat using integers. "
            selectInputType()
    convert(integers)




def get_integers_from_terminal():
    integers = raw_input("Enter integers separated by commas: ")
    if not integers:
        print "Please enter one or more integers"
        selectInputType()
    integers = integers.split(",")
    return integers


def get_integers_from_csv(file_name):
    with open(file_name, 'rb') as csvfile:
        file_output = csv.reader(csvfile)
        integers = ""
        for row in file_output:  ## object to string
            integers += ','.join(row)
            while integers[-1] == ",":  #removing multiple excess commas from the line
                integers = integers[:-1]
            integers = integers + ","   #add a single comma at end of the line
    csvfile.close()
    integers = integers[:-1] #delete the last comma in the string
			
    integers = integers.split(",") #make a list
    return integers

###################################################################################


def convert(integers):
	message = ""
	mode = "uppercase"
	uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
	punctuation_signs = """!?=,. ;"'@#$%^&*()-_+~`[]{}\|:/><"""
	numbers = "0123456789"
	
	for i in integers:
		if i not in [",", " "]:
			i = int(i)
			if mode == "uppercase": 
				# convert integers to uppercase
				letter = i % 27
				if letter == 0:
					mode = "lowercase"
				else: 
					message = message + uppercase_letters[letter - 1]
				
			elif mode == "lowercase":
				# convert integers to lowercase
				letter = i % 27
				if letter == 0:
					mode = "punctuation"
				else:
					message = message + lowercase_letters[letter - 1]
				
			elif mode == "punctuation":
				# convert integers to punctuation
				punct = i % 34
				if punct == 0:
					mode = "number"
				else:
					message = message + punctuation_signs[punct - 1]
					
			elif mode == "number":
				# convert integers to numbers
				num = i % 11
				if num == 0:
					mode = "uppercase"
				else:
					message = message + numbers[num - 1]
	print message
	raw_input("Press 'enter' to close program ")

	
###################################################################################




selectInputType()
