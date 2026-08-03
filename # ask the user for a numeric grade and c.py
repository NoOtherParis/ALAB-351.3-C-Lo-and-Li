# ask the user for a numeric grade and convert it to a float
score = float(input("Enter your numeric grade (0-100): "))

# Determine the letter grade using an if-elif-else structure
if score>= 90 and score<= 100:
    letter_grade = "A"
elif score >= 80:
    letter_grade = "B"
elif score >= 70:
    letter_grade = "C"
elif score >= 60:
    letter_grade = "D"
else:
    letter_grade = "F"
    
# Print the letter grade result
print(f"Your grade is: {letter_grade}")

# Use a conditional expression for the final message
# Passing grades are A, B, or C
message= "Congratulations on passing!" if letter_grade in ["A", "B", "C,"] else "Keep pushing, and try again!"
print(message) 
      
      
        