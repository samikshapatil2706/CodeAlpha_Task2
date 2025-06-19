📊 CodeAlpha Task: Stock Portfolio Tracker
Project Overview
Stock Portfolio Tracker is a simple and practical command-line Python application designed especially for beginner programmers. The main objective is to allow users to track their stock investments by entering stock names and quantities, and calculating the total portfolio value based on fixed prices.

Game Concept
A set of predefined stocks and their current prices are stored in a Python dictionary:
"RELIANCE", "TCS", "INFY", "HDFC", "ITC", "HCL", "WIPRO", and more.

The user is prompted to input stock names and quantities:

If the stock is valid, its total value is calculated (price × quantity).

If the stock is invalid, a warning is shown and input is ignored.

Once the user types "done", the program displays:

A summary of each stock with quantity and total value

The total portfolio value

This program simulates a personal stock-tracking tool, useful for beginners to understand data collection and calculation with real-world examples.

Extended Features
This version includes a modular structure using a portfolio_tracker() function, which allows:

Tracking multiple stocks in a session

Looping to handle dynamic stock entries

Summing up total portfolio value at the end

Optionally prompting the user to track again in a new session

Python Concepts Used
This project helps reinforce important Python programming concepts:

Loops (while, for)

Functions and modular code (def)

Dictionaries and list operations

User input and output handling

Conditional statements (if, else)

String formatting and numeric operations

Customization
You can easily extend or customize this tracker:

Add more stocks and prices to the dictionary

Integrate real-time stock prices using APIs (like NSE/BSE or Yahoo Finance)

Include date-wise or session-based tracking

Add features like profit/loss calculation, percentage gains, or chart visualization

Build a GUI or web interface using tools like Tkinter or Flask

Ideal For
Beginner Python programmers

Students learning dictionaries, input handling, and basic logic

Finance and commerce students exploring tech integration

Anyone wanting to build a useful, real-world Python project
