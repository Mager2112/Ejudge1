import sys
accumulated_str = ""
sum = 0
while True:
	char = sys.stdin.read(1)
	if char == '':
		break
	if char.isdigit() or(accumulated_str == "" and char == '-'):
		accumulated_str += char
	elif accumulated_str == "-" and char == '-':
		continue
	elif accumulated_str and not char.isdigit():
		if len(accumulated_str) < 2 and accumulated_str.isdigit():
			sum += int(accumulated_str)
		elif accumulated_str.isdigit() or (accumulated_str[0] == '-' and accumulated_str[1:].isdigit()):
			sum += int(accumulated_str)
		accumulated_str=""
print(sum)
	    
