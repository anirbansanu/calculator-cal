#this is the gui for the calculator app
from tkinter import *
from tkinter.font import Font

from evaluate import evaluate


def on_click(x):
    print("clicked  ", x)
    if x == "AC":
        e.delete(0, END)
    elif x == "C":
        e.delete(len(e.get())-1)
    elif x == "=":
        e_string = str(e.get())
        answer = evaluate(e_string)
        e.delete(0, END)
        e.insert(INSERT, str(answer))
        t.insert(END, e_string+" = "+str(answer)+"\n")
    else:
        e.insert(INSERT, x)


root = Tk()
root.title("Calculator")
root.resizable(width=False, height=False)

t_font = Font(family="Helvetica, Arial, sans-serif", size=20)

f = Frame(root, bg="#55aeed")
f.grid(row=0)

e = Entry(f, width=35, font=t_font, bd=4)
e.grid(row=1, columnspan=5)

f2 = Frame(f)
f2.grid(row=2, columnspan=5)

sbar = Scrollbar(f2)
sbar.pack(side=RIGHT, fill=Y)

t = Text(f2, width=34, height=2, fg="black", bg="white", font=t_font, wrap=WORD, yscrollcommand=sbar.set)
t.pack(side=LEFT)
sbar.config(command=t.yview())


l = Label(f, text="Calculator", font=t_font, bg="#55aeed", fg="white")
l.grid(row=3, columnspan=5)


btns_names = ["1", "2", "3", "C", "AC", "4", "5", "6", "+", "-",
              "7", "8", "9", "*", "/", "0", "00", ".", "√", "^",
              "()", "{}", "[]", "%", "="]

btns = []

for i in btns_names:
    btns.append(Button(f, text=str(i), font=t_font, width=5, bd=4, command=lambda x = i:on_click(x)))


nxt = 0
for row in range(4, 9):
    for col in range(0, 5):
        btns[nxt].grid(row=row, column=col)
        nxt += 1


l1 = Label(f, text="------------------Proudly powered by Anirban Mukherjee-------------------", bg="#55aeed", fg="white")
l1.grid(row=9, columnspan=5)

root.mainloop()
#this is the gui for the calculator app
