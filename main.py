#Text pg. 45 Exercise 2.11(b) :

AvgAge = round((17*9+24*10+21*11+27*12)/89.0) #finding avg of given numbers
print(f"The average age is: {AvgAge}") #printing the result

#Text pg. 45 Exercise 2.11(d) :

import math #importing math to use floor function later

numTime = 4356/61 #math to find exactly how many times 61 fits into 4356
numWhole = math.floor(numTime) #Finds lower val so that its a whole number

print(f"The number of times 61 goes into 4356 = {numWhole}")

#Text pg. 46 Exercise 2.14(b) :

s = "goodbye"  #Told me to create and assign s

#Bool expression and a little if statement and print statement to verify
if s[6] == "g":
    print("The seventh character of var 's' is g!")
else:
    print("The seventh character of var 's' isn't g.")


#Text pg. 46 Exercise 2.14(d) :

s = "goodbye" #Told me to create and assign s

#Bool expression and a little if statement and print statement to verify
if s[-2] == "x":
    print("The second from last character of var 's' is x!")
else:
    print("The second from last character of var 's' isn't x.")


#Text pg. 46 Exercise 2.16(e) :

#Assigning names to vars
first = "Bob"
middle = "John"
last = "Smith"

#concatination of names to full name
fullname = first + " " + middle + " " + last

#printing all the vars from the prob in a nice format
print(f"The fullname is: {fullname} \n The first name is: {first} \n The middle name is: {middle} \
\n The last name is: {last}")