import tkinter as tk

"""Decimal to Binary Converter"""

class BinaryConverter():
    def __init__(self):
        self.decimalToBinary = tk.Tk()
        self.decimalToBinary.title("Decimal to Binary Converter")
        self.decimalToBinary_label = tk.Label(
            self.decimalToBinary, text="Decimal number:") 
        self.input_1 = tk.Entry(self.decimalToBinary)
        self.convert_button = tk.Button(self.decimalToBinary, 
            text="Convert", command = self.convert)
        self.result_label = tk.Label(self.decimalToBinary, 
            text="Binary number: ")

        self.decimalToBinary_label.pack()
        self.input_1.pack()
        self.convert_button.pack()
        self.result_label.pack()

    def convert_to_binary(self, x):
        if x > 1:
            return self.convert_to_binary(x//2) + str(x%2)
        else:
            return str(x % 2)

    def convert(self):
        num = self.input_1.get()
        if num.isnumeric() == True:
            num = int(num)
            biNum = self.convert_to_binary(num)
            self.result_label['text'] = f"Binary number: {biNum}"
        else: 
            self.result_label['text'] = f"Please enter a number only!"
    
    def run(self):
        self.decimalToBinary.mainloop()

if __name__ == '__main__':
    decimalToBinary = BinaryConverter()
    decimalToBinary.run()
