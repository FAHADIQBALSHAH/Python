tup = (1,2,3,4)
print(tup)
print(type(tup))
print(tup[1])

# tup[2] = 5 tupples are immutable.

#Empty Tupple
tup = ()
print(tup)
print(type(tup))

#Single element Tupple
tup = (1,)  #Here (,) after inserting the single element is important.
print(tup)
print(type(tup))

#Single element without using comma(,)
tup = (1)
print(tup)
print(type(tup))

tup = (1.0)
print(tup)
print(type(tup))

tup = ("A")
print(tup)
print(type(tup))

tup = (2,1,3,1,4)
print(tup.index(1))
print(tup.count(1))


#Give count of students with Grade A in the given tuple

grade = ("A", "B", "C", "A", "C", "A", "B", "A")
print(grade)
print(grade.count("A"))