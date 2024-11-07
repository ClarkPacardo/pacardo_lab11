gradelist = []
passed = 0
i = 1
x = 0
input_grade = input(f"Enter Student Grade: {i} (Type done to finish): ")
while input_grade.lower() != 'done':
    if int(input_grade) >= 40 and int(input_grade) <= 100: 
        gradelist.append(int(input_grade))
        if int(input_grade) >= 75:
            passed+=1
    else:
        print("Invalid Input, Please enter a grade between 40 and 100.")
        x+=1
        break
    i+=1
    input_grade = input(f"Enter Student Grade: {i} (Type done to finish): ")
average = sum(gradelist) / len(gradelist)
percentage = (passed/len(gradelist))*100
print(f"Average Grade: {average: .2f}")
print(f"Number of Students Passed: {passed}")
print(f"Passing Percentage]: {int(percentage)}%")