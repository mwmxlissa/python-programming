import csv
import random

# Define the initial data and generate sample data
data = [
    {"Name": "Alice", "Age": random.randint(20, 40), "City": "Ebbw Vale"},
    {"Name": "Bob", "Age": random.randint(20, 40), "City": "Tredegar"},
    {"Name": "Charlie", "Age": random.randint(20, 40), "City": "Newport"},
    {"Name": "David", "Age": random.randint(20, 40), "City": "Caerphilly"},
    {"Name": "Eve", "Age": random.randint(20, 40), "City": "Llantrisant"},
    {"Name": "Frank", "Age": random.randint(20, 40), "City": "Port Talbot"}
]

# Define the CSV file name
csv_file = "Student.csv"

# Check if the file already exists to avoid overwriting
try:
    with open(csv_file, mode='x', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
        writer.writeheader()
        for row in data:
            writer.writerow(row)
    print(f"Initial data has been saved to {csv_file}")
except FileExistsError:
    print(f"{csv_file} already exists. New data will be appended.")

# Function to append new data to the CSV file
def append_data_to_csv(file_name):
    while True:
        name = input("Enter Name (or type 'exit' to stop): ")
        if name.lower() == 'exit':
            break
        city = input("Enter City: ")
        age = random.randint(20, 40)  # Generate a random age for the new entry

        new_entry = {"Name": name, "Age": age, "City": city}

        with open(file_name, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=["Name", "Age", "City"])
            writer.writerow(new_entry)

        print(f"New entry {new_entry} has been appended to {file_name}")

# Call the function to append data
append_data_to_csv(csv_file)