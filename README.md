# 🍽️ Smart Canteen Discount System

A beginner-friendly Python project that demonstrates the use of **conditional statements (`if`, `elif`, and `else`)**, comparison operators, user input, and basic arithmetic through a real-world college canteen discount management scenario.

## 📌 Project Overview

The Smart Canteen Discount System is a console-based Python application designed to calculate student discounts based on their total bill amount and membership status.

In a college canteen, students may receive different discounts depending on how much they spend. Students with a membership card receive an additional 5% discount.

This project automates the discount calculation process and displays a complete bill summary, including the original bill, discount rate, discount amount, and final payable amount.

## 🎯 Project Objectives

The main objectives of this project are to:

- Understand and implement Python conditional statements.
- Practice `if`, `elif`, and `else` structures.
- Learn how to use comparison operators.
- Take input from users using the `input()` function.
- Perform mathematical calculations using arithmetic operators.
- Apply logical thinking to solve real-world problems.
- Understand nested conditional statements.
- Validate user input and handle invalid bill amounts.
- Display formatted output using Python f-strings.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Programming language |
| VS Code | Code editor |
| Terminal / PowerShell | Program execution |
| Git & GitHub | Version control and project hosting |

## 📋 Discount Policy

The canteen follows the following discount structure:

| Total Bill Amount | Discount Rate |
|---|---:|
| Rs. 3,000 or above | 20% |
| Rs. 2,000 – Rs. 2,999.99 | 10% |
| Rs. 1,000 – Rs. 1,999.99 | 5% |
| Below Rs. 1,000 | 0% |

**Additional Membership Benefit:**

Students who have a membership card receive an additional **5% discount** on their applicable discount rate.

For example:
- Bill amount: Rs. 3,000
- Regular discount: 20%
- Membership discount: 5%
- Total discount rate: 25%

## ⚙️ Program Features

### 1. User Input
The program asks students to enter their total bill amount.

### 2. Bill Validation
The program checks whether the entered bill amount is valid.

- If the bill amount is zero or negative, an invalid bill message is displayed.
- If the bill amount is positive, the program continues with discount calculations.

### 3. Automatic Discount Calculation
The program uses `if`, `elif`, and `else` statements to determine the applicable discount based on the total bill amount.

### 4. Membership Discount
The program asks whether the student has a membership card.

- If the answer is `yes`, an additional 5% discount is applied.
- If the answer is `no`, only the regular discount is applied.

### 5. Bill Summary
The program displays:

- Original Bill Amount
- Total Discount Rate
- Discount Amount
- Final Payable Amount

### 6. Savings Message
If a discount is applied, the program displays a congratulatory message showing how much the student saved.

## 🧠 Python Concepts Covered

This project covers the following Python programming concepts:

| Concept | Implementation |
|---|---|
| `print()` | Displaying program messages |
| `input()` | Taking user input |
| `float()` | Converting bill input into a decimal number |
| `if` | Checking the first condition |
| `elif` | Checking multiple discount conditions |
| `else` | Handling the remaining conditions |
| Nested if-else | Validating bills and processing discounts |
| Comparison operators | `>=`, `<=`, `>` |
| Arithmetic operators | `+`, `-`, `*`, `/` |
| `.lower()` | Converting membership input to lowercase |
| F-strings | Formatting bill summary output |
| `.2f` | Displaying amounts up to two decimal places |

## 🔄 Program Workflow

1. Start the program.
2. Display the Smart Canteen welcome message.
3. Ask the student to enter the bill amount.
4. Check whether the bill amount is valid.
5. If the bill is invalid, display an error message.
6. Otherwise, calculate the discount according to the bill amount.
7. Ask whether the student has a membership card.
8. Apply an additional 5% discount if applicable.
9. Calculate the discount amount.
10. Calculate the final payable amount.
11. Display the complete bill summary.
12. Display the savings message if a discount is applied.
13. End the program.

## 💻 How to Run the Project

### Prerequisites

Make sure Python 3 is installed on your computer.

Check your Python installation:

```bash
python --version
```

### Step 1: Clone the Repository

```bash
git clone <your-repository-url>
```

### Step 2: Navigate to the Project Folder

```bash
cd smart-canteen
```

### Step 3: Run the Python Program

```bash
python canteen.py
```

## 📸 Sample Program Output

### Example 1: Student with Membership Card

```text
===== SMART CANTEEN =====
Enter your total bill amount (Rs.): 3000
Do you have a membership card? (yes/no): yes

===== BILL SUMMARY =====
Original Bill: Rs. 3000.00
Discount Rate: 25%
Discount Amount: Rs. 750.00
Final Payable: Rs. 2250.00

Congratulations! You saved Rs. 750.00
```

### Example 2: Student Without Membership Card

```text
===== SMART CANTEEN =====
Enter your total bill amount (Rs.): 1500
Do you have a membership card? (yes/no): no

===== BILL SUMMARY =====
Original Bill: Rs. 1500.00
Discount Rate: 5%
Discount Amount: Rs. 75.00
Final Payable: Rs. 1425.00

Congratulations! You saved Rs. 75.00
```

### Example 3: Invalid Bill Amount

```text
===== SMART CANTEEN =====
Enter your total bill amount (Rs.): 0

Invalid bill amount. Please enter a positive value.
```

## 📝 Student Practice Challenges

Students can extend this project by implementing the following features:

1. Add input validation to handle non-numeric bill amounts.
2. Restrict membership input to only `yes` or `no`.
3. Introduce a maximum discount limit.
4. Add a student name and display it in the bill summary.
5. Add a loyalty points system for regular customers.
6. Allow students to process multiple bills using loops.

## 🎓 Learning Outcomes

After completing this project, students should be able to:

- Write Python programs using conditional statements.
- Make decisions using comparison operators.
- Understand the difference between `if`, `elif`, and `else`.
- Implement nested conditional logic.
- Validate input before performing calculations.
- Solve simple real-world problems using Python.
- Generate formatted output using f-strings.

## 📚 Educational Context

**Program:** PSEB Bootcamp  
**Week:** Week 01 – Python Basics  
**Topic:** Conditional Statements  
**Project:** Program 01 – Smart Canteen Discount System  
**Difficulty Level:** Beginner  
**Language:** Python 3

## 👨‍💻 Author

Developed as part of the PSEB Bootcamp – Python Basics curriculum to practice fundamental programming concepts through a practical, real-world application.

---

⭐ **If you find this project helpful, consider giving the repository a star!**

**Happy Coding! 🐍**
