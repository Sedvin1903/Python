# STRING Methods 

txt = "Hello world."


# capitalize()
S = txt.capitalize()
print("String: ",S)
print("\n")

# casefold()
S = txt.casefold()
print("String : ",S)
print("\n")

# center()
S =txt.center(20)
print("String : ",S)
print("\n")

# count()
txt1 = "I love apples, apple are my favorite fruit"
S =txt1.count("apple")
print("String : ",S)
print("\n")

# encode()
S =txt.encode()
print("String : ",S)
print("\n")

# endswith()
S =txt.endswith(".")
print("String : ",S)
print("\n")

# expandtabs()
txt2 = "H\te\tl\tl\to"
S = txt2.expandtabs(2)
print("String : ",S)
print("\n")

# find()
S =txt.find("world")
print("String : ",S)
print("\n")

# format()
txt3 = "For only {price:.2f} dollars!"
print(txt3.format(price = 49))
print("String : ",S)
print("\n")

# format_map()
S =txt.format_map("W")
print("String : ",S)
print("\n")

# index()
S =txt.index("world")
print("String : ",S)
print("\n")

# isalnum()
txt4 = "Company12"
S =txt4.isalnum()
print("String : ",S)
print("\n")

# isalpha()
txt4 = "CompanyX"
S =txt4.isalpha()
print("String : ",S)
print("\n")

# isascii()
S =txt4.isascii()
print("String : ",S)
print("\n")

# isdecimal()
txt5 = "\u0033" #unicode for 3
S =txt5.isdecimal()
print("String : ",S)
print("\n")

# isdigit()
txt6 = "50800"
S =txt6.isdigit()
print("String : ",S)
print("\n")

# isidentifier()
S =txt4.isidentifier()
print("String : ",S)
print("\n")

# islower()
txt7 = "hello world!"
S =txt7.islower()
print("String : ",S)
print("\n")

# isnumeric()
S =txt6.isnumeric()
print("String : ",S)
print("\n")

# isprintable()
txt8 = "Hello! Are you #1?"
S =txt8.isprintable()
print("String : ",S)
print("\n")

# isspace()
txt9 = "   "
S =txt9.isspace()
print("String : ",S)
print("\n")

# istitle()
txt10 = "Hello, And Welcome To My World!"
S =txt10.istitle()
print("String : ",S)
print("\n")

# isupper()
txt1 = "THIS IS NOW!"
S =txt1.isupper()
print("String : ",S)
print("\n")

# join()
myTuple = ("John", "Peter", "Vicky")
S ="#".join(myTuple)
print("String : ",S)
print("\n")

# ljust()
txt2 = "banana"
s = txt2.ljust(20)
print(s, "is my favorite fruit.")
print("String : ",s)
print("\n")

# lstrip()
txt3 = "     banana     "
S =txt3.lstrip()
print("String : ",S)
print("\n")

# maketrans()
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print("String : ",txt.translate(mytable))
print("\n")

# partition()
txt4 = "I love apples, apple are my favorite fruit"
S =txt4.partition("apple")
print("String : ",S)
print("\n")

# replace()
txt5 = "I like bananas"
S =txt5.replace("bananas", "apples")
print("String : ",S)
print("\n")

# rfind()
txt6 = "Mi casa, su casa."
S =txt6.rfind("casa")
print("String : ",S)
print("\n")

# rindex()
S =txt6.rindex("casa")
print("String : ",S)
print("\n")

# rjust()
s = txt2.rjust(20)
print(s, "is my favorite fruit.")
print("String : ",s)
print("\n")

# rpartition()
txt7 = "I could eat bananas all day, bananas are my favorite fruit"
S =txt7.rpartition("bananas")
print("String : ",S)
print("\n")

# rsplit()
txt8 = "apple, banana, cherry"
S =txt8.rsplit(", ")
print("String : ",S)
print("\n")

# rstrip()
#txt3 = "     banana     "
S =txt3.rstrip()
print("String : ",S)
print("\n")

# split()
S =txt.split()
print("String : ",S)
print("\n")

# splitlines() 
txt8 = "Thank you for the music\nWelcome to the jungle"
S =txt8.splitlines()
print("String : ",S)
print("\n")

# startswith()
S =txt.startswith("Hello")
print("String : ",S)
print("\n")

# strip()
S =txt3.strip()
print("String : ",S)
print("\n")

# swapcase()
S =txt.swapcase()
print("String : ",S)
print("\n")

# title()
S =txt.title()
print("String : ",S)
print("\n")

# translate()
mydict = {83:  80}
txt = "Hello Sam!"
print("String : ",txt.translate(mydict))
print("\n")

# upper()
txt9 = "hello world!"
S =txt9.upper()
print("String : ",S)
print("\n")

# zfill()
txt10 = "50"
S =txt10.zfill(10)
print("String : ",S)
print("\n")
