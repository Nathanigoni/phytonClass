def assign_grade(score):
    if not 0 <= score <= 100:
        return 'Invalid score. Must be between 0 and 100.'
    return 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'D' if score >= 60 else 'F'

user_input = input("Enter your score: ")

if user_input.replace('.', '', 1).isdigit():
    score = float(user_input)
    print("Your grade is:", assign_grade(score))
else:
    print("Invalid input. Please enter a number.")
