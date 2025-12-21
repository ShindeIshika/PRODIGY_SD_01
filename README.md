Temperature Converter
Overview

The Temperature Converter is a graphical desktop application designed to convert temperature values between Celsius and Fahrenheit.
It provides a clean, modern, and user-friendly interface that allows users to perform conversions quickly without using the command line.

Features

Simple and intuitive graphical user interface

Supports:

Celsius → Fahrenheit

Fahrenheit → Celsius

Dropdown-based conversion selection

Clearly formatted output with units

Input validation to prevent invalid entries

Technologies Used

Python – GUI implementation

Go (Golang) – temperature conversion logic

Standard libraries and GUI framework used in the project

Project Structure
Task_1/
├── assets/
│   └── demo_output.png
├── temperature_converter.go
├── main.py
└── README.md

Application Preview

The screenshot below shows the main interface of the Temperature Converter application:

How It Works

The user enters a temperature value in the input field.

A conversion type is selected from the dropdown menu.

The Convert button performs the calculation.

The converted temperature is displayed with the appropriate unit.

Conversion Formulas

Celsius to Fahrenheit:

F=(C×9/5)+32

Fahrenheit to Celsius:

C=(F−32)×5/9

Error Handling

The application ensures reliable behavior by:

Preventing non-numeric input

Requiring a valid conversion selection

Displaying results only when inputs are valid

Purpose

This project demonstrates:

GUI-based application development

Integration of backend logic with a user interface

Clean UI design and usability principles

Fundamental temperature conversion logic
