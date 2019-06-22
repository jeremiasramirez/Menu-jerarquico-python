
maxChange = 0


def mostrar(v1, v2):
	global maxChange
	maxChange += 1

	savevalue = v2.get()

	print(savevalue)
	if maxChange < 2 and v2.get() != "":	
		v1.set(savevalue)
		v2.set("Solo puedes editar 1 vez")
		text2.config(state="disabled")
		text.config(state="disabled")

def call():
	mostrar(val, val2)

root = Tk(className="Validation") 
root.config(width=450, height=300)
root.resizable(0, 0)
val = StringVar()
val2 = StringVar()

img = None
def create():
	rootwindow = Tk(className="Nuevo")
	rootwindow.config(bg="orange", bd=0, width=400, height=680)
	baseroot = rootwindow.mainloop()

img = PhotoImage(file="icon2.png")
menubar = Menu(root)

menubar.config(font="Arial", fg="white", bg="black")

menuitem = Menu(menubar, tearoff=0)
menuitem.add_command(label="Abrir", command=create)
menuitem.add_command(label="Nuevo")

menuitem.add_command(label="Guardar")
menuitem.add_command(label="Cerrar", command=root.quit)
menubar.add_cascade(label="Menu", menu=menuitem)

root.config(menu=menubar)
val.set("Viejo valor")
text = Entry(root, textvariable=val)
text.place(x=0, y=0)
text.config(width=30, bd=0, font="Arial", selectbackground="orange")

text2 = Entry(root, textvariable=val2)
text2.place(x=0, y=30)
text2.config(width=30, bd=0, font="Arial", selectbackground="orange")
val2.set(val.get())
button = Button(root)
button.place(x=300, y=0)
 
 
button.config(text="actualizar", command=call)
 









root.mainloop()
