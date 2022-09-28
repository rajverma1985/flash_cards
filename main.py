import random
from tkinter import *
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
df = pd.read_csv("data/german_en.csv")
lang_words = [df["German"]]
translation = [df["English"]]

window = Tk()
window.title("Flash Cards")
# window.resizable(False, False)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


# canvas
canvas = Canvas(width=800, height=526)
flashkcard_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400, 263, image=flashkcard_img)
canvas.create_text(400, 150, text="German", font=("Ariel", 40, "italic"), fill="black")
canvas.create_text(400, 263, text="Some Word", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# buttons and their images
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

rt_button = Button(image=right_image, highlightthickness=0)
wr_button = Button(image=wrong_image, highlightthickness=0)
rt_button.grid(row=1, column=0)
wr_button.grid(row=1, column=1)

window.mainloop()
