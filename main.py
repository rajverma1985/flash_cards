from tkinter import *
import random
from word_picker import list_words

BACKGROUND_COLOR = "#B1DDC6"

word = ''
lang_choice = ''


def pick_word():
    global timer
    global word
    global lang_choice
    window.after_cancel(timer)
    word = random.choice(list_words)
    lang_choice = [key for key in word]
    canvas.itemconfig(title_canvas, text=lang_choice[0], fill="black")
    canvas.itemconfig(word_canvas, text=word[lang_choice[0]], fill="black")
    canvas.itemconfig(canvas_image, image=front_img)
    timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_canvas, text=lang_choice[1], fill="white")
    canvas.itemconfig(word_canvas, text=word[lang_choice[1]], fill="white")
    canvas.itemconfig(canvas_image, image=back_image)


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
timer = window.after(3000, flip_card)

# canvas
canvas = Canvas(width=800, height=526)
front_img = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
title_canvas = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
word_canvas = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill="black")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# buttons and their images
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

rt_button = Button(image=right_image, highlightthickness=0, command=pick_word)
wr_button = Button(image=wrong_image, highlightthickness=0, command=pick_word)
rt_button.grid(row=1, column=0)
wr_button.grid(row=1, column=1)

pick_word()
window.mainloop()
