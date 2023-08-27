my_name = input("what is your name?")
my_age = int(input("how old are you?"))
print(f"my name is{my_name} and i'm {my_age} years old")

first_number = int(input("what is your first number?"))
secound_number = int(input("what is your secound number?"))

operation = input ("what your operation?")
if operation == '+':
    print (first_number+secound_number)
elif operation == "*" :
    print (first_number*secound_number)
elif operation =="-" :
    print(first_number-secound_number)
elif operation =="/" :
    print (first_number/secound_number)
else :
    print("the operation is not valid")

bus_capcity=(11)
people_inbus= int(input("enter the number of people who want to ride the bus"))
people_outside = int(input("how many peolpe want to enter the bus?"))
empty_seats = bus_capcity - people_inbus 

if empty_seats >= people_outside :
    print (f'there is {empty_seats} empty seats')

elif empty_seats < people_outside or empty_seats == people_outside :
    print ("there is no empty seats ")

  