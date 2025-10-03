marks = [85.5, 92.3, 77.9, 90.1]
print(marks)
print(type(marks))

student = ["FAHAD", 24, 95.5, "SRINAGAR"]
print(student)

print(student[1])
print(len(student))
#print(student[6]) Will give out of range error

student[2] = 100
print(student)

mylist = [1,2,3,4]
print(mylist)
mylist.append(5)
print(mylist)
mylist.sort()
print(mylist)
mylist.sort(reverse = True)
print(mylist)
mylist.reverse()
print(mylist)
mylist.insert(0,0)
print(mylist)
mylist.remove(0)
print(mylist)
mylist.pop(0)
print(mylist)

#Enter three names and store them in a list

name1 = input("Enter 1st Name: ")
name2 = input("Enter 2nd Name: ")
name3 = input("Enter 3rd Name: ")


list_names =[]
list_names.append(name1)
list_names.append(name2)
list_names.append(name3)

print("List of Names:", list_names)


#Check if a list contains a palindrome of elememts

list_num = [1,2,3,2,1]
print(list_num)

new_list = list_num.copy()
new_list.reverse()
print(new_list)

if (list_num == new_list):
    print("Plaindrome")
else:
    print("Not a Palindrome")    