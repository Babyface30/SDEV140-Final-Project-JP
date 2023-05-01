import tkinter as tk
from datetime import date

def calculate_age():
    today = date.today()
    birth_date = date(int(year_entry.get()), int(month_entry.get()), int(day_entry.get()))
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    age_label.config(text="Age: " + str(age))

def clear_fields():
    day_entry.delete(0, tk.END)
    month_entry.delete(0, tk.END)
    year_entry.delete(0, tk.END)
    age_label.config(text="")

def quit_program():
    root.destroy()

root = tk.Tk()
root.title("Age Calculator")

# Labels
tk.Label(root, text="Day").grid(row=0, column=0)
tk.Label(root, text="Month").grid(row=1, column=0)
tk.Label(root, text="Year").grid(row=2, column=0)
age_label = tk.Label(root, text="")
age_label.grid(row=3, column=1)

# Entry fields
day_entry = tk.Entry(root)
month_entry = tk.Entry(root)
year_entry = tk.Entry(root)
day_entry.grid(row=0, column=1)
month_entry.grid(row=1, column=1)
year_entry.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Calculate Age", command=calculate_age).grid(row=4, column=0)
tk.Button(root, text="Clear Fields", command=clear_fields).grid(row=4, column=1)
tk.Button(root, text="Quit", command=quit_program).grid(row=4, column=2)

root.mainloop()