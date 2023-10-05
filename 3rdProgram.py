import pandas as pd

# Step 1: Read the Excel file
file_path = "employee_data.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# Step 2: Sort the dataframe by employee and date
df.sort_values(by=['Employee Name', 'Date'], inplace=True)

# Step 3: Find employees who have worked for more than 14 hours in a single shift
max_shift_duration_hours = 14
long_shift_employees = []

for employee, employee_df in df.groupby('Employee Name'):
    shift_start_time = None
    shift_end_time = None

    for _, row in employee_df.iterrows():
        if shift_start_time is None:
            shift_start_time = row['Date']
        shift_end_time = row['Date']

    if shift_start_time and shift_end_time:
        shift_duration_hours = (shift_end_time - shift_start_time).total_seconds() / 3600
        if shift_duration_hours > max_shift_duration_hours:
            long_shift_employees.append((employee, row['Position']))

# Step 4: Print the names and positions of employees with long shifts
if long_shift_employees:
    print("Employees who have worked for more than 14 hours in a single shift:")
    for employee, position in long_shift_employees:
        print(f"Name: {employee}, Position: {position}")
else:
    print("No employees have worked for more than 14 hours in a single shift.")
