#CENS2020 -- CENS20D
#Priya and her Bitwise AND 

test_case = int(input())
n = []
rawstr = []
val = []
out = []

for i in range(test_case):
	n.append(int(input()))
	rawstr.insert(i,str(input()).split())
	if(n[i]<=1):
		out.append(0)
		val.insert(i,0)
		continue
	temp = []
	for raw in rawstr[i]:
		temp.append(int(raw))
	val.insert(i,temp)
	count = 0
	for y in range(0,n[i],1):
		for x in range(0,y,1):
			if(val[i][x] == val[i][y] & val[i][x]):
				count += 1

	out.append(count)

for x in out:
	print(x)