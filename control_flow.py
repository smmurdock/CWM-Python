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
