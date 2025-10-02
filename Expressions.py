# String and Numeric operate with a *

A,B = 2,3
C = "@"
D = (A*C*B)
print(D)

# String and String operate with a + This is called "CONCATENATION".

A,B = "2",3
C = "@"
D = ((A+C)*B)
print(D)

# Numeric values can operate with Airthematic operators

A,B = 2,3
C =4
D = (A+B*C)
print(D)

# Airthematic expression with Integer & Float will result in Float

A,B = 10, 5.0
C= A*B
print(C)

#Division of 2 Integers will be Float

A,B = 4,2
C = A/B
print(C)

#Interger Division with Float and Int will give Int displayed as Float
# Works on the basis of Roundoff Principle and does it to the lower number 

A,B = 1.5, 3
C = A//B
D = A/B
print(C)
print(D)

#Remainder(%) is -ve when the denominator is -ve

A,B = -5,2
C = A%B
print("Case1:", C)

A,B = 5,2
C = A%B
print("Case2:", C)

A,B = 5,-2
C = A%B
print("Case3:", C)

A,B = -5,-2
C = A%B
print("Case4:", C)