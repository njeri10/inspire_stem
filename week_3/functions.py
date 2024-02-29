# functions in python
# date : 29/02/2024
# name : Edith 
 
# a block of code running together as a unit
# initializing a function / key words called def


def print_name (): 
    print ("My name is  Edith Njeri")


# calling the function 
#print_name ()    

def print_details (name , age , id, gender):
    print(" I am{0}  , {1}years old , My id no is {2} , and gender is {2} " . format(name,age,id,gender))
    
print_details ("Edith Njeri" , "18" , "22144366", "female") 
print_details ("John" , "20" , "28164368", "male") 

def sum_nums (x,y):
    return x + y

def prod_numbers(x,y) :
    return x * y


z = sum_nums (10,20)
print (z)
print (prod_numbers (20,10))


def print_odds (first_no , last_no):
    for i in range(first_no,last_no) :
        print (i % 2)


print_odds (3,19)

# write a function to print all prime nos btwn 1-99
# write a function to print all squares, cubes of no btwn 1-10
# write a function to calculate sa of cylinder,cone,cube and sphere and volume of the 4



