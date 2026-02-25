from datetime import datetime

import string 

from functools import partial

from tkinter import messagebox

from tkinter import *
root = Tk()
root.title("Multu Tool Calculator")
root.geometry("400x600+900+200")
root.resizable(0,0)
header_frame =Frame(root)
header_frame.pack()

main_frame = Frame(root)
main_frame.pack(fill="both", expand=True)

def clear_frame():
    for widget in main_frame.winfo_children():
        widget.destroy()



    

currencies = {
    "USD": {"name": "US Dollar", "rate": 1.0},
    "EUR": {"name": "Euro", "rate": 0.92},
    "GBP": {"name": "British Pound", "rate": 0.79},
    "JPY": {"name": "Japanese Yen", "rate": 146.5},
    "CAD": {"name": "Canadian Dollar", "rate": 1.35},
    "AUD": {"name": "Australian Dollar", "rate": 1.52},
    "CHF": {"name": "Swiss Franc", "rate": 0.88},
    "CNY": {"name": "Chinese Yuan", "rate": 7.15},
    "INR": {"name": "Indian Rupee", "rate": 83.0},
    "SAR": {"name": "Saudi Riyal", "rate": 3.75},
    "AED": {"name": "UAE Dirham", "rate": 3.67},
    "MAD": {"name": "Moroccan Dirham", "rate": 9.90},
    "EGP": {"name": "Egyptian Pound", "rate": 30.9},
    "TRY": {"name": "Turkish Lira", "rate": 30.2}
}


length_units = {
    "m":  {"name": "Meter",        "rate": 1.0},
    "km": {"name": "Kilometer",    "rate": 1000.0},
    "cm": {"name": "Centimeter",   "rate": 0.01},
    "mm": {"name": "Millimeter",   "rate": 0.001},
    "mi": {"name": "Mile",         "rate": 1609.34},
    "yd": {"name": "Yard",         "rate": 0.9144},
    "ft": {"name": "Foot",         "rate": 0.3048},
    "in": {"name": "Inch",         "rate": 0.0254}
}

mass_units = {
    "mg": {"name": "Milligram", "rate": 0.000001},
    "g":  {"name": "Gram",      "rate": 0.001},
    "kg": {"name": "Kilogram",  "rate": 1.0},
    "t":  {"name": "Tonne",     "rate": 1000.0},

    "oz": {"name": "Ounce",     "rate": 0.0283495},
    "lb": {"name": "Pound",     "rate": 0.453592},
    "st": {"name": "Stone",     "rate": 6.35029}
}


speed_units = {
    "m/s":   {"name": "Meters per second",        "rate": 1.0},
    "km/h":  {"name": "Kilometers per hour",      "rate": 0.277778},
    "mph":   {"name": "Miles per hour",           "rate": 0.44704},
    "ft/s":  {"name": "Feet per second",          "rate": 0.3048},
    "kn":    {"name": "Knot",                     "rate": 0.514444},

    "m/min": {"name": "Meters per minute",        "rate": 1 / 60},
    "km/min":{"name": "Kilometers per minute",    "rate": 1000 / 60},
    "km/s":  {"name": "Kilometers per second",    "rate": 1000.0}
}

area_units = {
    "m2":   {"name": "Square meter",      "rate": 1.0},
    "km2":  {"name": "Square kilometer",  "rate": 1_000_000.0},
    "cm2":  {"name": "Square centimeter", "rate": 0.0001},
    "mm2":  {"name": "Square millimeter", "rate": 0.000001},

    "ha":   {"name": "Hectare",            "rate": 10_000.0},
    "a":    {"name": "Are",                "rate": 100.0},

    "ft2":  {"name": "Square foot",        "rate": 0.092903},
    "yd2":  {"name": "Square yard",        "rate": 0.836127},
    "in2":  {"name": "Square inch",        "rate": 0.00064516},

    "mi2":  {"name": "Square mile",        "rate": 2_589_988.11},
    "acre": {"name": "Acre",               "rate": 4046.8564224}
}



