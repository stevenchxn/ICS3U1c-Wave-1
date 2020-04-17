a = float(input("Enter your currency amount here: $"))
savings = 0
time = 0
for i in range (3):
    b = a * 1.04
    savings += (b % a)
    time += 1
    print ("Your savings account will hold $", round(savings, 3), " after ", time, " years")