import csv

# Step 1: Generate students.csv with names and marks in 3 subjects
students_data = [
    {"Name": "ram" , "Math": 16 , "Science": 14 , "English": 17},
    {"Name": "lal" , "Math": 17 , "Science": 12, "English": 19},
    {"Name": "kishore" , "Math": 14 , "Science": 16, "English": 15},
  
]

csv_filename = "students.csv"
fieldnames = ["Name", "Math", "Science", "English"]

# Write data to CSV
with open(csv_filename, mode="w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for student in students_data:
        writer.writerow(student)

# Step 2: Read the CSV and calculate total and average marks for each student
with open(csv_filename, mode="r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    print(f"{'Name':<10} {'Total':<6} {'Average':<7}")
    print("-" * 26)
    for row in reader:
        marks = [int(row["Math"]), int(row["Science"]), int(row["English"])]
        total = sum(marks)
        average = total / len(marks)
        print(f"{row['Name']:<10} {total:<6} {average:<7.2f}")
