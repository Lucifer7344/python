marks = int(input("Enter the marks of the student:"))
if (marks>=90):
    print("Grade: A")
elif (marks<90 and marks>=80):
    print("Grade: B")
elif (marks<80 and marks>=70):
    print("Grade: C")
elif (marks<70 and marks>=30):
    print("Grade: D")
else:
    print("Failed")