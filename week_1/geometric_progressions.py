# program to show geometric progression
 # Date:20/02/2024
 # Name: Edith Njeri 

 # 1.Take input of 'a','r' ans 'n'
a = int(input("Enter the value of a: "))
r = int(input("Enter the value of r: "))
n = int(input("Enter the value of n: "))

# 2. Loop for n terms
for i in range(1,n+1):
    t_n = a * r**(i-1)
    print(t_n)


if(r>1):
  S_n = (a*(r**n))/(r-1)
else:
  S_n = (a*(r**n))/(1-r)
 
print("Sum of n terms: ",S_n)

a= 1
r= 2
n= 5




