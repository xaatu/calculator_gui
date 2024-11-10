import tkinter as tk
import math 

def append_to_expression(value):
    current_text = entry_display.get()
    entry_display.delete(0, tk.END) 
    entry_display.insert(0, current_text + str(value)) 

def calculate():
    try:
        expression = entry_display.get()
        
        expression = expression.replace('^', '**')
        
        result = eval(expression) 
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result)) 
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(0, "You did something silly.") 

def clear_display():
    entry_display.delete(0, tk.END)  

def calculate_square_root():
    try:
        value = float(entry_display.get())
        result = math.sqrt(value)
        entry_display.delete(0, tk.END)
        entry_display.insert(0, str(result))
    except Exception as e:
        entry_display.delete(0, tk.END)
        entry_display.insert(0, "You did something silly.") 

# WINDOW
root = tk.Tk()
root.title("CALC-U-L8R ALLIG8R")
root.geometry("400x450")  
root.configure(bg='black')

# DISPLAY
entry_display = tk.Entry(root, width=16, font=('Mono', 24), bg='white', fg='black')
entry_display.grid(row=0, column=0, columnspan=4, pady=15)

# ASTERISK/SLASH LABELS
left_asterisk = tk.Label(root, text='\*', font=('Mono', 46), bg='black', fg='white')
left_asterisk.grid(row=0, column=0, pady=10)

right_asterisk = tk.Label(root, text='*/', font=('Mono', 46), bg='black', fg='white')
right_asterisk.grid(row=0, column=3, pady=10)

# BUTTONS
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '', '0', '', '+',
    '√', '^', 'C', '='  
]

row_val = 1
col_val = 0

button_font = ('Mono', 14, 'bold')

for button in buttons:
    if button == '=':
        tk.Button(root, text=button, command=calculate, bg='white', fg='black', 
                    height=3, width=5, borderwidth=3, relief='raised', font=button_font).grid(row=row_val, column=col_val, pady=5, padx=5)
    elif button == 'C':
        tk.Button(root, text=button, command=clear_display, bg='white', fg='black', 
                    height=3, width=5, borderwidth=3, relief='raised', font=button_font).grid(row=row_val, column=col_val, pady=5, padx=5)
    elif button == '√':
        tk.Button(root, text=button, command=calculate_square_root, bg='white', fg='black', 
                    height=3, width=5, borderwidth=3, relief='raised', font=button_font).grid(row=row_val, column=col_val, pady=5, padx=5)
    elif button == '^':
        tk.Button(root, text=button, command=lambda: append_to_expression('**'), bg='white', fg='black', 
                    height=3, width=5, borderwidth=3, relief='raised', font=button_font).grid(row=row_val, column=col_val, pady=5, padx=5)
    else:
        tk.Button(root, text=button, command=lambda b=button: append_to_expression(b), bg='white', fg='black', 
                    height=3, width=5, borderwidth=3, relief='raised', font=button_font).grid(row=row_val, column=col_val, pady=5, padx=5)
    
    col_val += 1
    if col_val > 3: 
        col_val = 0
        row_val += 1


root.mainloop()
