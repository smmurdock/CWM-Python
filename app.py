# Variables
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(students_count)

# Variable Names
# 1. Use descriptive names
# 2. Use lowercase letters
# 3. Use underscore to separate words (snake_case)
# 4. Use spaces around equal signs

# Strings
course = "Python Programming"
print(len(course))
print(course[0])
print(course[-1])
print(course[0:3])
print(course[0:])
print(course[:3])
print(course[:])
print(course[1:-1])

# Escape Sequences
course = 'Python "Programming'
course = "Python \"Programming"
course = "Python \nProgramming"
course = "Python \tProgramming"
print(course)

# \"
# \'
# \\
# \n

# Formatted Strings
first = "Shanay"
last = "Murdock"
full = first + " " + last
print(full)
full = f"{first} {last}"
print(full)
