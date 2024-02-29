# program to find sa and volume of cone
# date : 29/02/2024
# name : Edith

import math

# area of cone

r= float(input("Enter the radius of cone (cm):"))
h= float(input("Enter the height of cone (cm):"))
l= float(input("Enter the slanting height of cone (cm):"))



def cone_SA(surface_a):
    surface_a = ((math.pi *(r**2))) + (math.pi *r * r *1)
    print ("The surface area of the cone is{0}" .format(surface_a))
    
    cone_SA_SA({0})

# volume of cone
    def cone_vol(volume):
        volume = ((1/3) * math.pi* (r**2)*h)
                  
        
        print("The volume of the cone is {0}cubed cm" . format (volume))

        cone_vol ({0})