# program to check if string is palindrome or not
# Date : 22/02/2024
# Name : Edith

my_str = 'aIbohPhoBiA'

# make it suitable for caseless comparison
my_str = my_str. casefold ()

#reverse the string
rev_str = reversed(my_str)

#check if the string is equal to its reverse
if list(my_str) == list(rev_str) :
    print("The string is a palindrome.")
else :
    print("The string is not a palindrome. ")
    

