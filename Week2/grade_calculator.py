def get_grade(marks):

    if(marks>=90 and marks<=100):
        grade='A'
    elif(marks>=80 and marks<90):
        grade='B'
    elif(marks>=70 and marks<80):
        grade='C'
    elif(marks>=60 and marks<70):
        grade='D'
    else:
        grade='F'
    return grade

def encorage_msg(grade):
    if(grade=='A'):
        return ("Excellent work!")
    elif(grade=='B'):
        return ("Very good job!keep it up!")
    elif(grade=='C'):
        return ("Good effort, but there's room for improvement.")
    elif(grade=='D'):
        return ("You passed, but consider studying harder.")
    else:
        return ("Unfortunately, you did not pass. Don't be discouraged, keep trying!")

def get_valid_marks():
    while True:
        marks=int(input("Enter marks(0-100):"))
        if(marks>=0 and marks<=100):
            return marks
        else:
            print("Invalid marks! Please enter marks between 0 and 100.")
        

def main():
    print("Welcome to the Grade Calculator!")
    name=input("Enter Student name:")
    marks=get_valid_marks()
    grade=get_grade(marks)
    message=encorage_msg(grade)
    
    print(f"Result For {name}:")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")
    print(f"Message: {message}")

main()