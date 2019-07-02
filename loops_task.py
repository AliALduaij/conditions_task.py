market={}
item = input("item: (enter \"done\" when finished)")
x=0
total=0
while item != "done":
	
	market["items%d"%x]=[]
	market["items%d"%x].append(item)
	market["items%d"%x].append(float(input("price: ")))
	market["items%d"%x].append(float(input("quantity: ")))
	item = input("item: (enter \"done\" when finished)")
	x = x+1
print("-------------------------")
print("RECEIPT")
print("-------------------------")

for i in market :
	print(str(market[i][2])+" " +" " +str(market[i][0])+" "+" "+str(float(market[i][2]*market[i][1])))
	total+=float(market[i][2]*market[i][1])

print("-------------------------")	
print("Total: %s" %total)
#for t in market:

	#for s in market[i]:
		#print("%f  %s   %f"% s[2],s[0],s[1]*s[2])

        