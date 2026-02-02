a = 12
print(a)

b = 16
print(b)        # Operators

# Arithmetic Operators
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a // b) # Floor Division
print(a % b)  # Modulus
print(a ** b) # Exponentiation

# Comparison (Relational) Operators
x = 5
y = 10
print(x == y)  # Equal to
print(x != y)  # Not equal to
print(x > y)   # Greater than
print(x < y)   # Less than
print(x >= y)  # Greater than or equal to
print(x <= y)  # Less than or equal to

# Logical Operators
a = True
b = False
print(a and b)  # and
print(a or b)   # or
print(not a)    # not

# Assignment Operators
x = 5
x += 3  # +=
x *= 2  # *=
x /= 4  # /=

# Identity Operators
x = [1, 2, 3]
y = [1, 2, 3]
z = x
print(x is y)      # is
print(x is z)      # is
print(x is not y)  # is not

# Membership Operators
lst = [1, 2, 3, 4]
print(3 in lst)    # in
print(5 not in lst) # in not

# Bitwise Operators
x = 5   # 0101 in binary
y = 3   # 0011 in binary
print(x & y)  # AND (&)  (0001 in binary)
print(x | y)  # OR (|) (0111 in binary)
print(x ^ y)  # XOR (^) (0110 in binary)
print(~x)     # Bitwise NOT (~) (inverse of 0101)
print(x << 1) # Left shift (<<) (1010 in binary)
print(x >> 1) # Right shift (>>)  (0010 in binary)
