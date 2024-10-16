# The purpose of this program is to calculate the grade of a class once inputted with the number of grades,
# the grade received, and the weight of the grade


# Initialize the variables

total_grades = int(input('How many grades do you want?:'))
count = 0
total_weight = 0

# Establish a while loop that runs as long as count is less than the number of total grades

while count < total_grades:
    print(f'Assignment {count + 1}')
    user_grade = float(input('Enter a grade for this assignment (0-100):'))
    grade_weight = float(input('Enter a weight for this assignment:'))
    count += 1
    # Update the total weight of all the weights entered
    total_weight += grade_weight

# If total weight is 100, output the final grade rounded to two decimal points
# Otherwise inform user that the total weight isn't 100%

if total_weight == 100:
    final_grade = round(user_grade * (total_weight / 100), 2)
    print('Your final grade is %', final_grade)
else:
    print("The total weight isn't 100%, Please try again!")