# ===================== UTILITIES =====================

def header(title):
    print("\n" + "=" * 50)
    print(f"{title:^50}")
    print("=" * 50)

def line():
    print("-" * 50)


# ===================== CALCULATOR =====================

# -------------------------------
# Check for parentheses correctness
# -------------------------------
def handle_parentheses(expression):
    #expression = input("Enter your operation: ")
    operations_list = ["+", "-", "/", "*", "r", "^"] 
    parentheses = []
    parentheses_stack = False
    # Check for ending parenthesis or unmatched parentheses
    if expression.endswith("("):
        print("Syntax error: expression cannot end with '('")
        return
    if expression.count("(") != expression.count(")"):
        print("Syntax error: unmatched parentheses")
        return 

    for par in expression:
        if par == "(":
            parentheses_stack = False
            parentheses.append(par)
        elif par in string.digits:
            parentheses_stack = True
        elif par == ")":
            if not parentheses or not parentheses_stack:
                print("Syntax error: empty or unmatched parentheses")
                return 
            parentheses.pop()
    
    return expression


# -------------------------------
# Evaluate expressions inside parentheses
# -------------------------------
def evaluate_parentheses(expr):
    operations_list = ["+", "-", "/", "*", "r", "^"] 
    expr = handle_parentheses(expr)
    if expr is None:
        print("Syntax error")
        return 
    
    # Process inner parentheses firstoperations_list = ["+", "-", "÷", "×", "√", "^"]
    while '(' in expr:
        open_index = expr.rfind("(")  # Find last open parenthesis
        close_index = open_index + 1 + expr[open_index + 1:].find(")")  # Find first close parenthesis after it 

        if open_index >= 3 and expr[open_index -3: open_index] == 'cos':
            i = open_index - 4
            side_out = []
            while i >= 0 and (expr[i].isdigit() or expr[i] == '.'):  
                side_out.append(expr[i])
                i-=1
            
            start_index = i +1
            side_out = side_out[::-1]
            outside = ''.join(side_out) if side_out else '1'
            

            inside = expr[open_index + 1: close_index]
            x = calculator(inside)
            x = float(x)
            cos_rad = cos_radians(x)
            expr = expr[:start_index] + outside + "*" + str(cos_rad) + expr[close_index + 1:]
        elif open_index >= 3 and expr[open_index -3: open_index] == 'sin':
            i = open_index - 4
            side_out = []
            while i >= 0 and (expr[i].isdigit() or expr[i] == '.'):  
                side_out.append(expr[i])
                i-=1
            
            start_index = i +1
            side_out = side_out[::-1]
            outside = ''.join(side_out) if side_out else '1'
            

            inside = expr[open_index + 1: close_index]
            x = calculator(inside)
            x = float(x)
            sin_rad = sin_radians(x)
            expr = expr[:start_index] + outside + "*" + str(sin_rad) + expr[close_index + 1:]
            
        
        elif open_index >= 3 and expr[open_index -3: open_index] == 'tan':
            i = open_index - 4
            side_out = []
            while i >= 0 and (expr[i].isdigit() or expr[i] == '.'):  
                side_out.append(expr[i])
                i-=1
            
            start_index = i +1
            side_out = side_out[::-1]
            outside = ''.join(side_out) if side_out else '1'
            

            inside = expr[open_index + 1: close_index]
            x = calculator(inside)
            x = float(x)
            tan_rad = tan_radians(x)
            expr = expr[:start_index] + outside + "*" + str(tan_rad) + expr[close_index + 1:]
        
        else:
            sub_expr = expr[open_index + 1: close_index]

            # Calculate inner expression and replace it with result
            result = calculator(sub_expr)
            expr = expr[:open_index] + str(result) + expr[close_index + 1:]
    
    # Calculate remaining expression after removing all parentheses
    result = calculator(expr)
    result = float(result)
    result = int(result) if result.is_integer() else float(result)

    
    return result
