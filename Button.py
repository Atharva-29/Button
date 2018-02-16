import tkinter as tk
def p():
	print("Hello")
root=tk.Tk()
frame = tk.Frame(root)
frame.pack()
b=tk.Button(frame,text="Print",fg="BLue",bg="WHITE",command=p)
b.pack(side=tk.LEFT)
slogan=tk.Button(frame,text="Quit",fg="red",bg="WHITE",command=quit)
slogan.pack(side=tk.LEFT)
root.mainloop()