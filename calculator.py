Fnum=input("input the first number please")
Snum=input("the second number please")

if Fnum.isdigit()==True and Snum.isdigit()==True:

    operation=input("input between these operation : + or - or / or *")
    if operation == "+":
        total = int(Fnum) + int(Snum)
        print ("the total = " + str(total))

    elif operation == "-":
        total = int(Fnum) - int(Snum)
        print ("the total = " + str(total))

    elif operation == "/":
        total = int(Fnum) / int(Snum)
        print ("the total = " + str(total))

    elif operation == "*":
        total = int(Fnum) * int(Snum)
        print ("the total = " + str(total))

    else:
        print ("you have to type between these operations only : + or - or / or * ")

else :
	print("error")
