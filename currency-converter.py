from tkinter import * 

class CurrencyConverter(Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("300x317")

        # layout configuration
        # rows 
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 1)
        self.rowconfigure(2, weight = 1)

        # columns 
        for i in range (2):
            self.columnconfigure(i, weight = 1)

        # widgets
        self.title_label = Title(self)
        self.title_label.grid(row = 0, sticky = EW)
        # self.input_frame = InputFrame(self)
        # self.input_frame.grid(row = 0, sticky = EW, pady = (0,5))
        
        self.mainloop()

class Title(Frame):
    def __init__(self, parent):
        super().__init__(parent, height = 50, width = 300)

        # layout configuration
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.grid_propagate(False)

        self.title = Label(self, text = "Currency Converter", font = ('Helvetica', 12), background = '#BDB6AC', foreground = '#0a0a0a',)
        self.title.grid(row = 0, rowspan = 2, column = 0, columnspan = 2, sticky = NSEW)

class InputFrame(Frame):
    def __init__(self, parent):
        super().__init__(parent)

if __name__ == "__main__":
    CurrencyConverter()