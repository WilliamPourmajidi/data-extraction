import random
import matplotlib.pyplot as plt

# Generate 5 random grades for 5 students
grades = [random.randint(0, 100) for _ in range(5)]

# Sort the grades in descending order
grades.sort(reverse=True)

# Visualize the grades
plt.bar(range(len(grades)), grades)
plt.title('Grades')
plt.xlabel('Student')
plt.ylabel('Grade')
plt.xticks(range(len(grades)), [f'Student {i+1}' for i in range(len(grades))])
plt.show()