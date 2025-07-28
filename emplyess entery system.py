# General-purpose Employee Entry System

# Step 1: Create a list or dictionary of allowed employees
# You can use either ID or Name depending on your organization
allowed_employees = {
    "EMP001": "John Doe",
    "EMP002": "Jane Smith",
    "EMP003": "Michael Johnson",
    # Add more employee IDs and names here
}

def employee_entry_system():
    print("=== Employee Entry System ===")
    emp_id = input("Enter your Employee ID: ").strip().upper()

    # Step 2: Check if the entered ID is in the allowed list
    if emp_id in allowed_employees:
        print(f"✅ Access Granted. Welcome, {allowed_employees[emp_id]}!")
    else:
        print("❌ Access Denied. You are not registered as an employee.")

# Step 3: Run the system
if __name__ == "__main__":
    employee_entry_system()
