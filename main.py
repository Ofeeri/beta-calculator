import tkinter
from tkinter import *

import calculate as cal

root = tkinter.Tk()
root.title("beta calculator")
root.geometry("280x240")

# index dropbox
index_label = Label(root, text="Choose an index:")
chosen_index = StringVar()
chosen_index.set("SPY")
indices_drop = OptionMenu(root, chosen_index, "SPY", "QQQ", "DIA")
index_label.grid(row=180, column=80, padx=5)
indices_drop.grid(row=190, column=80)

# timeframe dropbox
timeframe_label = Label(root, text="Choose timeframe")
chosen_timeframe = StringVar()
timeframes_drop = OptionMenu(root, chosen_timeframe, "5Y", "1Y", "6M", "3M")  # check if this works with yfinance
chosen_timeframe.set("5Y")
timeframe_label.grid(row=240, column=80)
timeframes_drop.grid(row=250, column=80)

# frequency dropbox
frequency_label = Label(root, text="Choose frequency")
chosen_frequency = StringVar()
frequency_drop = OptionMenu(root, chosen_frequency, "Monthly", "Weekly", "Daily")
chosen_frequency.set("Monthly")
frequency_label.grid(row=300, column=80)
frequency_drop.grid(row=310, column=80)

# ticker entry
ticker_label = Label(root, text="Enter ticker symbol:")
ticker_entry = Entry(root, width=8, borderwidth=2)
ticker_label.grid(row=180, column=700)
ticker_entry.grid(row=190, column=700)


def normalize_frequency(frequency):
    # converts frequency input to format that fits yfinance
    if frequency == "Monthly":
        return "1mo"
    if frequency == "Weekly":
        return "1wk"
    if frequency == "Daily":
        return "1d"


def button_click():
    index = chosen_index.get()
    ticker = ticker_entry.get().upper()
    timeframe = chosen_timeframe.get()
    frequency = normalize_frequency(chosen_frequency.get())
    beta = cal.main(index, ticker, timeframe, frequency)
    beta_label.config(text=f"Beta = {str(beta)}")


# calculate button
calculate_button = Button(root, text="Calculate", command=button_click)
calculate_button.grid(row=350, column=390, pady=10)

# display result
beta_label = Label(root, text="", fg="red")
beta_label.grid(row=360, column=390)


if __name__ == "__main__":
    root.mainloop()
