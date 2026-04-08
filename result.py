print("MarkSheet")
a=75
b=100
c=100
maths= int(input("enter the marks of maths (out of 75): "))
urdu= int(input("enter the marks of urdu (out of 100): "))
english= int(input("enter the marks of english (out of 100): "))
total=a+b+c
obtained=maths+urdu+english
percentage=(obtained/total)*100
print("Total Marks:",total)
print("Obtained Marks:",obtained)
print("Percentage:",percentage)
if percentage >= 80:
    print("Grade: A-one.")
    print("EXCELLENT.")
elif percentage >= 70:
    print("Grade: A.")
    print("GOOD.")
elif percentage >= 60:
    print("Grade: B.")
    print("You Need to Improve.")
else:
    print("Grade: Fail.")
    print("SORRY.")