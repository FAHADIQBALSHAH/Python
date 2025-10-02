#Basic operations on Strings

#CONCATENATION
str1 = "FAHAD"
str2 = "IQBAL"
str3 = (str1 + " " + str2)
print(str3)

#len() function to calculate length
str = "APNA_COLLEGE"
length = len(str)
print(length)

#Indexing
str = "APNA_COLLEGE"
print(str[2])
# str[3] = 10 this is not supported by strings in Python

#Slicing
str = "PYTHON"
print(str[1:4])
print(str[:4])
print(str[1:])


#Other Operations
str = "pYTHON"
print(str.endswith("ON"))
print(str.capitalize())
print(str.replace("p","P"))
print(str.find("HON"))
print(str.count("ON"))


#WAP to input users name and calculate its length

name = input("Enter your Name: ")
print("The Length of name is:", len(name))