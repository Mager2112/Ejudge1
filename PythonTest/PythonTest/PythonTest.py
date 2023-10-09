#  Copyright Mager 2023
# All rights reserved lmao
import sys
result = 0
acc_string = ""
while True:
	char = sys.stdin.read(1)
	if char == '':
		break
	if char.isdigit() or (acc_string == "" and char == '-'):
		acc_string += char
	elif acc_string == "-" and char == '-':
		continue
	elif acc_string and not char.isdigit():
		#if len(acc_string) < 2 and acc_string.isdigit():
		#	result += int(acc_string)
		#elif acc_string.isdigit() or (acc_string[0] == '-' and acc_string[1:].isdigit()):
		result += int(acc_string)
		acc_string = ""
print(result)
	    
