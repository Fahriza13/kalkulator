import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title('Kalkulator Sederhana')

        self.display = tk.Entry(master, width=25, font=('Arial', 14), bg="white")
        self.display.grid(row=0, column=0, columnspan=4, pady=5, padx=5)

        self.create_button('7', 1, 0)
        self.create_button('8', 1, 1)
        self.create_button('9', 1, 2)
        self.create_button('/', 1, 3)

        self.create_button('4', 2, 0)
        self.create_button('5', 2, 1)
        self.create_button('6', 2, 2)
        self.create_button('*', 2, 3)

        self.create_button('1', 3, 0)
        self.create_button('2', 3, 1)
        self.create_button('3', 3, 2)
        self.create_button('-', 3, 3)

        self.create_button('0', 4, 0)
        self.create_button('.', 4, 1)
        self.create_button('C', 4, 2)
        self.create_button('+', 4, 3)

        self.create_button('=', 5, 0, columnspan=2)
        self.create_button('\u232B', 5, 2, columnspan=2)

        self.equation = ''

    def create_button(self, text, row, column, rowspan=1, columnspan=1):
        button = tk.Button(self.master, text=text, width=5, height=2, font=('Arial', 12), bg="yellow",
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, pady=2, padx=2)

    def button_click(self, text):
        if text == '=':
            try:
                self.equation = str(eval(self.equation))
            except:
                self.equation = 'Error'
            self.display.delete(0, tk.END)
            self.display.insert(0, self.equation)
        elif text == 'C':
            self.equation = ''
            self.display.delete(0, tk.END)
        elif text == '\u232B':
            self.equation = self.equation[:-1]
            self.display.delete(len(self.equation), tk.END)
        elif text in ['+', '-', '*', '/']:
            if self.equation and self.equation[-1] in ['+', '-', '*', '/']:
                self.equation = self.equation[:-1]
                self.display.delete(len(self.equation), tk.END)
            self.equation += text
            self.display.insert(tk.END, text)
        else:
            self.equation += text
            self.display.insert(tk.END, text)

root = tk.Tk()
app = Calculator(root)
root.mainloop()