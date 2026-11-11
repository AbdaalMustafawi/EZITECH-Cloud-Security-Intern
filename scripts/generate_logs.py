import csv
import random

# Origins and Destinations
cities = ["Lahore", "Karachi", "Islamabad", "Gujranwala"]
# statuses of delivery 
statuses = ["Delivered", "Pending", "In Transit", "Cancelled"]


# Print Headers
print("Origin           ", "Status           ",  "Destination")
# Gives new line after headers printed
print()
# Loop for printing 100 random Origins, statuses and Destinations 
for i in range(100):
    print(f"{random.choice(cities):<15} , {random.choice(statuses):<15} ,  {random.choice(cities):<15}")
    

with open("delivery_logs.csv", "w", newline="") as file:
    writer = csv.writer(file)

