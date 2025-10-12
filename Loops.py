#While Loops

num = 1
while(num<=100):
    print(num)
    num += 1

nums = 100
while(nums>=1):
    print(nums)
    nums -=1    

n = int(input("Enter the Number: "))
i = 1
while(i<=10):
    print(n*i)
    i +=1    

new_list = [1,4,9,16,25,36,49,64,81,100]
n = len(new_list)
i = 0
while (i<n):
    print(new_list[i])
    i +=1

new_tuple = (1,4,9,16,25,36,49,64,81,100)
n = len(new_tuple)

x = int(input("Enter any Number: "))
i = 0
while (i<n):
    if(new_tuple[i] == x):
        print("Number found in Tuple")
    else:
        print("Number not found")
    i += 1       

#For Loops
nums = [1,4,9,16,25]

for i in nums:
    print(i)
else:
    print("LOOP ENDS")    

name = "FAHAD"
for x in name:
    print(x)


#Range Function 
print(range(10))  

for el in range(5):
    print(el)

for el in range(2,5):
    print(el)

for el in range(2,10,2):
    print(el)    
