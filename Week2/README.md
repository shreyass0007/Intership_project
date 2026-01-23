# Grade Calculator Program

## 📋 Project Overview
A student grade calculator program that takes student marks (0-100) and returns corresponding grades (A, B, C, D, F) along with encouraging messages for each performance level.

## 🎯 Features
- **Input Validation**: Only accepts marks between 0-100
- **Grading System**: Converts numeric marks to letter grades
- **Encouraging Messages**: Personalized motivational messages for each grade
- **Error Handling**: Continuously prompts for valid input if user enters invalid marks
- **Student Tracking**: Records student name along with results

## 🛠️ Technical Requirements ✓

### 1. If-Elif-Else Statements
The program uses conditional logic to determine grades:
- **A**: 90-100 - Excellent work!
- **B**: 80-89 - Very good job! Keep it up!
- **C**: 70-79 - Good effort, but there's room for improvement
- **D**: 60-69 - You passed, but consider studying harder
- **F**: Below 60 - Unfortunately, you did not pass. Don't be discouraged, keep trying!

### 2. Input Validation
- Validates that marks are between 0 and 100 (inclusive)
- Rejects any marks outside this range
- Provides clear error messages for invalid input

### 3. Functions
The program includes three main functions:

#### `get_grade(marks)`
- Determines the letter grade based on marks
- Uses if-elif-else logic
- Returns the appropriate grade (A, B, C, D, or F)

#### `encorage_msg(grade)`
- Returns an encouraging message for each grade
- Provides motivation tailored to performance level
- Helps students feel supported regardless of their grade

#### `get_valid_marks()`
- Handles user input validation
- Uses a **while loop** to continuously prompt until valid input is received
- Ensures marks are between 0-100
- Returns valid marks once confirmed

#### `main()`
- Orchestrates the program flow
- Gets student name
- Calls validation function for marks
- Calculates grade
- Retrieves encouraging message
- Displays comprehensive results

### 4. While Loop for Invalid Inputs
The `get_valid_marks()` function uses a while loop to handle invalid inputs:
```python
while True:
    marks = int(input("Enter marks(0-100):"))
    if marks >= 0 and marks <= 100:
        return marks
    else:
        print("Invalid marks! Please enter marks between 0 and 100.")
```

## 🚀 How to Run
```bash
python grade_calculator.py
```

### Example Interaction
```
Welcome to the Grade Calculator!
Enter Student name: John
Enter marks(0-100): 150
Invalid marks! Please enter marks between 0 and 100.
Enter marks(0-100): 95

Result For John:
Marks: 95
Grade: A
Message: Excellent work!
```

## 📊 Grade Boundaries
| Grade | Marks | Message |
|-------|-------|---------|
| A | 90-100 | Excellent work! |
| B | 80-89 | Very good job! Keep it up! |
| C | 70-79 | Good effort, but there's room for improvement |
| D | 60-69 | You passed, but consider studying harder |
| F | 0-59 | Unfortunately, you did not pass. Don't be discouraged, keep trying! |

## 💡 Key Learning Points
- ✅ Function definition and calling
- ✅ Conditional statements (if-elif-else)
- ✅ Input validation techniques
- ✅ While loops for repeated operations
- ✅ String formatting for output
- ✅ Program flow control

## 📝 Notes
- All input validation errors prompt the user to try again
- The program continues until a valid mark is entered
- Each grade level has an appropriate encouraging message to motivate students
- The program successfully handles edge cases (0 and 100)

## 🔄 Possible Enhancements
- Add multiple student processing in a single session
- Store grades in a file for record keeping
- Calculate class average statistics
- Add weighted grading for different assignment types
- Create a GUI version of the program
