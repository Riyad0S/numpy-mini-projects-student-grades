import numpy as np

#rows are students, columns are grades
students_grades = np.array([[90, 85, 88],
                            [70, 65, 72],
                            [100, 98, 95],
                            [80, 79, 83],
                            [60, 55, 58]])

# Printing each student grade
print("--" * 50)
print("Student 1", students_grades[0])
print("Student 2", students_grades[1])
print("Student 3", students_grades[2])
print("Student 4", students_grades[3])
print("Student 5", students_grades[4])
print("--" * 50)

# printing grades in an array
print(students_grades)
print("--" * 50)

print("Student 1 average scores: ", np.mean(students_grades[0]))
print("Student 2 average scores: ", np.mean(students_grades[1]))
print("Student 3 average scores: ", np.mean(students_grades[2]))
print("Student 4 average scores: ", np.mean(students_grades[3]))
print("Student 5 average scores: ", np.mean(students_grades[4]))
print("--" * 50)

# one array averages
print("Students average: ", np.mean(students_grades, axis = 1))
print("--" * 50)

print("Exams average: ", np.mean(students_grades, axis = 0))
print("--" * 50)

print("Highest grade: ", np.max(students_grades))
print("--" * 50)

print("Lowest grade: ", np.min(students_grades))
print("--" * 50)

print("Class average: ", np.mean(students_grades))

students_average = np.mean(students_grades, axis = 1)
print("Students that passed:\n", students_average >= 70)
print("--" * 50)

# each student
print("Student 1: ", "Passed" if students_average[0] >= 70 else "Failed")
print("Student 2: ", "Passed" if students_average[1] >= 70 else "Failed")
print("Student 3: ", "Passed" if students_average[2] >= 70 else "Failed")
print("Student 4: ", "Passed" if students_average[3] >= 70 else "Failed")
print("Student 5: ", "Passed" if students_average[4] >= 70 else "Failed")

students_grades += 5
students_grades = np.clip(students_grades, 0, 100)
# printing grades after bonus
print(students_grades)
print("--" * 50)

students_average = np.mean(students_grades, axis = 1)
highest_grade = np.argmax(students_average)

print("Top student:", highest_grade + 1)
print("Grades:", students_grades[highest_grade])
print("Average:", np.mean(students_grades[highest_grade]))

