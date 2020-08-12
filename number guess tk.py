import tkinter
import random


computer_guess = random.randint(1,10)

def check():
    user_guess = int( txt_guess.get())

    if user_guess < computer_guess:
        msg ="higher!"
    elif user_guess > computer_guess:
        msg ="lower!"
    elif user_guess == computer_guess:
        msg ="correct!"
    else:
        msg ="Something went wrong..."

    lbl_result["text"] = msg
        
def reset():
    global computer_guess
    computer_guess = random.randint(1,10)
    lbl_result["text"] = "Game reset. Guess again!"

root = tkinter.Tk()

lbl_title = tkinter.Label(root, text="Welcome to the guessing game!")
lbl_title.pack()

lbl_result = tkinter.Label(root, text="Good Lock!")
lbl_result.pack()

btn_check = tkinter.Button(root, text="check",fg="green",command=check)
btn_check.pack(side="left")

btn_reset = tkinter.Button(root, text="Reset",fg="red",command=reset)
btn_reset.pack(side="right")

txt_guess =tkinter.Entry(root, width=3)
txt_guess.pack()

root.mainloop()
root.destroy()
