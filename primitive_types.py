import math

#############################################################
# Variables
students_count = 1000
rating = 4.99
is_published = False
course_name = "Python Programming"
print(students_count)

#############################################################
# Variable Names
# 1. Use descriptive names
# 2. Use lowercase letters
# 3. Use underscore to separate words (snake_case)
# 4. Use spaces around equal signs

#############################################################
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

#############################################################
# Formatted Strings
first = "Shanay"
last = "Murdock"
full = first + " " + last
print(full)
full = f"{first} {last}"
print(full)

#############################################################
# String Methods
course = "Python Programming"
print(course.upper())
course_upper = course.upper()
print(course)
print(course.lower())

course = "python programming"
print(course.title())

course = "    Python Programming  "
print(course.strip())
print(course.lstrip())
print(course.rstrip())

course = "Python Programming"
print(course.find("Pro"))  # returns index; -1 means not found
print(course.replace("P", "-"))
print("Pro" in course)  # returns boolean
print("swift" not in course)

#############################################################
# Numbers
x = 1
x = 1.1
x = 1 + 2j  # a + bi
print(10 + 3)
print(10 - 3)
print(10 * 3)
print(10 / 3)  # returns float
print(10 // 3)  # returns integer
print(10 % 3)  # returns remainder
print(10 ** 3)

# Augmented Assignment Operator
x = 10
x = x + 3
x += 3
x -= 3
x *= 3
x /= 3
print(x)

#############################################################
# Working with Numbers
print(round(2.9))
print(abs(-2.9))

# import math module for more complex math functions (import at top)
print(math.ceil(2.2))
# Google Python 3 math modules for more functions
print(math.floor(2.9))
