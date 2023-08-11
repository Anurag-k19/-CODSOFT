from tkinter import *
import string
import random

window=Tk()
window.geometry('300x200')
window.title('Password Generator')
window.configure(bg='#12181B')

label=Label(window,text='Enter the length of password',bg='#c9910e')
label.pack(pady=20)

e=Entry(window,bg='#a19d95',font='Poppins 12',)
e.place(x=60,y=50)

letters=string.ascii_letters
digits=string.digits
special=string.punctuation
all_characters=letters+digits+special


def onclick():
    x=e.get()
    q=int(x)
    e.delete(0,END)
    for i in range(0,q):
        a=random.choice(all_characters)
        Password.insert(END,a)

def clear():
    Password.delete("1.0","end")


Password=Text(window,font='Poppins 12',width=20,height=0,bg='#a19d95')
Password.pack(pady=55)

label_password=Label(window,text='Your Password',bg='#c9910e')
label_password.place(x=105,y=90)


button=Button(window,text='Generate',command=onclick,font='Poppins 12',bg='#eb113c')
button.place(x=60,y=150)

button_clear=Button(window,text='Delete',command=clear,font='Poppins 12',bg='#eb113c')
button_clear.place(x=180,y=150)





window.mainloop()