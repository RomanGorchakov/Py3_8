f2 = Frame()
f2.pack()
text = Text(f2, width = 50, height = 20, wrap = NONE)
text.pack(side = LEFT)
scroll = Scrollbar(f2, command = text.yview)
scroll.pack(side = LEFT, fill = Y)
text.config(yscrollcommand = scroll.set)

scroll2 = Scrollbar(orient=HORIZONTAL, command = text.xview)
scroll2.pack(side = BOTTOM, fill = X)
text.config(xscrollcommand = scroll2.set)

root.mainloop()

#~ from tkinter import *

#~ def smile():
    #~ label = Label(text = ":)", bg = "yellow")
    #~ text.window_create(INSERT, window = label)