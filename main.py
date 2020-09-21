#  Is prime Project

#  Gets initial num value
num = input("Please enter the number you would like to check if prime: ")
number = 0

#  Checks to make sure input is convertible to float number and assigns float value
while type(number) != float:

    try:
        number = float(num)
    except ValueError:
        print("That doesn't seem to be a number. \n")
        num = input("Please input a number: ")
number = int(number)  # Reformatting number to an int, I tried doing this in above loop but threw error so did this way


factor = [1, number]
#  For loop to check if number is prime and add to factors list if not
for i in range(2, number):

    if number % i == 0:
        factor.append(i)

#  Prints results based on whether or not the number is prime
if len(factor) >= 3:
    print(f"{number} is not a prime because it is divisible by: {factor[2]}.")
elif number == 0:
    print("0 is not a prime number.")
else:
    print(f"{number} is a prime.")
