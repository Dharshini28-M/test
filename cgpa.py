import tkinter as tk

def evaluate_expression():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, columnspan=4)

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

for i, button_text in enumerate(buttons):
    row, col = divmod(i, 4)
    tk.Button(root, text=button_text, command=lambda text=button_text: entry.insert(tk.END, text)).grid(row=row + 1, column=col)

tk.Button(root, text="=", command=evaluate_expression).grid(row=5, column=0, columnspan=4)

root.mainloop()
