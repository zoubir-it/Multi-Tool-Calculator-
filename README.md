Multi Tool Calculator 🧮

A comprehensive desktop calculator application built with Python and Tkinter.

It features a standard calculator with parentheses support, custom implementations of trigonometric functions (sin, cos, tan), and a wide range of converters and utilities.



✨ Features

🔢 Calculator

Basic arithmetic operations (+, -, \*, /, ^) with parentheses handling.



Trigonometric functions (sin, cos, tan) – implemented with custom algorithms (Taylor series expansion, not relying on built‑in math functions).



Square root (√) operation.



Interactive GUI with button grid and expression entry.



🔄 Converters

Currency – 14 currencies with predefined exchange rates.



<<<<<<< HEAD
Length – 8 units (meter, kilometer, mile, foot, inch, etc.).



Mass – 8 units (gram, kilogram, pound, ounce, etc.).

=======
· Length (meter, km, mile, etc...).

· Mass (kg, g, lb, etc...).

· Speed (km/h, m/s, mph...).

· Area (m², km², acre, etc...).

· Date counter (years, months, days between two dates).
>>>>>>> 49f3bb2fcfa25c60f1c0cc1c27615b608e927677


Speed – 8 units (m/s, km/h, mph, knot, etc.).



Area – 11 units (square meter, hectare, acre, square foot, etc.).



Date counter – calculates days, months, and years between a given date and today.



Discount calculator – computes final price and savings.



BMI calculator – body mass index with gender/age adjustment and ideal weight range.



🖥️ User Interface

Clean and intuitive Tkinter GUI.



Easy navigation between calculator and converter menus.



Real‑time result display.



📋 Requirements

Python 3.x



Tkinter (usually included with Python)



No external libraries required – all functionality is built with Python standard libraries.



🚀 How to Run

Clone the repository or download the source.



Navigate to the project folder.



Run the main script:



bash

python multi\_tool\_calculator.py

The GUI will open – choose Calculator or Converter from the main menu.



📁 Project Structure

text

Multi-Tool-Calculator/

├── multi\_tool\_calculator.py   # main application script

└── README.md                  # this file

🛠️ Custom Trigonometry Implementation

The sine, cosine, and tangent functions are implemented from scratch using Taylor series expansion:



sin(x) = x − x³/3! + x⁵/5! − x⁷/7! + ...



cos(x) = 1 − x²/2! + x⁴/4! − x⁶/6! + ...



tan(x) = sin(x)/cos(x)



This demonstrates an understanding of numerical methods and makes the project particularly interesting for learning purposes.



📊 Converter Details

Currency Exchange Rates (Sample)

Code	Name	Rate (vs USD)

USD	US Dollar	1.00

EUR	Euro	0.92

GBP	British Pound	0.79

MAD	Moroccan Dirham	9.90

...	and 10 more	...

Length Units

Meter (m), Kilometer (km), Centimeter (cm), Millimeter (mm), Mile (mi), Yard (yd), Foot (ft), Inch (in).



Mass Units

Milligram (mg), Gram (g), Kilogram (kg), Tonne (t), Ounce (oz), Pound (lb), Stone (st).



Speed Units

m/s, km/h, mph, ft/s, knot, m/min, km/min, km/s.



Area Units

m², km², cm², mm², hectare (ha), are (a), ft², yd², in², mi², acre.



🧮 BMI Calculator Features

Takes gender, age, height (cm), and weight (kg) as input.



Calculates BMI and displays status: Underweight ⚠️, Normal ✅, Overweight ⚠️, Obese 🚨.



Adjusts ideal weight range based on age and gender factors.



Shows healthy weight range for the given height.



⚠️ Important Notes

Trigonometric functions accept radians as input.



The calculator supports complex expressions with parentheses (e.g., 2\*(3+4)).



Date format must be dd/mm/yyyy (slashes, dashes, or underscores are accepted).



BMI calculation is not recommended for individuals under 15 years old.





📄 License

This project is open source and available under the MIT License.



🙏 Acknowledgements

Built with Python's standard library – tkinter, datetime, functools.



Inspired by the need for a simple, all‑in‑one desktop utility.

