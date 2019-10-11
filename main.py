from tkinter import *
from tkinter.ttk import *
import database as db1

db1.create()
def click1():
    txt=income.get()
    db1.income(txt)

    db1.insert_expense("transportion",0)
    db1.insert_expense("food",0)
    db1.insert_expense("clothes",0)
def click2():
    db1.create_for_expences()
    txt=db1.select()
    Expense=comb.get()
    theExpensemoney=theExpense.get()
    themoneybefore=db1.get_the_money(Expense)
    theExpensemoney2=int(theExpensemoney)+int(themoneybefore)
    db1.insert_expense(Expense,theExpensemoney2)
    Balance=int(txt)-int(theExpensemoney)
    if Balance<0:
        Balance=0
    db1.income(Balance)
    label5=Label(window,text="Your Balance :    "+str(Balance),font=("Helvetica", 16))
    label5.grid(column=0,row=5,pady=15)
def click3():
    Transaction=db1.select_all_transcation()
    food=Transaction['food']
    transportion=Transaction['transportion']
    clothes=Transaction['clothes']
    label6=Label(window,text="transportion:"+str(transportion),font=("Helvetica", 16))
    label6.grid(column=0,row=7,pady=10)
    label6=Label(window,text="food:            "+str(food),font=("Helvetica", 16))
    label6.grid(column=0,row=8,pady=7)
    label6=Label(window,text="clothes:        "+str(clothes),font=("Helvetica", 16))
    label6.grid(column=0,row=9,pady=7)

window =Tk()
window.title("Expense Tracker")
window.geometry('600x500')
style=Style()
#background optional just insert your path
'''filename = PhotoImage(file = "/home/missrobot/Downloads/anime2.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)'''
style.configure('TButton',font=('calibri',10,'bold'),foreground='red')
comb=Combobox()
label1=Label(window,text="Please Enter You Income",font=("Helvetica", 16))
label1.grid(column=0,row=0)
income=Entry(window,width=10)
label2=Label(window,text="Your Income:",font=("Helvetica", 16))
label2.grid(column=0,row=1,pady=18)
income.grid(column=1,row=1)

button1=Button(window,text="Click Once",style='TButton',command=click1)
button1.grid(column=2,row=1,padx=10)
label4=Label(window,text="Add Expenses",font=("Helvetica", 16))
label4.grid(column=0,row=3,pady=20,padx=50)
comb['values']=("transportion","food","clothes")
comb.grid(column=0,row=4,pady=5)
theExpense=Entry(window,width=10)
theExpense.grid(column=1,row=4)
button2=Button(window,text="Click Once",style='TButton',command=click2)
button2.grid(column=2,row=4)
button3=Button(window,text="Show Transaction",command=click3)
button3.grid(column=0,row=6,pady=9)

window.mainloop()
