nums = {1,2,3,4,5}
print(nums)
print(type(nums))
print(len(nums))

nums2 = {1,2,2,2,3,4} #2 will get printed only once
print(nums2)
print(len(nums2))

null_set = set()
print(null_set)
print(type(null_set))
print(len(null_set))

null_set.add(10)
null_set.add(20)
null_set.add(30)
null_set.add(40)
print(null_set)

null_set.remove(10)
print(null_set)
print(null_set.pop())
null_set.clear()
print(null_set)

set1 = {10,20,30,40}
set2 = {30,40,50,60}

set3 = set1.union(set2)
print("UNION", set3)

set4 = set1.intersection(set2)
print("INTERSECTION", set4)