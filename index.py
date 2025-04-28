import tkinter as tk
from tkinter import messagebox

def convert_currency():
    try:
        amount = float(entry_amount.get())
        from_currency = currency_from.get()
        to_currency = currency_to.get()

        rates = {
            'USD': {'INR': 83.20, 'EUR': 0.93},
            'INR': {'USD': 0.012, 'EUR': 0.011},
            'EUR': {'USD': 1.07, 'INR': 89.15},
        }

        if from_currency == to_currency:
            result = amount
        elif from_currency in rates and to_currency in rates[from_currency]:
            result = amount * rates[from_currency][to_currency]
        else:
            raise ValueError(f"Conversion rate from {from_currency} to {to_currency} not available.")

        label_result.config(text=f"{amount} {from_currency} = {result:.2f} {to_currency}", fg="green")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def reset_fields():
    entry_amount.delete(0, tk.END)
    currency_from.set('USD')
    currency_to.set('INR')
    label_result.config(text="", fg="black")

# Create UI
root = tk.Tk()
root.title("Currency Converter")
root.config(bg="#f4f4f9")  # Set background color

# Title Label
title_label = tk.Label(root, text="Currency Converter", font=("Helvetica", 20, "bold"), bg="#f4f4f9", fg="#2c3e50")
title_label.grid(row=0, columnspan=2, pady=10)

# Amount Entry
tk.Label(root, text="Amount:", font=("Arial", 12), bg="#f4f4f9").grid(row=1, column=0, padx=10, pady=5)
entry_amount = tk.Entry(root, font=("Arial", 12), bd=2, relief="solid", width=15)
entry_amount.grid(row=1, column=1, padx=10, pady=5)

# From Currency Dropdown
tk.Label(root, text="From Currency:", font=("Arial", 12), bg="#f4f4f9").grid(row=2, column=0, padx=10, pady=5)
currency_from = tk.StringVar(root)
currency_from.set('USD')  # Default value
dropdown_from = tk.OptionMenu(root, currency_from, 'USD', 'INR', 'EUR')
dropdown_from.config(font=("Arial", 12), relief="solid", bd=2)
dropdown_from.grid(row=2, column=1, padx=10, pady=5)

# To Currency Dropdown
tk.Label(root, text="To Currency:", font=("Arial", 12), bg="#f4f4f9").grid(row=3, column=0, padx=10, pady=5)
currency_to = tk.StringVar(root)
currency_to.set('INR')  # Default value
dropdown_to = tk.OptionMenu(root, currency_to, 'USD', 'INR', 'EUR')
dropdown_to.config(font=("Arial", 12), relief="solid", bd=2)
dropdown_to.grid(row=3, column=1, padx=10, pady=5)

# Convert Button
convert_button = tk.Button(root, text="Convert", font=("Arial", 12, "bold"), bg="#3498db", fg="white", command=convert_currency, relief="raised", bd=5)
convert_button.grid(row=4, columnspan=2, pady=15)

# Reset Button
reset_button = tk.Button(root, text="Reset", font=("Arial", 12, "bold"), bg="#e74c3c", fg="white", command=reset_fields, relief="raised", bd=5)
reset_button.grid(row=5, columnspan=2, pady=10)

# Result Label
label_result = tk.Label(root, text="", font=("Arial", 14), bg="#f4f4f9", fg="black")
label_result.grid(row=6, columnspan=2, pady=10)

root.mainloop()
