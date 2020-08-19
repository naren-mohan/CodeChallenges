#CENS2020 -- CENS20G
#Martha and her loverboy


def subVal(arr):
	x = 0
	y = 0
	for a in arr:
		if(a=="R"):
			x+=1
		elif(a=="L"):
			x+=-1
		elif(a=="D"):
			y+=-1
		elif(a=="U"):
			y+=1
	return [x,y]


def printSubsequences(arr, index, subarr): 
	global subseqlen,subseqVal
	if index == len(arr): 
		if len(subarr) != 0: 
			subseqlen.append(len(subarr))
			subseqVal.append(subVal(subarr))
			#print(subarr) 
	else: 
		printSubsequences(arr, index + 1, subarr) 
		printSubsequences(arr, index + 1, subarr+[arr[index]]) 
	return

T = raw_input()
T = int(T)
out = []
for i in range(T):
	subseqlen = []
	subseqVal = []
	string = input()
	stringlist = [char for char in string]
	start = str(input()).split()
	printSubsequences(stringlist, 0, [])
	#print(subseq)
	x1 = int(start[0])
	y1 = int(start[1])
	
	q = int(input())
	temp = []
	for j in range(q):
		query = str(input()).split(" ")
		x2 = int(query[0])
		y2 = int(query[1])
		flag = 0
		minim = 1000000000000
		for k in range(len(subseqVal)):
			#print(len(subseqVal))
			#print(subseqVal[k][0])
			if(x2 == x1+subseqVal[k][0] and y2 == y1+subseqVal[k][1]):
				flag = 1
				if(subseqlen[k] <= minim):
					minim = subseqlen[k]
		if(flag):
			temp.insert(j,["YES",minim])
		else:
			temp.insert(j,["NO"])
	out.insert(i,temp)
#print(out)
for i in range(len(out)):
	for j in range(len(out[i])):
		if(out[i][j][0] == "YES"):
			print("YES"+" "+str(out[i][j][1]))
		else:
			print("NO")