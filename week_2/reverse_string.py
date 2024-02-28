# program that checks whether a string is reversed
# Date : 23/02/2024
# Name : Edith

name = input (" ")
l_name = len(name)
rev_name = " "
 
for i in range(l_name -1,-1,-1) :
    rev_name += name [i]

print("Result is : " ,rev_name)
if(rev_name == name) :
  print(" PALINDROME")
else: 
  print(" NOT A PALINDROME")
  