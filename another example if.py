years_worked = int(input("Enter the amount of years you worked: "))
salary = float(input("Enter the yearly salary you get: "))
name = 'merhawi'
print(name.upper())
if(years_worked >=2 and salary >= 30000):
    print("your qualify for loan")
elif(years_worked < 2 and salary >= 30000):
    print("you are not qualify becouse of too low work years")

elif(years_worked >= 2 and salary < 30000):
    print("you are not cualifay b/c of too low salary")

else:
    print("you are not meet either requrment to get loan ")
    