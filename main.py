from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
data_list={}


try:
    data=pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data=pd.read_csv("data/french_words.csv")
    data_list=original_data.to_dict(orient="records")
else:
    data_list = data.to_dict(orient="records")

def next_card():
    global current_card,flip_timer
    window.after_cancel(flip_timer)
    current_card=random.choice(data_list)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image=card_front_img)
    flip_timer=window.after(3000,flip_the_card)

def is_known():
    data_list.remove(current_card)
    df=pd.DataFrame(data_list)
    df.to_csv("data/words_to_learn.csv",index=False)
    next_card()

def flip_the_card():
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image=card_back_img)

#-----------------------------------------UI----------------------------------------------------------#

window=Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

flip_timer=window.after(3000,flip_the_card)


canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img=PhotoImage(file="images/card_front.png")
card_background=canvas.create_image(400,263,image=card_front_img)
card_back_img=PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=card_back_img)
card_title=canvas.create_text(400,150,text="",font=("Ariel",40,"italic"))
card_word=canvas.create_text(405,280,text="",font=("Ariel",60,"bold"))

canvas.grid(row=0,column=0,columnspan=2)

next_card()
#-------------------------------------------BUTTONS---------------------------------------------------#

#buttons
tick_img=PhotoImage(file="images/right.png")
tick_button=Button(image=tick_img,highlightthickness=0,command=is_known)
tick_button.grid(row=1,column=1)


wrong_img=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong_img,highlightthickness=0,command=next_card)
wrong_button.grid(row=1,column=0)


window.mainloop()

