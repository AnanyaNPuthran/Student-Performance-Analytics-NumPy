import numpy as np
# Creating a 2D array of student marks
marks = np.array([
    [85, 78, 92, 88, 80],
    [76, 85, 79, 90, 82],
    [95, 92, 89, 94, 96],
    [45, 55, 60, 50, 48],
    [67, 72, 70, 75, 69],
    [88, 91, 85, 89, 92],
    [32, 45, 50, 40, 38],
    [90, 87, 93, 95, 91],
    [56, 62, 58, 65, 60],
    [78, 80, 82, 75, 79],
    [92, 95, 90, 88, 94],
    [35, 28, 42, 38, 30],
    [81, 84, 86, 80, 83],
    [69, 74, 71, 68, 73],
    [98, 96, 94, 97, 99],
    [50, 48, 55, 52, 58],
    [87, 89, 91, 85, 88],
    [73, 68, 76, 70, 74],
    [40, 35, 38, 42, 45],
    [94, 90, 96, 92, 95]
])

# Subject names
subjects = np.array([
    "Python",
    "Mathematics",
    "Statistics",
    "Computer Science",
    "Database Management"
])

# Student names
students = np.array([f"Student {i}" for i in range(1, 21)])


# Q1. ARRAY CREATION AND DIMENSIONS

print("\n========== Q1: ARRAY CREATION AND DIMENSIONS ==========")

print("Complete Marks Array:")
print(marks)

print("Shape:", marks.shape)
print("Size:", marks.size)
print("Number of Dimensions:", marks.ndim)
print("Data Type:", marks.dtype)


# Q2. ARRAY INDEXING AND SLICING

print("\n========== Q2: ARRAY INDEXING AND SLICING ==========")

print("First 5 Students:")
print(marks[:5])

print("Python Marks of All Students:")
print(marks[:, 0])

print("Students 5 to 10 in Mathematics and Statistics:")
print(marks[4:10, 1:3])

print("Last 5 Students:")
print(marks[-5:])


# Q3. MATHEMATICAL OPERATIONS

print("\n========== Q3: MATHEMATICAL OPERATIONS ==========")

# Total marks of each student
total = np.sum(marks, axis=1)
print("Total Marks:")
print(total)

# Percentage of each student
percentage = (total / 500) * 100
print("Percentage:")
print(percentage)

# Add 5 grace marks (maximum 100)
grace_marks = np.clip(marks + 5, 0, 100)
print("Marks After Grace Marks:")
print(grace_marks)

# Difference between highest and lowest marks
difference = np.max(marks, axis=1) - np.min(marks, axis=1)
print("Difference:")
print(difference)


# Q4. STATISTICAL CALCULATIONS

print("\n========== Q4: STATISTICAL CALCULATIONS ==========")

# Average marks in each subject
subject_average = np.mean(marks, axis=0)
print("Subject Average:")
print(subject_average)

# Highest marks in each subject
print("Highest Marks:")
print(np.max(marks, axis=0))

# Lowest marks in each subject
print("Lowest Marks:")
print(np.min(marks, axis=0))

# Overall class average
print("Overall Class Average:")
print(np.mean(marks))

# Standard deviation
print("Standard Deviation:")
print(np.std(marks, axis=0))

# Subject with highest average
print("Highest Average Subject:")
print(subjects[np.argmax(subject_average)])

# Subject with lowest average
print("Lowest Average Subject:")
print(subjects[np.argmin(subject_average)])


# Q5. CONDITIONAL INDEXING

print("\n========== Q5: CONDITIONAL INDEXING ==========")

# Students scoring above 80%
print("Students Above 80%:")
print(students[percentage > 80])

# Students who failed in at least one subject
failed = np.any(marks < 35, axis=1)
print("Students Failed in At Least One Subject:")
print(students[failed])

# Students scoring above 90 in Python
print("Students Scoring Above 90 in Python:")
print(students[marks[:, 0] > 90])

# Count students who passed all subjects
passed = np.all(marks >= 35, axis=1)
print("Total Students Passed All Subjects:")
print(np.sum(passed))


# Q6. ARRAY MANIPULATION

print("\n========== Q6: ARRAY MANIPULATION ==========")

# Sort students based on total marks (descending)
sorted_indices = np.argsort(total)[::-1]

print("Students Sorted by Total Marks:")
print(students[sorted_indices])

# Top 3 students
print("Top 3 Students:")
print(students[sorted_indices[:3]])

print("Top 3 Marks:")
print(total[sorted_indices[:3]])

# Reshape into 3D array
array_3d = marks.reshape(4, 5, 5)
print("3D Array:")
print(array_3d)

# Flatten into 1D array
flat_array = marks.flatten()
print("1D Array:")
print(flat_array)

# Replace marks below 35 with zero
new_marks = np.where(marks < 35, 0, marks)
print("Marks After Replacing Below 35 With Zero:")
print(new_marks)


print("\n========== PROJECT COMPLETED SUCCESSFULLY ==========")
