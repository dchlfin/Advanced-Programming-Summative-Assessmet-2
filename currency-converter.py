from tkinter import * 

class CurrencyConverter(Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("300x317")

        # layout configuration
        for i in range(2):
            self.rowconfigure(i, weight = 1)

        # widgets
        # self.input_frame = InputFrame(self)
        # self.input_frame.grid(row = 0, sticky = EW, pady = (0,5))
        
        self.mainloop()

class InputFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

if __name__ == "__main__":
    CurrencyConverter()