# Given the age of a person as an input, output their age group.
# Here are the age groups you need to handle:
# Child: 0 to 11
# Teen: 12 to 17
# Adult: 18 to 64

age = int(input())
if age > 0 and age <= 11:
    print("Child")
elif age >= 12 and age <= 17:
    print("Teen")
elif age >= 18 and age <= 64:
    print("Adult")
# -- also you could use this --
# else:
#   print("Adult")   instead of last conditional statement