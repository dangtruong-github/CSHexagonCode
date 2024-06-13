age = int(input("Enter the age"))

# correct: age >= 0 and age <= 2
# incorrect: age >= 0 and <= 2
if age >= 0 and age <= 2:
    print("baby")
elif age >= 3 and age <= 39:
    print("young adults")
elif age >= 40 and age <= 59:
    print("Middle-aged Adults")
elif age >= 60 and age <= 99:
    print("Old adults")
