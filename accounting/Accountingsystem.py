from tkinter import*
from tkinter import messagebox
import Accountingdata
import Accountingsystemdata


root=Tk()
root.title('ACCOUNTING 2')
root.geometry('450x700')
root.config(bg='khaki4')

def cal():
	c=int(enmaccount.get())-int(enpardakhty.get())
	d=int(enmaccount.get())+int(endaryafty.get())
	if int(enpardakhty.get()) >0:
		enalbaghy.insert(END,c)
	elif int(endaryafty.get()) >0:
		enalbaghy.insert(END,d)
	else:
		enalbaghy==0

def clear():
	enidaccount.delete(0,END)
	ennaccount.delete(0,END)
	enmaccount.delete(0,END)
	enpardakhty.delete(0,END)
	endaryafty.delete(0,END)
	entozihat.delete(0,END)
	enalbaghy.delete(0,END)
	list.delete(0,END)

def adddata():
	cal()
	Accountingsystemdata.adddata(enidaccount.get(),ennaccount.get(),enmaccount.get(),enpardakhty.get(),endaryafty.get(),entozihat.get(),enalbaghy.get())
	list.delete(0,END)
	list.insert(END,(enidaccount.get(),ennaccount.get(),enmaccount.get(),enpardakhty.get(),endaryafty.get(),entozihat.get(),enalbaghy.get()))
	enmaccount.delete(0,END)
	enmaccount.insert(END,enalbaghy.get())
	
	

	
def viewdata():
	list.delete(0,END)
	for row in Accountingsystemdata.viewdata():
		list.insert(END,row)
	

def selectitem(event):
	global selecteditem
	index=list.curselection()[0]
	selecteditem=list.get(index)
	enidaccount.delete(0,END)
	enidaccount.insert(END,selecteditem[1])
	ennaccount.delete(0,END)
	ennaccount.insert(END,selecteditem[2])
	enmaccount.delete(0,END)
	enmaccount.insert(END,selecteditem[3])
	enpardakhty.delete(0,END)
	enpardakhty.insert(END,selecteditem[4])
	endaryafty.delete(0,END)
	endaryafty.insert(END,selecteditem[5])
	entozihat.delete(0,END)
	entozihat.insert(END,selecteditem[6])
	enalbaghy.delete(0,END)
	enalbaghy.insert(END,selecteditem[7])
	
	
def deldata():
	e=messagebox.askyesno('ACCOUNTING SYSTEM','ARE YOU SURE YOU WANT TO DELETE THIS CLIENT?\nALL DATA FOR THIS CLIENT WILL BE GONE!!')
	if e>0:
		
		Accountingsystemdata.deldata(selecteditem[0])
		enidaccount.delete(0,END)
		ennaccount.delete(0,END)
		enmaccount.delete(0,END)
		enpardakhty.delete(0,END)
		endaryafty.delete(0,END)
		entozihat.delete(0,END)
		enalbaghy.delete(0,END)
	else:
		return
	viewdata()
	

def update():
	Accountingsystemdata.update(selecteditem[0],enidaccount.get(),ennaccount.get(),enmaccount.get(),enpardakhty.get(),endaryafty.get(),entozihat.get(),enalbaghy.get())
	viewdata()
	messagebox.showinfo('client management system',f'The client updated\n{enidaccount.get()}\n{ennaccount.get()}\n{enmaccount.get()}\n{enpardakhty.get().upper()}\n{endaryafty.get()}\n{entozihat.get()}\n{enalbaghy.get().upper()}')
	
	
	
	
def search2():
			list.delete(0,END)
			for row in Accountingsystemdata.search(enidaccount.get(),ennaccount.get(),enmaccount.get(),enpardakhty.get(),endaryafty.get(),entozihat.get(),enalbaghy.get()):
				list.insert(END,row)






	
def searchitem(event):
	for row in Accountingsystemdata.search(enidaccount.get(),ennaccount.get()):
				ennaccount.delete(0,END)
				ennaccount.insert(END,row[2])
				enmaccount.delete(0,END)
				enmaccount.insert(END,row[7])
	
	
	
def searchitem1(event):
	for row in Accountingsystemdata.search(enidaccount.get(),ennaccount.get(),enmaccount.get()):
				enidaccount.delete(0,END)
				enidaccount.insert(END,row[1])
				enmaccount.delete(0,END)
				enmaccount.insert(END,row[7])	
	

	
f1=LabelFrame(root,relief=RIDGE,bg='khaki3',bd=5)
f1.pack()
lbl=Label(f1,text='ACCOUNTING SYSTEM',bg='khaki4',font='times 20 italic bold',padx=22)
lbl.pack()

