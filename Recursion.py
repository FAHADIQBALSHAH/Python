def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(10)    

def fact(m):
    if(m==0 or m==1):
        return 1
    else:
        return m * fact(m-1)

x = int(input("Enter any number: "))
y = fact(x)
print("Factorial of",x, "is", y)

def cal_sum(n):
    if(n==0):
        return 0
    else:
        return cal_sum(n-1) + n

    
x = int(input("Enter any number: "))
y = cal_sum(x)
print(y)   


new_list = [10,20,30,40]

def print_list(list, i=0):
    if(i == len(list)):
        return
    print(list[i])
    print_list(list, i+1)


print_list(new_list)