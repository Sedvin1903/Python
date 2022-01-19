
# DICTIONARY Methods 

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# copy()
Car = car.copy()
print("Dictionary :",car)
print("Dictionary :",Car)
print("\n")

# clear()
car.clear()
print("Dictionary :",car)
print("Dictionary :",Car)
print("\n")

# fromkeys()
x = ['key1', 'key2', 'key3']
y = 0
car = dict.fromkeys(x, y)
print("Dictionary :",car)
print("\n")

# get()
d = Car.get("model")
print("Value of key \'model\':",d)
print("\n")

# items()
d = Car.items()
print("Dictionary LIST :",d)
print("\n")

# keys()
d = car.keys()
print("Dictionary KEY list:",d)
print("\n")

# pop()
Car.pop("model")
print("Dictionary :",Car)
print("\n")

# popitem()
Car.popitem()
print("Dictionary :",Car)
print("\n")

# setdefault()
d = Car.setdefault("model", "Bronco")
print("Dictionary :",Car)
print("\n")

# update()
Car.update({"color": "White"})
print("Dictionary :",Car)
print("\n")

# values()
d = Car.values()
print("Dictionary VALUES list:",d)
print("\n")
