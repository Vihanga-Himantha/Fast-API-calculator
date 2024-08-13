import tkinter as tk
import requests

# Define the server URL
SERVER_URL = "http://18.143.66.235/calculate"  # Replace with your server's URL

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = entry_operator.get()

        response = requests.get(
            SERVER_URL,
            params={"num1": num1, "num2": num2, "operator": operator}
        )
        response.raise_for_status()  # Raise an error if the request failed
        result = response.json().get("result")
        label_result.config(text=f"Result: {result}")
    except requests.exceptions.RequestException as e:
        label_result.config(text=f"Error: {e}")
    except ValueError:
        label_result.config(text="Invalid input. Please enter valid numbers.")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create and place the widgets
label_num1 = tk.Label(root, text="Enter first number:")
label_num1.pack()

entry_num1 = tk.Entry(root)
entry_num1.pack()

label_num2 = tk.Label(root, text="Enter second number:")
label_num2.pack()

entry_num2 = tk.Entry(root)
entry_num2.pack()

label_operator = tk.Label(root, text="Enter operator (+, -, *, /):")
label_operator.pack()

entry_operator = tk.Entry(root)
entry_operator.pack()

button_calculate = tk.Button(root, text="Calculate", command=calculate)
button_calculate.pack()

label_result = tk.Label(root, text="Result: ")
label_result.pack()

# Start the Tkinter event loop
root.mainloop()