# -------------------------------
# Main calculator function
# -------------------------------
def calculator(operations):
    tokens = []
    current_number = ""
    operations_list = ["+", "-", "/", "*", "r", "^"]

    # -------------------------------
    # Convert expression into tokens
    # -------------------------------
    for char in operations:
        if char.isspace():
            continue
        elif char in string.digits or char == ".":
            if "." in current_number and char == ".":
                return "Syntax error: invalid number format"
            
            current_number += char
        elif char in operations_list:
            if not tokens and not current_number and char == "-":
                tokens.append('0')  # Support negative numbers at the start
            elif char == "r" and (not current_number and (not tokens or tokens[-1] in operations_list)):
                tokens.append("1")  # √ without previous number is treated as 1
            elif not current_number and char in ["+", "*", "/", "^"]:
                return "Syntax error: operator without operand"
         
            
            if tokens and tokens[-1] in operations_list and current_number == "":
                print("Syntax error: two consecutive operators") 
                return

            if current_number:
                tokens.append(current_number)
                current_number = ""
            tokens.append(char)
        else:
            print(f"Syntax error: invalid character '{char}'")
            return 

    if current_number:
        tokens.append(current_number)
    if tokens[-1] in operations_list:
        print("Syntax error: expression cannot end with an operator")
        return 
        
    # -------------------------------
    # Priority operations: × ÷ ^ √
    # -------------------------------
    op_list = ["*", "/", "^", "r"]
    while len(tokens) > 1:
        for i in range(len(tokens)):
            if tokens[i] in op_list:
                n1 = float(tokens[i-1])
                n2 = float(tokens[i+1])  
                op = tokens[i]

                if op == "*":
                    result = n1 * n2
                elif op == "/":
                    if n2 == 0:
                        print("Error: division by zero")
                        return 
                    result = n1 / n2
                elif op == "^":
                    result = n1 ** n2
                elif op == "r":
                    result = n1 * n2 ** 0.5

                # Replace operation and operands with result
                tokens[i-1: i+2] = [str(result)]
                break
        else:
            break 

    # -------------------------------
    # Lower priority operations: + -
    # -------------------------------
    while len(tokens) > 1:
        n1 = float(tokens[0])
        n2 = float(tokens[2])
        op = tokens[1]
        if op == "+":
            result = n1 + n2
        elif op == "-":
            result = n1 - n2
        tokens[0:3] = [str(result)]
            
    return tokens[0]  



#====== function for calculate cos radians =======
def cos_radians(x):
    
    counter = 0
    power = 2
    factorial = 2
    sing = -1
    cos_sum = 1
   
    while counter < 15:
        term = sing * x ** power / factorial
        cos_sum += term
        
        counter += 1
        power += 2
        factorial *= (power - 1) * power
        sing *= -1
        
    return cos_sum


#====== function for calculate sin radians =======
def sin_radians(x):
    
    counter = 0
    power = 3
    factorial = 6
    sing = -1
    sin_sum = x
    while counter < 15:
        term = sing * x **power / factorial
        sin_sum += term
        counter += 1
        power += 2
        factorial *= (power-1) * power
        sing *= -1
    
    return sin_sum

#====== function for calculate tan radians =======
def tan_radians(x):

    sin_value = sin_radians(x)
    cos_value = cos_radians(x)
    return sin_value / cos_value


def open_menu():
    #label = Label(header_frame, text="Welcome to Multu Tool Calculator!", font=("arial",15))
    #label.pack(pady=20)
    clear_frame()
    title = Label(main_frame, text="Multu Tool Calculator", font=("Arial", 20))
    title.pack(pady=20)
    
    calc_button = Button(
        main_frame,
        text="Calculator",
        font=("arial", 11, "bold"),
        background="red",
        foreground="white",
        height=1,
        width=10,
        command=open_calculator
        )
    calc_button.pack(pady=15)
    conver_button = Button(
        main_frame,
        text="Converter",
        font=("arial", 11, "bold"),
        background="red",
        foreground="white",
        height=1,
        width=10,
        command=open_converter_menu
        )
    conver_button.pack(pady=15)
    
    exit_button = Button(main_frame, text="   Exit  ", font=("arial", 11, "bold"), background="red", foreground="white", height=1, width=10, command=root.destroy)
    exit_button.pack(pady=15)


