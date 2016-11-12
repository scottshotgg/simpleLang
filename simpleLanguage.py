string = "1+11"

result = 0
stringIndex = 0
numberString = ""
character = ""
hasPeriod = False

def getChar():
	global stringIndex
	if stringIndex == len(string):
		stringIndex += 1
		return -1
	chara = string[stringIndex]
	stringIndex += 1
	return chara


def determineChar(char):
	print char

	if char.isalpha():
		print "alpha"
	elif char.isdigit():
		print "digit"
		global result
		global numberString
		numberString += char
		character = getChar()
		while (character != -1 and character.isdigit()): 
				numberString += character
				print numberString
				character = getChar()
		
		result += int(numberString)
		print "i am in here"
		
		if (character == '+'):
			numberString = ""
			character = getChar()
			while (character != -1 and character.isdigit()): 
				numberString += character
				print numberString
				character = getChar()	
				print character
			result += int(numberString)

		elif (character == '.'):
			hasPeriod = True
			numberString = ""
			print "period"

	else:
		print "other"

	print "result in the function", result
	return




#determineChar(char)
while not (stringIndex > len(string)):
	determineChar(getChar())

global character
print "char", character

print "\n\nresult:", result