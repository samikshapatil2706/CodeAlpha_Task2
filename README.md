# CodeAlpha_Task2
CodeAlpha Task: Stock Portfolio Tracker
Project Overview
The Stock Portfolio Tracker is a simple yet practical Python-based command-line application designed for beginner programmers. It helps users manage and monitor their stock investments by allowing them to input stock names, quantities, and automatically calculate the total portfolio value based on current prices.

Project Concept
Users can enter the stock name and the quantity they hold.

The program uses a predefined dictionary of stock prices (e.g., RELIANCE: ₹3050) to compute the value of each stock in the portfolio.

At the end of the input, it displays:

A summary of all stocks entered

The total value of the portfolio

Optionally, individual stock-wise valuations

Core Features
Predefined stock list with current hardcoded prices

Input-driven collection of stock quantities

Automatic calculation of:

Individual stock values

Total portfolio worth

Graceful handling of invalid stock names

Option to run multiple sessions or update stocks dynamically

Extended Features
This version is modularized using a portfolio_tracker() function and includes:

Looping structure for tracking multiple stocks in a session

Handling of "done" keyword to stop input

Clean, organized display of results

Easy-to-update stock price dictionary

Python Concepts Used
This project helps reinforce essential Python programming skills such as:

Loops (while, for)

Functions and modular programming

Dictionaries and list manipulation

String handling and formatting

User input/output

Conditional logic (if, else)

Customization
You can easily extend or modify the tracker to:

Fetch real-time stock prices using APIs (e.g., from NSE/BSE)

Add date-wise tracking or portfolio history

Generate PDF reports or graphs

Include profit/loss calculations over time

Build a GUI version using Tkinter or a web version with Flask

Ideal For
Beginner Python programmers

Students learning real-life application development

Anyone interested in financial programming

Hobbyists wanting a personal finance tool
