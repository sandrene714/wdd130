# I added an option for the user to type yes or no 
# if they want to buy the tires it will save their phone numbers and save it to volumes.txt
import math
from datetime import datetime

width = float(input("What is the width of the tire in mm? "))
aspect_ratio = float(input("What is the ratio of the tire? "))
diameter = float(input("What us the diameter of the wheel in inches? "))

volume = (math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000000

print(f"The estimation of the volume would be {volume:.2f} liters")

current_date = datetime.now()
date = f"{current_date:%Y-%m-%d}"

with open("volumes.txt", "at") as volumes_file:
    print(f"{date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}", file=volumes_file)

purchase_tire = input("Would you like to buy these tires? (yes/no): ").lower()

if purchase_tire == "yes":
    phone_number = input("What is your phone number?: ")
    with open("volumes.txt", "at") as volumes_file:
       print(f"The customer phone number is: {phone_number}", file=volumes_file)

elif purchase_tire == "no":
    print("Thank you for participating")

else: 
    print("Types yes or no.")

print("The tire information has been saved succesfully")
