def traverseFunc(string):
	string = list(string)
	for _ in range(len(string)):
		leftChange = []
		rightChange = []
		for i in range(len(string)):	
			if(i==len(string)-1):
				pass
			elif(string[i]=='-' and string[i+1]=='A'):
				#string[i-1] = 'A'
				leftChange.append(i)
			
			if(i==len(string)-1):
				pass
			elif(string[i]=='B' and string[i+1]=='-'):
				rightChange.append(i+1)
			res = []
			for m in leftChange:
				for n in rightChange:
					if(m==n):
						if(res.count(m)>0):
							pass
						else:
							res.append(n)
			#print(res)
			for x in res:
				if(leftChange.count(x)>0):
					leftChange.remove(x)
				else:
					pass
				if(rightChange.count(x)>0):
					rightChange.remove(x)
				else:
					pass

		for x in leftChange:
			string[x] = 'A'
		for x in rightChange:
			string[x] = 'B'
		#print(_)
		#print("".join(string))
	return "".join(string)

n = input()
rawstr = input()
res = traverseFunc(rawstr)
#print(res)
aCount = res.count('A')
bCount = res.count('B')

if(aCount>bCount):
	print("A")
elif(aCount<bCount):
	print("B")
else:
	print("Coalition Government")