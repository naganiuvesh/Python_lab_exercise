# 1. print message
print("Assignment")

# 2. Enter value is print its sum
a = int(input("Enter value : "))
b = int(input("Enter value : "))
print("Sum is = ",(a+b))

# 3. Check given input is ODD OR EVEN
c = int(input("Enter value : "))
if(c % 2 != 0):
    print("Given value is ODD")
else:
    print("Given value is EVEN")

# 4. check Leap year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, "is a Leap Year")
else:
    print(year, "is not a Leap Year")

# 5. print PI value 
PI = 3.14
print(PI, "its a PI value")

# 6. Constant value
import math
PI = math.pi
print("PI value is : ",PI)

# 7. Square of numbers
square = int(input("Enter value : "))
print("It square is : ",(square*square))

# 8. Area of circle
r = int(input("Enter value : "))
circle = 2 * PI * r
print("Area of circle is : ",circle)

# Check Data Type
data = input("Enter something : ")
print(type(data))

# 10. Use math function && 11. Find power
import math
number = 12
power = pow(number, 2)
print("PI value is : ",power)

# 12. Check Positive or Negative
x = int(input("Enter number : ")) 
if(x >= 0) :
    print("Your number is Positive ")
else :
    print("Your number is Nagative")
