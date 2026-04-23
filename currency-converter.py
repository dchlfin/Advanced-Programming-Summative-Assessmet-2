import os
import requests
from tkinter import * 
from tkinter import ttk

# load apikey from .env file
from dotenv import load_dotenv

class CurrencyConverter(Tk):
    def __init__(self):
        super().__init__()
        self.title("Currency Converter")
        self.geometry("300x317")
        self.resizable(False, False)
        self.config(background = "#F2EDE7")

        # api request values
        self.base_url = "https://api.freecurrency.api.com/v1/"
        self.api_key = os.getenv("api_key")
        
        self.all_currencies = ['eur', 'usd', 'jpy', 'bgn', 'czk', 'dkk', 'gbp', 'huf', 'pln', 'ron', 'sek', 'chf', 'isk', 'nok', 'hrk', 'rub', 'try', 'aud', 'brl', 'cad', 'cny', 'hkd', 'idr', 'inr', 'krw', 'mxn', 'myr', 'nzd', 'php', 'sgd', 'thb', 'zar']

        # layout configuration
        # rows 
        self.rowconfigure(0, weight = 0)
        self.rowconfigure(1, weight = 0)
        self.rowconfigure(2, weight = 1)

        # columns 
        for i in range (2):
            self.columnconfigure(i, weight = 1)

        # widgets
        self.title_label = Title(self, "#BDB6AC")
        self.title_label.grid(row = 0, sticky = NSEW)
        self.input_frame = InputFrame(self, "#BDB6AC", self.base_url, self.api_key, self.all_currencies)
        self.input_frame.grid(row = 1, pady = (22, 15))
        # self.input_frame = InputFrame(self)
        # self.input_frame.grid(row = 0, sticky = EW, pady = (0,5))
        self.output_frame = OutputFrame(self, "#BDB6AC")
        self.output_frame.grid(row = 2, pady = (0, 14))
        
        self.mainloop()

class Title(Frame):
    def __init__(self, parent, bg):
        super().__init__(parent, height = 50, width = 300, bg = bg)

        # layout configuration
        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)
        self.grid_propagate(False)

        self.title = Label(self, text = "Currency Converter", font = ('Helvetica', 15, 'bold'), background = '#BDB6AC', foreground = '#0a0a0a',)
        self.title.grid(row = 0, rowspan = 2, column = 0, columnspan = 2)

class InputFrame(Frame):
    def __init__(self, parent, bg, base_url, api_key, all_currencies):
        super().__init__(parent, height = 144, width = 200, bg = bg)

        # initialize api values
        self.base_url = base_url
        self.api_key = api_key
        self.all_currencies = all_currencies 

        # layout configuration
        for i in range(3):
            self.rowconfigure(i, weight = 1)
            self.columnconfigure(i, weight = 1)
        
        self.grid_propagate(False)

        vcmd = (self.register(self.callback))

        self.amount = Entry(self, font = ('Helvetica', 12), bg = "#F2EDE7", relief = FLAT, width = 30, validate = 'all', validatecommand = (vcmd, '%P'))
        self.amount.grid(row = 0, column = 0, columnspan = 3)
    
        #comboboxes
        # FROM
        currencies = self.supported_currencies
        from_currency_cmb = ttk.Combobox(self, values = currencies, font = ('Helvetica', 12), foreground = '#F2EDE7', background = '#C44010')
        from_currency_cmb.grid(row = 1, column = 0, sticky = E)
        to_currency_cmb = ttk.Combobox(self, values = currencies, font = ('Helvetica', 12), foreground = '#F2EDE7', background = '#C44010')
        to_currency_cmb.grid(row = 1, column = 2, sticky = W)

        # convert button
        convert_btn = Button(self, text = "CONVERT", foreground = '#F2EDE7', background = '#C44010', relief = FLAT, command = self.get_amount)
        convert_btn.grid(row = 2, column = 0, columnspan = 3, sticky = EW, padx = 15)

        for widget in self.winfo_children():
            widget.grid(padx = 15, pady = 5)

    # methods
    # validate entry input if it is a number or not
    def callback(self, P):
        return str.isdigit(P) or P == ""
    
    # get amount to convert
    def get_amount(self):
        amount = self.amount.get()

        # return nothing if entry is empty, return amount otherwise
        return None if amount == "" else float(amount)
    
    def supported_currencies(self):
        # form request url
        url = f"{self.base_url}currencies?apikey={self.api_key}"
        print(url)

        # assign the raw data as the api 'response'
        response = requests.get(url)

        # if the request is succesful
        if response.status_code == 200:
            # parse the raw data into a Python dictionary
            currencies_data = response.json()
            if "data" in currencies_data:
                # access the "data" value in the dictionary
                currencies = currencies_data["data"]

                # gathers each currency keycode into a list
                currencies_keys = list(currencies.keys())
                return currencies_keys
            else:
                return None


class OutputFrame(Frame):
    def __init__(self, parent, bg):
        super().__init__(parent, height = 76, width = 200, bg = bg)

        # layout configuration
        # rows
        self.rowconfigure(0, weight = 1)

        # columns
        for i in range(2):
            self.columnconfigure(i, weight = 1)

        self.grid_propagate(False)

        converted_amount = Label(self, text = "", font = ('Helvetica', 12), foreground = '#0a0a0a', background = '#F2EDE7')
        converted_amount.grid(row = 0, column = 0, columnspan = 2, padx = 15, pady = 5, sticky = EW)

if __name__ == "__main__":
    load_dotenv()
    CurrencyConverter()