def open_calculator():
    clear_frame()
    entry = Entry(main_frame, font=("arial", 18), justify='right')
    entry.pack(pady=20)

    buttons_frame = Frame(main_frame)
    buttons_frame.pack()

    
    
    buttons = [
    "C", "(", ")", "√", "cos(", "tan(", "sin(", "^",
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    ".", "0", "=", "+"
    ]

    
    def add_to_entry(entry_widget, value):
        entry_widget.insert(END, value)

    def clear_entry(entry_widget):
        entry_widget.delete(0, END)

    def calculate_result(entry_widget):
        expr = entry_widget.get()
        result = evaluate_parentheses(expr)
        entry_widget.delete(0, END)
        entry_widget.insert(END, result)
    


    i = 0
    num_culmns = 4
    while i < len(buttons):
        row = i // num_culmns
        column = i % num_culmns
        if buttons[i] == "=":
            cmd = partial(calculate_result, entry)
        elif buttons[i] == "C":
            cmd = partial(clear_entry, entry)
        else:
            cmd = partial(add_to_entry, entry, buttons[i])
        btn = Button(buttons_frame, text=buttons[i], width = 5, height=2, command=cmd)
        btn.grid(row=row, column=column, padx=5, pady=5)
        i +=1
        
    back_buttons = Button(buttons_frame, text="Back", width=7, height=2, background="red", foreground="white", command=open_menu)
    back_buttons.grid(row=6, column=3, columnspan=10, pady=5)



#=======================Converter Menu========================
def open_converter_menu():
    clear_frame()

    title = Label(main_frame, text="Converter Menu", font=("Arial", 20))
    title.pack(pady=20)


    Button(main_frame, text="Currency 💵", width=9, height=1, background="red", foreground="white", command=open_currency_converter).pack(pady=5)
    Button(main_frame, text="Length 📏", width=9, height=1, background="red", foreground="white", command=open_length_converter).pack(pady=5)
    Button(main_frame, text="Mass ⚖️", width=9, height=1, background="red", foreground="white", command=open_mass_converter).pack(pady=5)
    Button(main_frame, text="Date 📅", width=9, height=1, background="red", foreground="white", command=open_date_counter).pack(pady=5)
    Button(main_frame, text="Speed 🚀", width=9, height=1, background="red", foreground="white", command=open_speed_converter).pack(pady=5)
    Button(main_frame, text="Discount 🏷️", width=9, height=1, background="red", foreground="white", command=open_discount_calculator).pack(pady=5)
    Button(main_frame, text="Area 📐", width=9, height=1, background="red", foreground="white", command=open_area_converter).pack(pady=5)
    Button(main_frame, text="BMI ⚕️", width=9, height=1, background="red", foreground="white", command=open_bmi_calculator).pack(pady=5)

    Button(main_frame, text="Back 🔙", width=9, height=1, background="red", foreground="white", command=open_menu).pack(pady=20)

