from tkinter import *

expression = "" 

def press(num):
    
	
    global expression 
    expression = expression + str(num)
    equation.set(expression)

def equalpress(): 
	
	try: 

		global expression 

		total = str(eval(expression)) 

		equation.set(total) 
		expression = "" 

	except: 

		equation.set(" error ") 
		expression = "" 

def clear(): 
	global expression 
	expression = "" 
	equation.set("") 

if "main":
    
    
	gui = Tk() 
	gui.configure(background="white") 
	gui.title("Simple Calculator") 
	gui.geometry("400x298") 
	equation = StringVar() 
	expression_field = Entry(gui, textvariable=equation,font=('Arial',15)) 
	expression_field.grid(row=0,column=0,columnspan=100,padx=0,pady=0, ipady=10,ipadx=90)
	button_font=('Arial',12)
	button1 = Button(gui, text=' 1 ', fg='white', bg='black', 
					command=lambda: press(1), height=2, width=10,font=button_font) 
	button1.grid(row=2, column=0) 

	button2 = Button(gui, text=' 2 ', fg='white', bg='black', 
					command=lambda: press(2), height=2, width=10,font=button_font) 
	button2.grid(row=2, column=1) 

	button3 = Button(gui, text=' 3 ', fg='white', bg='black', 
					command=lambda: press(3), height=2, width=10,font=button_font) 
	button3.grid(row=2, column=2) 

	button4 = Button(gui, text=' 4 ', fg='white', bg='black', 
					command=lambda: press(4), height=2, width=10,font=button_font) 
	button4.grid(row=3, column=0) 

	button5 = Button(gui, text=' 5 ', fg='white', bg='black', 
					command=lambda: press(5), height=2, width=10,font=button_font) 
	button5.grid(row=3, column=1) 

	button6 = Button(gui, text=' 6 ', fg='white', bg='black', 
					command=lambda: press(6), height=2, width=10,font=button_font) 
	button6.grid(row=3, column=2) 

	button7 = Button(gui, text=' 7 ', fg='white', bg='black', 
					command=lambda: press(7), height=2, width=10,font=button_font) 
	button7.grid(row=4, column=0) 

	button8 = Button(gui, text=' 8 ', fg='white', bg='black', 
					command=lambda: press(8), height=2, width=10,font=button_font) 
	button8.grid(row=4, column=1) 

	button9 = Button(gui, text=' 9 ', fg='white', bg='black', 
					command=lambda: press(9), height=2, width=10,font=button_font) 
	button9.grid(row=4, column=2) 

	button0 = Button(gui, text=' 0 ', fg='white', bg='black', 
					command=lambda: press(0), height=2, width=10,font=button_font) 
	button0.grid(row=5, column=0) 

	plus = Button(gui, text=' + ', fg='black', bg='orange', 
				command=lambda: press("+"), height=2, width=10,font=button_font) 
	plus.grid(row=2, column=3) 

	minus = Button(gui, text=' - ', fg='black', bg='orange', 
				command=lambda: press("-"), height=2, width=10,font=button_font) 
	minus.grid(row=3, column=3) 

	multiply = Button(gui, text=' * ', fg='black', bg='orange', 
					command=lambda: press("*"), height=2, width=10,font=button_font) 
	multiply.grid(row=4, column=3) 

	divide = Button(gui, text=' / ', fg='black', bg='orange', 
					command=lambda: press("/"), height=2, width=10,font=button_font) 
	divide.grid(row=5, column=3) 

	equal = Button(gui, text=' = ', fg='black', bg='orange', 
				command=equalpress, height=2, width=10,font=button_font) 
	equal.grid(row=6, column=3) 

	clear = Button(gui, text='Clear', fg='black', bg='red', 
				command=clear, height=2, width=10,font=button_font) 
	clear.grid(row=5, column=2) 

	Decimal= Button(gui, text='.', fg='white', bg='black', 
					command=lambda: press('.'), height=2, width=10,font=button_font) 
	Decimal.grid(row=5, column=1) 
	
	gui.mainloop()
