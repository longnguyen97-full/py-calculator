import tkinter as tk
from tkinter import ttk
from calculator import Calculator

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(False, False)
        
        self.calculator = Calculator()
        self.setup_gui()
        
    def setup_gui(self):
        # Display
        self.display = ttk.Entry(self.root, justify="right", font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")
        
        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        for button in buttons:
            cmd = lambda x=button: self.click(x)
            ttk.Button(self.root, text=button, command=cmd).grid(
                row=row, column=col, padx=2, pady=2, sticky="nsew"
            )
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Clear button
        ttk.Button(self.root, text="C", command=self.clear).grid(
            row=5, column=0, columnspan=4, padx=2, pady=2, sticky="nsew"
        )
        
        # Configure grid weights
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
            
    def click(self, key):
        if key == '=':
            try:
                expression = self.display.get()
                result = eval(expression)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            self.display.insert(tk.END, key)
            
    def clear(self):
        self.display.delete(0, tk.END)
        self.calculator.clear()

def main():
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main() 