#========================Currency Converter========================
def open_currency_converter():
    clear_frame()

    title = Label(main_frame, text="Currency Converter", font=("arial", 20))
    title.pack(pady=10)
    input_frame = Frame(main_frame)
    input_frame.pack(pady=10)

    value_entry = Entry(input_frame, font=("arial", 16), width=10)
    value_entry.grid(row=0, column=0, padx=5, pady=5)

    from_unit_var = StringVar()
    from_unit_var.set(list(currencies.keys())[0])
    from_menu = OptionMenu(input_frame, from_unit_var, *currencies.keys())
    from_menu.grid(row=0, column=2, padx=5, pady=5)

    to_unit_var = StringVar()
    to_unit_var.set(list(currencies.keys())[0])
    to_menu = OptionMenu(input_frame, to_unit_var, *currencies.keys())
    to_menu.grid(row=1, column=2, padx=5, pady=5)

    result_label = Label(main_frame, text="", font=("arial", 16))
    result_label.pack(pady=10)

    def convert():
        try:
            value = float(value_entry.get())
            src = from_unit_var.get()
            tgt = to_unit_var.get()
            result = value * currencies[src]['rate'] / currencies[tgt]['rate']
            result = int(result) if result.is_integer() else round(result, 4)
            result_label.config(text=f"{value} {src} == {result} {tgt}")
        except ValueError:
            result_label.config(text="error, invalid number")
    
    convert_btn = Button(main_frame, text="convert", width=15, height=2, command=convert)
    convert_btn.pack(pady=20)
    back_btn = Button(main_frame, text="back", width=10, height=2, background="red", foreground="white", command=open_converter_menu)
    back_btn.pack(pady=20)

#========================Length Converter========================
def open_length_converter():
    clear_frame()
    
    title = Label(main_frame, text="Length Converter", font=("arial", 20))
    title.pack(pady=10)
    input_frame = Frame(main_frame)
    input_frame.pack(pady=10)

    value_entry = Entry(input_frame, font=("arial", 16), width=10)
    value_entry.grid(row=0, column=0, padx=5, pady=5)

    from_unit_var = StringVar()
    from_unit_var.set(list(length_units.keys())[0])
    from_menu = OptionMenu(input_frame, from_unit_var, *length_units.keys())
    from_menu.grid(row=0, column=2, padx=5, pady=5)

    to_unit_var = StringVar()
    to_unit_var.set(list(length_units.keys())[0])
    to_menu = OptionMenu(input_frame, to_unit_var, *length_units.keys())
    to_menu.grid(row=1, column=2, padx=5, pady=5)

    result_label = Label(main_frame, text="", font=("arial", 16))
    result_label.pack(pady=10)

    def convert():
        try:
            value = float(value_entry.get())
            src = from_unit_var.get()
            tgt = to_unit_var.get()
            result = value * length_units[src]['rate'] / length_units[tgt]['rate']
            result = int(result) if result.is_integer() else round(result, 4)
            result_label.config(text=f"{value} {src} == {result} {tgt}")
        except ValueError:
            result_label.config(text="error, invalid number")
    
    convert_btn = Button(main_frame, text="convert", width=15, height=2, command=convert)
    convert_btn.pack(pady=20)
    back_btn = Button(main_frame, text="back", width=10, height=2, background="red", foreground="white", command=open_converter_menu)
    back_btn.pack(pady=20)

#========================Mass Converter========================
def open_mass_converter():
    clear_frame()
    
    title = Label(main_frame, text="Mass Converter", font=("arial", 20))
    title.pack(pady=10)
    input_frame = Frame(main_frame)
    input_frame.pack(pady=10)

    value_entry = Entry(input_frame, font=("arial", 16), width=10)
    value_entry.grid(row=0, column=0, padx=5, pady=5)

    from_unit_var = StringVar()
    from_unit_var.set(list(mass_units.keys())[0])
    from_menu = OptionMenu(input_frame, from_unit_var, *mass_units.keys())
    from_menu.grid(row=0, column=2, padx=5, pady=5)

    to_unit_var = StringVar()
    to_unit_var.set(list(mass_units.keys())[0])
    to_menu = OptionMenu(input_frame, to_unit_var, *mass_units.keys())
    to_menu.grid(row=1, column=2, padx=5, pady=5)

    result_label = Label(main_frame, text="", font=("arial", 16))
    result_label.pack(pady=10)

    def convert():
        try:
            value = float(value_entry.get())
            src = from_unit_var.get()
            tgt = to_unit_var.get()
            result = value * mass_units[src]['rate'] / mass_units[tgt]['rate']
            result = int(result) if result.is_integer() else round(result, 4)
            result_label.config(text=f"{value} {src} == {result} {tgt}")
        except ValueError:
            result_label.config(text="error, invalid number")
    
    convert_btn = Button(main_frame, text="convert", width=15, height=2, command=convert)
    convert_btn.pack(pady=20)
    back_btn = Button(main_frame, text="back", width=10, height=2, background="red", foreground="white", command=open_converter_menu)
    back_btn.pack(pady=20)

