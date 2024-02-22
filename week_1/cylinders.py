# This is a program to show how to calculate area and volume of sphere
 # Date:20/02/2024
 # Name Edith Njeri
import math

#height and radius of the cylinder
height = 6
radius = 5

#calculating the lateral surface area
cyl_lsa = 2*(math.pi)*(radius)*(height)

#calculating the total surface area
cyl_tsa = 2*(math.pi)*(radius)*(radius + height)

#calculating the volume
cyl_volume = (math.pi)*(radius)*(radius)*(height)

#displaying the area and volume
print("Lateral Surface Area of the cylinder: ", str(cyl_lsa))
print("Total Surface Area of the cylinder: ", str(cyl_tsa))
print("Volume of the cylinder: ", str(cyl_volume))
