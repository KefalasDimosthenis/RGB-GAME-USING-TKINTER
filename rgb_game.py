import tkinter as tk
from tkinter import *
import utils

attemp_counter = 0
best_score = [-1, -1, -1, -1]
root = Tk()
root.config(bg="white")
root.title("RGB GUESS")
root.resizable(width=FALSE, height=FALSE)
root.geometry("{}x{}".format(800, 800))
nxt_to_btn_var = tk.StringVar()
down_var = tk.StringVar()


def button_pressed(r, g, b, pc):
    global attemp_counter
    global best_score
    down_var.set(f"({r},{g},{b})")
    user_pick = (r, g, b)
    pc_pick = pc
    color_distance = utils.color_diff(user_pick, pc_pick)
    attemp_counter += 1
    best_scor = format(color_distance, ".2f")
    p = utils.rgb_to_Hex(user_pick)
    bot2_Frame.config(bg=p)

    if color_distance > best_score[0]:
        nxt_to_btn_var.set(
            f"Try {attemp_counter}/5, Best score {best_scor}% ({r},{g},{b})"
        )
        best_score[0] = color_distance
        best_score[1] = r
        best_score[2] = g
        best_score[3] = b
    else:
        best_scor = format(best_score[0], ".2f")
        nxt_to_btn_var.set(
            f"Try {attemp_counter}/5, Best score {best_scor}% ({best_score[1]},{best_score[2]},{best_score[3]})"
        )

    if color_distance > 10 and attemp_counter >= 5:
        dokimi["state"] = DISABLED
        nxt_to_btn_var.set("LOSE")

    elif color_distance <= 10:
        dokimi["state"] = DISABLED
        nxt_to_btn_var.set("WIN")
    else:
        return (color_distance, user_pick)


top_frame = Frame(root, bg="white", width=800, height=255, pady=3)
top_frame.grid(row=0, columnspan=3)

redtext = Label(top_frame, text="RED", bg="white")
redtext.grid(row=0, column=0)

slider_red = Scale(top_frame, from_=0, to=255, orient=HORIZONTAL, bg="white")
slider_red.grid(
    column=1,
    row=0,
)


greentext = Label(top_frame, text="GREEN", bg="white")
greentext.grid(row=1, column=0)

slider_green = Scale(top_frame, from_=0, to=255, orient=HORIZONTAL, bg="white")
slider_green.grid(column=1, row=1)
bluetext = Label(top_frame, text="BLUE", bg="white")
bluetext.grid(row=2, column=0)


slider_blue = Scale(top_frame, from_=0, to=255, orient=HORIZONTAL, bg="white")
slider_blue.grid(column=1, row=2)

pc_color_pick = utils.rand_color_picker()
dokimi = Button(
    top_frame,
    text="TEST",
    command=lambda: button_pressed(
        slider_red.get(), slider_green.get(), slider_blue.get(), pc_color_pick
    ),
)
dokimi.grid(row=3, column=0)


nxt_to_btn_var.set("Try 0/5")
next_to_btn = Label(top_frame, textvariable=nxt_to_btn_var, bg="white")
next_to_btn.grid(row=3, column=1)

bot1_frame = Frame(
    root, bg=utils.rgb_to_Hex(pc_color_pick), width=400, height=545, padx=3, pady=3
).grid(column=1, row=1, rowspan=2)

bot2_Frame = Frame(root, bg="White", width=400, height=545, padx=3, pady=3)
bot2_Frame.grid(column=2, row=1, rowspan=2)

final_frame1 = Frame(root, bg="White", width=400, height=100)
final_frame1.grid(row=3, column=1)

down_var.set("(0,0,0)")
final1_label = Label(final_frame1, text="Color target")
final1_label.grid(row=3, column=2)

final_frame2 = Frame(root, bg="White", width=400, height=100)
final_frame2.grid(row=3, column=2)

final2_label = Label(final_frame2, textvariable=down_var)
final2_label.grid(row=3, column=3)


root.mainloop()
