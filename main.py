from tkinter import *
from tkinter import messagebox
import random
import time


# ---------------------------------- Functions ---------------------------------
global count
count = 3
                    
def get_val(num1,num2):
  if num1>num2:
    # lblans = Label(win,text='Start should be less than end!')
    # lblans.grid(row=3,column=0)
    messagebox.showerror("Incorrect range", "Start should be less than end!") 
    return
  lblans = Label(win,text='')
  lblans.grid(row=3,column=0)
  global n1,n2
  n1 = num1
  n2 = num2
  global r_digit
  r_digit = random.randrange(num1,num2)
  btn = btn = Button(container,text='Generate random number',state=DISABLED)
  btn.grid(row=2,column=0,columnspan=2,pady=40)
  print(r_digit)

def check_guess(g):
  global count

  if r_digit ==None:
    messagebox.showerror('Range Absent','Please enter a range')
    return
  while count:
    userip = Entry(win,textvariable = guess)
    userip.grid(row=1,column=0)

    if g == r_digit:
      lblans = Label(win,text='You guessed the number correctly')
      lblans.grid(row=3,column=0)
      game = False
      break
    
    elif g<r_digit:
      lblans = Label(win,text='Guess higher')
      lblans.grid(row=3,column=0)
      break
    
    elif g>r_digit:
      lblans = Label(win,text='Guess Lower')
      lblans.grid(row=3,column=0)
      break
  count = count-1
  lbstatus = Label(win,text=f'You have {count} guess left',pady=20)
  lbstatus.grid(row=5,column=0,pady=20)
  if count == False:
    lblans = Label(win,text='You are out of guesses')
    lblans.grid(row=3,column=0)
    btnguess['state'] = DISABLED

  # Close window after winning
  # if game == False:
  #   time.sleep(3)
  #   win.destroy()


# ------------------------------------ main ------------------------------------
win = Tk()
win.title('Guess the number game')
win.geometry('500x550')

num1 = IntVar()
num2 = IntVar()
guess = IntVar()

container = LabelFrame(win,text='Guess the number',padx=50,pady=30)

ip1 = Entry(container,textvariable=num1)
ip2 = Entry(container,textvariable=num2)

btn = Button(container,text='Generate random number',command=lambda: get_val(num1.get(),num2.get()))

lb1 = Label(container,text='Start')
lb2 = Label(container,text='End')

userip = Entry(win,textvariable = guess)
btnguess = Button(win,text='Check',command=lambda: check_guess(guess.get()))
btnquit = Button(win,text='Quit',command=win.destroy)

container.grid(row=0,column=0,padx=50,pady=50)
ip1.grid(row=1,column=0,padx=20)
ip2.grid(row=1,column=1)
lb1.grid(row=0,column=0)
lb2.grid(row=0,column=1)
btn.grid(row=2,column=0,columnspan=2,pady=40)

userip.grid(row=1,column=0)
btnguess.grid(row=2,column=0,pady=15)
btnquit.grid(row=4,column=0)

  

win.mainloop()