# Define the employee data as a list of dictionaries
employee_data = [
    {"Employee ID": "161E90", "Name": "Raman", "Age": 41, "Salary (PM)": 56000},
    {"Employee ID": "161F91", "Name": "Himadri", "Age": 38, "Salary (PM)": 67500},
    {"Employee ID": "161F99", "Name": "Jaya", "Age": 51, "Salary (PM)": 82100},
    {"Employee ID": "171E20", "Name": "Tejas", "Age": 30, "Salary (PM)": 55000},
    {"Employee ID": "171G30", "Name": "Ajay", "Age": 45, "Salary (PM)": 44000},
]

# Function to sort employee data based on the selected parameter
def sort_employee_data(data, sort_param):
    if sort_param == 1:
        return sorted(data, key=lambda x: x["Age"])
    elif sort_param == 2:
        return sorted(data, key=lambda x: x["Name"])
    elif sort_param == 3:
        return sorted(data, key=lambda x: x["Salary (PM)"])
    else:
        return data

# Input from the user to select sorting parameter
print("Choose a sorting parameter:")
print("1. Age")
print("2. Name")
print("3. Salary")
sort_param = int(input("Enter the number corresponding to the sorting parameter: "))

# Sort the data based on the selected parameter
sorted_employee_data = sort_employee_data(employee_data, sort_param)

# Print the sorted data
print("\nSorted Employee Data:")
for employee in sorted_employee_data:
    print(f"Employee ID: {employee['Employee ID']}, Name: {employee['Name']}, Age: {employee['Age']}, Salary (PM): {employee['Salary (PM)']}")