f2=LabelFrame(root,relief=RIDGE,bg='khaki3',bd=5)
f2.pack()
lbl=Label(f2,text='id_account',bg='khaki3',font='times 7 italic bold')
lbl.grid(row=0,column=0,pady=20)

lbl=Label(f2,text='N_account',bg='khaki3',font='times 7 italic bold')
lbl.grid(row=1,column=0)

lbl=Label(f2,text='M_account',bg='khaki3',font='times 7 italic bold')
lbl.grid(row=2,column=0,pady=20)

enidaccount=Entry(f2,font='times 10 italic bold',bg='black',fg='gold',width=30)
enidaccount.bind('<Return>',searchitem)
enidaccount.grid(row=0,column=1)

ennaccount=Entry(f2,font='times 10 italic bold',bg='black',fg='gold',width=30)
ennaccount.bind('<Return>',searchitem1)
ennaccount.grid(row=1,column=1)

enmaccount=Entry(f2,font='times 10 italic bold',bg='black',fg='gold',width=30)
enmaccount.grid(row=2,column=1)


f3=LabelFrame(root,relief=RIDGE,bg='khaki3',bd=7)
f3.pack()

daryafti=IntVar()
pardakhti=IntVar()



lbl=Label(f3,text='PARDAKHTI',bg='khaki3',font='times 7 italic bold')
lbl.grid(row=0,column=0,pady=20)

lbl=Label(f3,text='DARYAFTI',bg='khaki3',font='times 7 italic bold')
lbl.grid(row=1,column=0)

lbl=Label(f3,text='ALBAGHI',bg='khaki3',font='times 7 italic bold')
lbl.grid(row=2,column=0,pady=20)

enpardakhty=Entry(f3,font='times 10 italic bold',bg='black',fg='gold',width=32,textvariable=pardakhti)
#enidaccount.bind('<Return>',searchitem)
enpardakhty.grid(row=0,column=1)

endaryafty=Entry(f3,font='times 10 italic bold',bg='black',fg='gold',width=32,textvariable=daryafti)
#ennaccount.bind('<Return>',searchitem1)
endaryafty.grid(row=1,column=1)

entozihat=Entry(f3,font='times 10 italic bold',bg='black',fg='gold',width=41)
entozihat.grid(row=3,column=0,columnspan=2)

enalbaghy=Entry(f3,font='times 10 italic bold',bg='black',fg='gold',width=32,borderwidth=5)
enalbaghy.grid(row=2,column=1)

f4=LabelFrame(root,relief=RIDGE,bg='khaki3',bd=7)
f4.pack()

btnadd=Button(f4,text='ADD',bg='khaki4',font='times 7 italic bold',width=3,command=adddata)
btnadd.grid(row=0,column=0)

btnclr=Button(f4,text='Clr',bg='khaki4',font='times 7 italic bold',width=2,command=clear)
btnclr.grid(row=0,column=1)

btnview=Button(f4,text='VIEW',bg='khaki4',font='times 7 italic bold',width=3,command=viewdata)
btnview.grid(row=0,column=2)

btnupdate=Button(f4,text='UPD',bg='khaki4',font='times 7 italic bold',width=3,command=update)
btnupdate.grid(row=0,column=3)

btndel=Button(f4,text='DEL',bg='khaki4',font='times 7 italic bold',width=3,command=deldata)
btndel.grid(row=0,column=4)

btnsearch=Button(f4,text='SEARCH',bg='khaki4',font='times 7 italic bold',width=3,command=search2)
btnsearch.grid(row=0,column=5)

btncal=Button(f4,text='PRINT',bg='khaki4',font='times 7 italic bold',width=3)
btncal.grid(row=0,column=6)

btnexit=Button(f4,text='EXIT',bg='khaki4',font='times 7 italic bold',width=3,command=exit)
btnexit.grid(row=0,column=7)



f5=LabelFrame(root,relief=RIDGE,bg='khaki3',bd=7)
f5.pack()

scroll=Scrollbar(f5)
scroll.pack(side=RIGHT,fill=Y)

scroll2=Scrollbar(f5,orient=HORIZONTAL)
scroll2.pack(side=BOTTOM,fill=X)

list=Listbox(f5,width=60,font='times 8 italic bold',height=40,yscrollcommand=scroll.set,xscrollcommand=scroll2.set,bg='khaki4')
list.bind('<<ListboxSelect>>',selectitem)
list.pack(side=LEFT,fill=BOTH)
scroll.config(command=list.yview)
scroll2.config(command=list.xview)

root.mainloop()