# print message
print("Assignment")

# Enter value is print its sum
a = int(input("Enter value : "))
b = int(input("Enter value : "))
print("Sum is = ",(a+b))

# Check given input is ODD OR EVEN
c = int(input("Enter value : "))
if(c % 2 != 0):
    print("Given value is ODD")
else:
    print("Given value is EVEN")

# check Leap year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# print PI value 
PI = 3.14
print(PI, "its a PI value")

# Constant value
import math
PI = math.pi
print("PI value is : ",PI)

# Square of numbers
square = int(input("Enter value : "))
print("It square is : ",(square*square))

# Area of circle
r = int(input("Enter value : "))
circle = 2 * PI * r
print("Area of circle is : ",circle)






