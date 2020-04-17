cents = int(input("Enter your cents here: "))
print (cents//200, "toonies")
cents = cents%200
print (cents//100, "loonies")
cents = cents%100
print (cents//25, "quarters")
cents = cents%25
print(cents//10, "dimes")
cents = cents%10
print(cents//5, "nickels")
cents = cents%5
print(cents//1, "pennies")
