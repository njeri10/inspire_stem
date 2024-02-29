# prime numbers in python
# date : 29/02/2024
# name : Edith 



def prime_no (x,y) :
    for i in range (x,y + 1,2):
        print(i)

        x= 1
        y = 99

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))

if x % 2 :
    prime_no (x + 1,y)

else :
    prime_no (x,y)