#========================Date Counter========================
def open_date_counter():
    clear_frame()
    
    Label(main_frame, text="DATE COUNTER", font=("arial", 16)).pack(pady=20)
    
    Label(main_frame, text="Enter date (dd/mm/yyyy):", font=("arial", 12)).pack(pady=10)
    date_entry = Entry(main_frame, font=("arial", 14))
    date_entry.pack(pady=5)
    
    def calculate_date():
        date_input = date_entry.get().replace("-", "/").replace("_", "/").replace(" ", "/")
        try:
            past = datetime.strptime(date_input, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "Invalid date format! Please use dd/mm/yyyy")
            return
        
        now = datetime.now()
        days = (now - past).days
        years = days // 365
        months = (days % 365) // 30
        remaining_days = (days % 365) % 30
        
        show_date_result(years, months, remaining_days)
    
    Button(main_frame, text="Calculate", width=15, height=2, command=calculate_date).pack(pady=20)
    Button(main_frame, text="back", width=10, height=2, background="red", foreground="white", command=open_converter_menu).pack(pady=20)

def show_date_result(years, months, days):
    clear_frame()
    
    Label(main_frame, text="Date Difference Result", font=("arial", 16)).pack(pady=20)
    Label(main_frame, text=f"⏳ {years} years | {months} months | {days} days", font=("arial", 14)).pack(pady=20)
    
    Button(main_frame, text="Back", width=10, height=2, command=open_date_counter).pack(pady=20)

#========================Speed========================
def open_speed_converter():
    clear_frame()

    title = Label(main_frame, text="Speed Converter", font=("arial", 20))
    title.pack(pady=10)
    input_frame = Frame(main_frame)
    input_frame.pack(pady=10)

    value_entry = Entry(input_frame, font=("arial", 16), width=10)
    value_entry.grid(row=0, column=0, padx=5, pady=5)

    from_unit_var = StringVar()
    from_unit_var.set(list(speed_units.keys())[0])
    from_menu = OptionMenu(input_frame, from_unit_var, *speed_units.keys())
    from_menu.grid(row=0, column=2, padx=5, pady=5)

    to_unit_var = StringVar()
    to_unit_var.set(list(speed_units.keys())[0])
    to_menu = OptionMenu(input_frame, to_unit_var, *speed_units.keys())
    to_menu.grid(row=1, column=2, padx=5, pady=5)

    result_label = Label(main_frame, text="", font=("arial", 16))
    result_label.pack(pady=10)

    def convert():
        try:
            value = float(value_entry.get())
            src = from_unit_var.get()
            tgt = to_unit_var.get()
            result = value * speed_units[src]['rate'] / speed_units[tgt]['rate']
            result = int(result) if result.is_integer() else round(result, 4)
            result_label.config(text=f"{value} {src} == {result} {tgt}")
        except ValueError:
            result_label.config(text="error, invalid number")
    
    convert_btn = Button(main_frame, text="convert", width=15, height=2, command=convert)
    convert_btn.pack(pady=20)
    back_btn = Button(main_frame, text="back", width=10, height=2, background="red", foreground="white", command=open_converter_menu)
    back_btn.pack(pady=20)

