print("===== Student Grader System =====")

while True:
    name = input("\nEnter student name: ")

    marks = []
    for i in range(1, 4):
        mark = float(input(f"Enter mark {i}: "))
        marks.append(mark)

    average = sum(marks) / len(marks)

    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\n===== RESULTS =====")
    print(f"Student: {name}")
    print(f"Average: {round(average, 2)}")
    print(f"Grade: {grade}")

    choice = input("\nDo you want to grade another student? (yes/no): ").lower()
    if choice != "yes":
        break

print("\nProgram Ended.")