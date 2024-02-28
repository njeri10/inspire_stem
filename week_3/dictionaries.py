
laptop = { "make":"HP","colour": "grey", "weight": "1.3","year": "2022"} 


print (laptop["make"])
print (laptop["colour"])
print (laptop["year"])

# change values in dictionaries
laptop  ["colour"] = "red"
laptop  [ "year"] = "2010"

print(laptop)

laptop ["size" ] = "120m * 60m"
print (laptop)

del  laptop ["colour" ] 
print(laptop)

siz_laptop = laptop.copy
print(laptop)

""""""

for key,value in laptop.items():
    print (key)
    print("\n")
    print(value)