#============================Discount============================
def open_discount_calculator():
    clear_frame()

    title = Label(main_frame, text="Discount", font=("arial", 15))
    title.pack(pady=20)
    input_frame = Frame(main_frame)
    input_frame.pack(pady=10)

    Label(input_frame, text="Original price:", font=("arial", 14)).grid(row=0, column=0, padx=5, pady=5)
    price_entry = Entry(input_frame, font=("arial", 14), width=10)
    price_entry.grid(row=0, column=1, padx=5, pady=5)
    
    Label(input_frame, text="Discount%:", font=("arial", 14)).grid(row=1, column=0, padx=5, pady=5)
    discount_entry = Entry(input_frame, font=("arial", 14), width=10)
    discount_entry.grid(row=1, column=1, padx=5, pady=5)
    
    result_label = Label(main_frame, text="", font=("arial", 16))
    result_label.pack(pady=15)
    
    def calculate_discount():
        try:
            price = float(price_entry.get())
            discount = float(discount_entry.get())

            discount_amount = price * (discount/ 100)
            final_price = price - discount_amount
            discount_amount = int(discount_amount) if discount_amount.is_integer() else round(discount_amount, 2)
            final_price = int(final_price) if final_price.is_integer() else round(final_price, 2)
            
            result_label.config(text=f"Finale price: {final_price}\n You save: {discount_amount}")
            
        except ValueError:
            result_label.config(text="error, invalid number")

    Button(main_frame, text="calculate", width=15, height=2, command=calculate_discount).pack(pady=(30, 10))
    Button(main_frame, text="back", width=10, height=2, background="red", foreground="white", command=open_converter_menu).pack(pady=(10, 20))

#========================Area Converter========================
def open_area_converter():
    clear_frame()

    title = Label(main_frame, text="Area Converter", font=("arial", 20))
    title.pack(pady=10)
    input_frame = Frame(main_frame)
    input_frame.pack(pady=10)

    value_entry = Entry(input_frame, font=("arial", 16), width=10)
    value_entry.grid(row=0, column=0, padx=5, pady=5)

    from_unit_var = StringVar()
    from_unit_var.set(list(area_units.keys())[0])
    from_menu = OptionMenu(input_frame, from_unit_var, *area_units.keys())
    from_menu.grid(row=0, column=2, padx=5, pady=5)

    to_unit_var = StringVar()
    to_unit_var.set(list(area_units.keys())[0])
    to_menu = OptionMenu(input_frame, to_unit_var, *area_units.keys())
    to_menu.grid(row=1, column=2, padx=5, pady=5)

    Label(input_frame, text="Discount%:", font=("arial", 14)).grid(row=1, column=0, padx=5, pady=5)
    discount_entry = Entry(input_frame, font=("arial", 14), width=10)
    discount_entry.grid(row=1, column=1, padx=5, pady=5)
    result_label = Label(main_frame, text="", font=("arial", 16))
    result_label.pack(pady=15)
    
    def convert():
        try:
            value = float(value_entry.get())
            src = from_unit_var.get()
            tgt = to_unit_var.get()
            result = value * area_units[src]['rate'] / area_units[tgt]['rate']
            result_label.config(text=f"{value} {src} == {result} {tgt}")
        except ValueError:
            result_label.config(text="error, invalid number")
    
    convert_btn = Button(main_frame, text="convert", width=15, height=2, command=convert)
    convert_btn.pack(pady=20)
    back_btn = Button(main_frame, text="back", width=10, height=2, background="red", foreground="white", command=open_converter_menu)
    back_btn.pack(pady=20)

#=======================BMI========================

