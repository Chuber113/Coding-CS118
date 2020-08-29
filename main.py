#imports librarys
import math
#predefines variables we are going to use
diam = 0.0
circ = 0.0
SA = 0.0
vol = 0.0
radius = "Placeholder"

#Gets initial rad(ius) value
rad = input("Please enter the radius of the sphere: ")


#Checks to make sure input is convertable to float number and assigns float value
while type(radius) != float:

    try:
        radius = float(rad)
    except ValueError:
        print("That doesn't seem to be a number. \n")
        rad = input("Please input a number: ")

#Calculates the diameter
diam = 2 * radius
#Calculates the circumference
circ = 2 * math.pi * radius
#Calculates the surface area
SA = 4 * math.pi * radius**2
#Calculates the volume
vol = (4/3) * math.pi * radius**3

#Prints all the sphere info using f-string formatting
print(f"With your input of {radius}\nThe diameter of the sphere is {diam}\nThe circumference of the sphere is {circ}\n"
      f"The surface area of the sphere is {SA}\nAnd the volume of the sphere is {vol}")
