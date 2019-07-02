
from datetime import *
today=date.today()


def check_birthday(year,month,day):
   
    
    

    if today > Date_of_birth :
        return True

    else :
        return False

def calculate_age(year,month,day):
    
    age= today - Date_of_birth
    age_in_days = age.days

    yearss= age_in_days /365
    age_in_days= age_in_days%365

    monthss= age_in_days/30
    age_in_days=age_in_days%30


    print ("years= %d , months= %d , and days = %d" % (yearss,monthss,age_in_days))

    # print("your age is %d years ,%d month and %d days" % (age.year,age.month,age.days))

year=int(input("enter year of your birthday"))
month=int(input("input month of your birthday"))
day=int(input("enter day of your birthday"))
Date_of_birth=date(year ,month ,day) 
check_birthday(year,month,day)
if check_birthday(year,month,day) == True:
    calculate_age(year,month,day)

else:
    print("error")