def open_bmi_calculator():
    clear_frame()

    title = Label(main_frame, text="BMI Calculator", font=("arial", 15))
    title.pack(pady=20)
    input_frame = Frame(main_frame) 
    input_frame.pack(pady=10)

    Label(input_frame, text="Gender", font=("arial", 12)).grid(row=0, column=0, padx=5, pady=5)  
    gender_var = StringVar()
    gender_var.set("Male")
    radio_male = Radiobutton(input_frame, text="Male", variable=gender_var, value="Male")
    radio_male.grid(row=0, column=1, padx=5, pady=5)
    radio_female = Radiobutton(input_frame, text="Female", variable=gender_var, value="Female")
    radio_female.grid(row=0, column=2, padx=5, pady=5)

    Label(input_frame, text="Age:", font=("arial", 14)).grid(row=1, column=0, padx=5, pady=5)
    age_entry = Entry(input_frame, font=("arial", 14), width=10)
    age_entry.grid(row=1, column=1, padx=5, pady=5)

    Label(input_frame, text="Height (cm):", font=("arial", 14)).grid(row=2, column=0, padx=5, pady=5)
    height_entry = Entry(input_frame, font=("arial", 14), width=10)
    height_entry.grid(row=2, column=1, padx=5, pady=5)

    Label(input_frame, text="Weight (kg):", font=("arial", 14)).grid(row=3, column=0, padx=5, pady=5)
    weight_entry = Entry(input_frame, font=("arial", 14), width=10)
    weight_entry.grid(row=3, column=1, padx=5, pady=5)

    #result_label = Label(main_frame, text="", font=("arial", 16))
    #result_label.pack(pady=15)


    #bmi_title_label = Label(main_frame, text="", font=("arial", 16))
    #bmi_title_label.pack(pady=15)

    #bmi_result_label = Label(main_frame, text="", font=("arial", 16))
    #bmi_result_label.pack(pady=15)
    
    #ideal_weight_label = Label(main_frame, text="", font=("arial", 16))
    #ideal_weight_label.pack(pady=15)


    def calculate_bmi():
        try:
            gender = gender_var.get()
            age = int(age_entry.get())
            height = float(height_entry.get())
            weight = float(weight_entry.get())

            if age < 15:
                messagebox.showerror("can`t calculate BMI for people younger than 15 years old")
                return
            if height <= 0:
                messagebox.showerror(text="height must be positive")
                return
            if weight <= 0:
                messagebox.showerror("weight must be positive")
                return

            if gender == "Male":
                gender_factor = 1
            else:
                gender_factor = 0.95

            if age < 18:
                age_factor = 0.95
            elif 18 <= age <= 65:
                age_factor = 1
            else:
                age_factor = 1.05

            convert_h = (height * 0.01) **2
            BMI = weight / convert_h
            

            if BMI < 18.5:
                status = "Underweight ⚠️"
            elif 18.5 <= BMI < 24:
                status = "Normal ✅"
            elif 24 <= BMI < 28:
                status = "Overweight ⚠️"
            else:
                status = "Obese 🚨"
            
            

            min_weight = convert_h * 18.5 * age_factor * gender_factor
            max_weight = convert_h * 24 * age_factor * gender_factor

            show_bmi_result(BMI, status, min_weight, max_weight)
    
        except ValueError:
            messagebox.showerror("error, invalid input")
            


    convert_btn = Button(main_frame, text="calculate", width=15, height=2, command=calculate_bmi)
    convert_btn.pack(pady=20)
    back_btn = Button(main_frame, text="back", width=10, height=2, background="red", foreground="white", command=open_converter_menu)
    back_btn.pack(pady=20)

def show_bmi_result(BMI, status, min_w, max_w):
    clear_frame()
    Label(main_frame, text="Your BMI Result", font=("arial", 16)).pack(pady=20)
    
    Label(main_frame, text=f"BMI:    {BMI:.2f}", font=("arial", 14)).pack(pady=10)
    Label(main_frame, text=f"Status: {status}", font=("arial", 14)).pack(pady=10)
    Label(main_frame, text=f"Ideal range: {min_w:.1f} kg  →  {max_w:.1f} kg", font=("arial", 16)).pack(pady=20)
    Button(main_frame, text="back", width=10, height=2, background="red", foreground="white", command=open_bmi_calculator).pack(pady=20)

    
open_menu()

root.mainloop()
    
    