from datetime import datetime

class employees:
	def __init__ (self,name,age,salary,employment_date):
		self.name=name
		self.age=age
		self.salary=salary
		self.employment_date=employment_date

	def get_working_years(self):
		today = datetime.now()
		c_years= today.year
		return c_years - int(self.employment_date)

	def __repr__(self):
		return "name: %s,age: %s,salary: %s, employment date: %s"	% (self.name , self.age , self.salary , self.get_working_years() )

class manager(employees):
	def __init__(self,name,age,salary,employment_date,bonus_percentage):
		employees.__init__(self, name,age,salary,employment_date) # or super(self, name,age,salary,employment_date).
		self.bonus_percentage=bonus_percentage

	def get_bonus(self):
		return self.bonus_percentage*self.salary

	def __repr__(self):
		return "name: %s,age: %s,salary: %s, employment date: %s,bonus: %s	"	% (self.name , self.age , self.salary , self.get_working_years() , self.get_bonus())

employee=[]
managers=[]

print("\tWelcome to HR Pro 2019")
print("\tChoose an action to do:")
print("\t\t1. show employees")
print("\t\t2. show managers")
print("\t\t3. add an employee")
print("\t\t4. add a manager")
print("\t\t5. exit")
print("")


choose = input("what would you like to do ?")
print("----------------")

while choose != "5":

	if choose =="1":
		for x in employee:
			print (x)

	elif choose =="2":
		for m in managers:
			print(m)

	elif choose == "3":
		emp=employees(input("Name: "), input("age: "), input("Salary: "),input("working years: "))
		employee.append(emp)

	elif choose =="4":

		mng=manager(input("Name: "), input("age: "), input("Salary: "),input("working years: "),input("bonus "))
		managers.append(mng)

	else :
		print("wrong input")

	choose = input("what would you like to do ?")
