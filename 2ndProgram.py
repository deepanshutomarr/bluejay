import pandas as pd

# Step 1: Read the Excel file
file_path = "employee_data.xlsx"
df = pd.read_excel(file_path, engine='openpyxl')

# Step 2: Sort the dataframe by employee and date
df.sort_values(by=['Employee Name', 'Date'], inplace=True)

# Step 3: Find employees who have less than 10 hours between shifts but greater than 1 hour
shift_gap_threshold_min = 60  # 1 hour in minutes
max_shift_gap_min = 600  # 10 hours in minutes
shift_gap_employees = []

for employee, employee_df in df.groupby('Employee Name'):
    last_shift_end = None

    for _, row in employee_df.iterrows():
        if last_shift_end is not None:
            time_between_shifts_min = (row['Date'] - last_shift_end).total_seconds() / 60
            if shift_gap_threshold_min < time_between_shifts_min < max_shift_gap_min:
                shift_gap_employees.append((employee, row['Position']))
        last_shift_end = row['Date']

# Step 4: Print the names and positions of employees who meet the criteria
if shift_gap_employees:
    print("Employees with less than 10 hours between shifts but greater than 1 hour:")
    for employee, position in shift_gap_employees:
        print(f"Name: {employee}, Position: {position}")
else:
    print("No employees meet the criteria.")
