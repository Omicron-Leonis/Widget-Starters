import tkinter as tk
from tkinter import messagebox

# Function to calculate the product of two numbers
def calculate_product():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        text_box.delete("1.0", tk.END)  # Clear the Text Box
        text_box.insert(tk.END, f"The product is: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Create the main window
window = tk.Tk()
window.title("Getting Started with Widgets")
window.geometry("400x300")

# Add a label to describe the functionality
label_description = tk.Label(window, text="This application calculates the product of two numbers.", fg="blue")
label_description.pack(pady=10)

# Add two labels for input
label1 = tk.Label(window, text="Enter the first number:")
label1.pack()

entry1 = tk.Entry(window)
entry1.pack()

label2 = tk.Label(window, text="Enter the second number:")
label2.pack()

entry2 = tk.Entry(window)
entry2.pack()

# Add a button to calculate the product
calculate_button = tk.Button(window, text="Calculate Product", command=calculate_product, bg="lightgreen")
calculate_button.pack(pady=10)

# Add a Text Box to display the result
text_box = tk.Text(window, height=4, width=40, bg="lightyellow")
text_box.pack(pady=10)

# Run the application
window.mainloop()
