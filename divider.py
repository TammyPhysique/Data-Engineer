t = input("What operator do you want to use? ")
x = input("Type a number: ")
y = input("Type another number: ")

if float(y) == 0:
    print("Kan niet delen door 0")

else:
    print("The sum is: ", float(x) + t + float(y))
