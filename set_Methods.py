# SET Methods 

fruits = {"apple", "banana", "cherry"}


# add()

fruits.add("orange")
print("Set :",fruits)
print("\n")

# copy()
s = fruits.copy()
print("Set :",fruits)
print("Set :",s)
print("\n")

# clear()
s.clear()
print("Set :",fruits)
print("Set :",s)
print("\n")

# difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print("Set :",z)
print("\n")

# difference_update()
x.difference_update(y)
print("Set :",x)
print("\n")

# discard()
fruits.discard("banana")
print("Set :",fruits)
print("\n")

# intersection()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print("Set :",z)
print("\n")

# intersection_update()
x.intersection_update(y)
print("Set :",x)
print("\n")

# isdisjoint()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print("Set :",z)
print("\n")

# issubset()
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print("Set :",z)
print("\n")

# issuperset()
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print("Set :",z)
print("\n")

# pop()
fruits.pop()
print("Set :",fruits)
print("\n")

# remove()
fruits.remove("apple")
print("Set :",fruits)
print("\n")

# symmetric_difference()
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
print("Set :",z)
print("\n")

# symmetric_difference_update()
x.symmetric_difference_update(y)
print("Set :",x)
print("\n")

# union() 
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
print("Set :",z)
z = x.union(y)
print("\n")

# update()
x.update(y)
print("Set :",x)
print("\n")
