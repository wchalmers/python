#Grades Program
Course=int(input("Please enter your course mark here"))
Exam=int(input("Please enter your exam mark here"))
Total=Course+Exam
Percentage=(Total/150)*100


if Percentage >=70 and Percentage <101:
    print("Well Done you passed with an A!and your percentage was", Percentage)
elif Percentage >=69 and Percentage <70:
    print("Well Done you passed with a B! and your percentage was", Percentage)
elif Percentage >=59 and Percentage <69:
    print("Well Done you passed with a C! and your percentage was", Percentage)
elif Percentage >=49 and Percentage <69:
    print("Well Done you passed with a D! and your percentage was", Percentage)
else:
    print("Sorry you failed the course")
    
    
