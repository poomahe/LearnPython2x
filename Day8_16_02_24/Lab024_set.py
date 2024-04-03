set1 = {1,2,3}
set2 = {4,5,6}
set3 = set1.union(set2)
print(set3)

set4 = {1,2,3,4,5}
set5= {4,5,6,7,8}
diffe = set4.difference(set5)
print(diffe)

#userful in API
set6 = {1,2,3,4,5}
set7 = {2,3,4}
subs = set7.issubset(set6)
print(subs)