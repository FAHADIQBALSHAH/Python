#WAF to calculate length of a list

def calc_len(new_list):
    return len(new_list)

length = calc_len([10,20,30,40])
print(length)

# WAF to print the list in one single line
def print_list(new_list):
    print(new_list, sep= " ", end= " ")

print_list([10,20,30,40])

#WAF to find the Factorial of a Number n

def factorial(n):
    fact = 1
    i = 1
    while (i<=n):
        fact *= i 
        i += 1 
    return fact         

x = int(input("Enter a Number: "))
y = factorial(x)
print("FACTORIAL:", y)


def odd_even(n):
    if(n%2 == 0):
        print("EVEN")
    else:
        print("ODD")


a = int(input("Enter a Number: "))
odd_even(a)      
