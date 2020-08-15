def binaryFunc(num2, digit=False):
	zero = 0
	one = 0
	binary = ""

	while(num2>=2):
		rem = int(num2%2)
		if(rem==1):
			one += 1
		else:
			zero += 1
		binary = str(rem)+binary
		#print(binary)
		num2 = int(num2/2)
	binary = str(num2)+binary
	
	if(num2):
		one += 1
	else:
		zero += 1
	if(digit!=False):
		for _ in range(digit-len(binary)):
			binary = '0'+binary
			zero += 1
	return [binary,zero,one]

def subcase(caselist):
	global digit
	zeroes = 0
	ones = 0
	for case in caselist:
		res = binaryFunc(case,digit)
		zeroes += res[1]
		ones += res[2]
	#print(zeroes)
	#print(ones)
	if(zeroes == ones):
		return True
	else:
		return False

inplist = []

n = int(input())
rawinput = input()
rawlist = rawinput.split()
greatest = 0
for i in range(n):
	temp = int(rawlist[i])
	if(temp>greatest):	greatest = temp
	inplist.append(temp)

initRes = binaryFunc(greatest,digit=False)	#dryRun to get the max digits
digit = len(initRes[0])

binCounter = 0
for i in range(len(inplist)+1): 
    for j in range(i+1,len(inplist)+1):
    	if(subcase(inplist[i:j])):
    		binCounter+=1

print((binaryFunc(binCounter,digit)[0]))