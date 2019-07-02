skills=["c++","designing","python","sprinting"]
cv={}
cv["name"]=input("Name: ")
cv["age"]=input("Age: ")
cv["exp"]=int(input("years of experience: "))

cv["skills"]=[]

print("1-" + skills[0])
print("2-" + skills[1])
print("3-" + skills[2])
print("4-" + skills[3])

chose=int(input("choose the number of the skills above : "))
cv["skills"].append(skills[chose-1])

chose=int(input("choose another number of the skills above : "))
cv["skills"].append(skills[chose-1])

if int(cv["age"])>25 and int(cv["age"])<40 and int(cv["exp"]) > 3 and cv["skills"][0]==skills[2] or cv["skills"][1]==skills[2]:
    print ("yay u r accepted")

else :
	print ("sorry")

