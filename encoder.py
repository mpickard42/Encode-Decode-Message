### encoder ####
# * random.randint(1, 1000)
import random, csv

uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
punctuation_signs = """!?=,. ;"'@#$%^&*()-_+~`[]{}\|:/><"""
numbers = "0123456789"

integers = []

message = raw_input("Message: ")

#since the decoder assumes it starts with capitals, add in numbers to change to lowercase or punctuation
if message[0] in lowercase_letters:
	integers.append(27 * random.randint(1, 1000)) 
elif message[0] in punctuation_signs:
	integers.append(27 * random.randint(1, 1000)) 
	integers.append(27 * random.randint(1, 1000))
elif message[0] in numbers:
	integers.append(27 * random.randint(1, 1000))
	integers.append(27 * random.randint(1, 1000))
	integers.append(34 * random.randint(1, 1000))
	
		
mode = ""


for character in message:
	if character in uppercase_letters:
		if mode == "lower":
			integers.append(27 * random.randint(1, 1000)) 
			integers.append(34 * random.randint(1, 1000))
			integers.append(11 * random.randint(1, 1000))
		elif mode == "punct":
			integers.append(34 * random.randint(1, 1000)) 
			integers.append(11 * random.randint(1, 1000))
		elif mode == "num":
			integers.append(11 * random.randint(1, 1000))
		mode = "upper"
		
		int = uppercase_letters.index(character)
		int = int + 1 + (27 * random.randint(1, 1000))
		integers.append(int)
		
	elif character in lowercase_letters:
		if mode == "upper":
			integers.append(27 * random.randint(1, 1000))
		elif mode == "punct":
			integers.append(34 * random.randint(1, 1000)) 
			integers.append(11 * random.randint(1, 1000))
			integers.append(27 * random.randint(1, 1000)) 
		elif mode == "num":
			integers.append(11 * random.randint(1, 1000))
			integers.append(27 * random.randint(1, 1000)) 
		mode = "lower"
		int = lowercase_letters.index(character)
		int = int + 1 + (27 * random.randint(1, 1000))
		integers.append(int) 
		
	elif character in punctuation_signs:
		if mode == "upper":
			integers.append(27 * random.randint(1, 1000))
			integers.append(27 * random.randint(1, 1000)) 
		elif mode == "lower":
			integers.append(27 * random.randint(1, 1000))
		elif mode == "num":
			integers.append(11 * random.randint(1, 1000)) 
			integers.append(27 * random.randint(1, 1000)) 
			integers.append(27 * random.randint(1, 1000)) 
		mode = "punct"
		
		int = punctuation_signs.index(character)
		int = int + 1 + (34 * random.randint(1, 1000))
		integers.append(int) 
		
	elif character in numbers:
		if mode == "upper":
			integers.append(27 * random.randint(1, 1000)) 
			integers.append(27 * random.randint(1, 1000)) 
			integers.append(34 * random.randint(1, 1000)) 
		elif mode == "lower":
			integers.append(27 * random.randint(1, 1000)) 
			integers.append(34 * random.randint(1, 1000)) 
		elif mode == "punct":
			integers.append(34 * random.randint(1, 1000)) 
		mode = "num"
		
		int = numbers.index(character)
		int = int + 1 + (11 * random.randint(1, 1000))
		integers.append(int)


print integers
in_file = raw_input("Would you like this message stored in a csv file? y/n ")
if in_file == "y":
	name = raw_input("Enter the name of the file: ")
	with open(name, 'wb') as csvfile:
		messagewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		messagewriter.writerow(integers)
	csvfile.close()
raw_input("Press 'enter' to close program ")

		