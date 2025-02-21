#############################################################
# Comparison Operators
print(10 > 3)
print(10 >= 3)
print(10 < 20)
print(10 <= 20)
print(10 == 10)
print(10 == "10")
print(10 != "10")
print("bag" > "apple")
print("bag" == "BAG")
print(ord("b"))
print(ord("B"))

#############################################################
# Conditional Statements
temperature = 15
if temperature > 30:
    print("It's warm")
    print("Drink water")
elif temperature > 20:
    print("It's nice")
else:
    print("It's cold")
print("Done")

#############################################################
# Ternary Operator
age = 22
if age >= 18:
    print("Eligible")
else:
    print("Not eligible")

# Achieve the same result with different syntax
if age >= 18:
    message = "Eligible"
else:
    message = "Not eligible"
print(message)

# Achieve the same result with a ternary operator
age = 12
message = "Eligible" if age >= 18 else "Not eligible"
print(message)

#############################################################
# Logical Operators
# and, or, not
high_income = False
good_credit = True
student = False

# Version 1
if high_income and good_credit:
    print("Eligible")
else:
    print("Not eligible")

# Version 2
if high_income or good_credit:
    print("Eligible")
else:
    print("Not eligible")

# Version 3
if not student:
    print("Eligible")
else:
    print("Not eligible")

# Version 4
if (high_income or good_credit) and not student:
    print("Eligible")

#############################################################
# Short-circuit Evaluation
# As soon as one of these values is False, the program will
# # stop evaluating the rest of the values
# This is called short-circuit evaluation

high_income = False
good_credit = True
student = True

if high_income and good_credit and not student:
    print("Eligible")

if high_income or good_credit or not student:
    print("Eligible")

#############################################################
# Chaining Comparison Operators
# age should be between 18 and 65
age = 22
if age >= 18 and age < 65:
    print("Eligible")

if 18 <= age < 65:
    print("Eligible")

#############################################################
# For Loops
print("Sending a message")
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")

for number in range(1, 4):
    print("Attempt", number, (number) * ".")


for number in range(1, 10, 2):
    print("Attempt", number, (number) * ".")

#############################################################
# For...Else
successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

#############################################################
# Nested Loops
for x in range(5):
    for y in range(3):
        print(f"({x}, {y})")

#############################################################
# Iterables
print(type(5))
print(type(range(5)))

# Iterable
for x in range(5):
    print(x)

for x in "Python":
    print(x)

for x in [1, 2, 3, 4]:
    print(x)

# for item in shopping_cart:
#     print(item)

#############################################################
# While Loops
# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# # Be careful to ensure there is a way to break out of the loop
# # otherwise it will run indefinitely and crash your program

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

#############################################################
# Infinite Loops
# A loop that runs foreber
# while True:
#     command = input(">")
#     print("ECHO", command)
#     # This will allow you to break out of the loop
#     if command.lower() == "quit":
#         break  # without a way out, your program may run out of memory and crash

#############################################################
# Exercise
# Write a program to display the even numbers between 1 and 10
count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)

print(f"We have {count} even numbers")
