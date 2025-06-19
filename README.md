# CodeAlpha Task: Stock Portfolio Tracker

## Project Overview  
Stock Portfolio Tracker is a simple and practical command-line Python application designed especially for beginner programmers. The main objective is to help users track their stock investments by entering stock names and quantities, and calculating the total portfolio value based on predefined prices.

---

## Concept  

A set of predefined stocks and their current prices are stored in a Python dictionary, such as:  
"RELIANCE", "TCS", "INFY", "HDFC", "ITC", "HCL", "WIPRO" and more.

Users are prompted to input:
- Valid stock name → the program calculates `price × quantity`
- Invalid stock name → a warning is shown and input is ignored

After typing "done", the program displays:
- A summary of each stock (name, quantity, value)
- The total portfolio value

This simulates a simple stock tracker for educational purposes and introduces core concepts of data collection and processing.

---

## Extended Features

- Modular structure using a `portfolio_tracker()` function
- Track multiple stocks per session
- Loop to allow dynamic input
- Total value calculation
- Optional replay of the tracker after each session

---

## Python Concepts Used

- Loops (`while`, `for`)  
- Functions and modular code (`def`)  
- Dictionaries and list operations  
- Conditional statements (`if`, `else`)  
- User input and output handling  
- String formatting and numeric operations  

---

## Customization Ideas

- Add more stocks to the dictionary  
- Integrate real-time stock prices using APIs (e.g., NSE, Yahoo Finance)  
- Track portfolio history across sessions  
- Add profit/loss calculations and performance charts  
- Build a GUI with Tkinter or a web app using Flask  

---

## Ideal For

- Beginner Python developers  
- Students learning data structures and logic  
- Finance and commerce students exploring automation  
- Anyone interested in a real-world finance project

---

## Sample Output

```bash
Enter stock name and quantity (type 'done' to finish):
Stock: RELIANCE
Quantity: 3
Stock: TCS
Quantity: 2
Stock: done

Portfolio Summary:
- RELIANCE (₹3050 × 3) = ₹9150
- TCS (₹3800 × 2) = ₹7600

Total Portfolio Value: ₹16,750
