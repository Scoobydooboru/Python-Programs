from math import sqrt
print ("Welcome to the program. Please enter the value of a,b,c and x at the corresponding prompts.")

a = float(input("Enter the value for a: "))
b = float(input("Enter the value for b: "))
c = float(input("Enter the value for c: "))
x = float(input("Enter the value for x: "))

new = "The following quadratic was entered: \n (%s * (x^2) + (%sx) + %s" % (a, b, c)

print (new)

solve = (a*(x**2) + (b * x) + c)

print ("Here is the solution to the quadratic:", solve)
