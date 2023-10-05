import pandas as pd

# Step 1: Read the Excel file
file_path = "employee_data.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# Step 2: Sort the dataframe by employee and date
df.sort_values(by=['Employee Name', 'Date'], inplace=True)

# Step 3: Find employees who worked for 7 consecutive days
consecutive_days = 7
consecutive_employees = []

for employee, employee_df in df.groupby('Employee Name'):
    consecutive_count = 0
    last_date = None

    for _, row in employee_df.iterrows():
        if last_date is None:
            consecutive_count = 1
        elif (row['Date'] - last_date).days == 1:
            consecutive_count += 1
        else:
            consecutive_count = 1

        if consecutive_count >= consecutive_days:
            consecutive_employees.append((employee, row['Position']))
            break

        last_date = row['Date']

# Step 4: Print the names and positions of employees who worked for 7 consecutive days
if consecutive_employees:
    print("Employees who worked for 7 consecutive days:")
    for employee, position in consecutive_employees:
        print(f"Name: {employee}, Position: {position}")
else:
    print("No employees worked for 7 consecutive days.")
