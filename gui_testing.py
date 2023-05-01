import tkinter
from PIL import Image,ImageTk
top = tkinter.Tk(className="New Window")
image = Image.open("test_image.jpg")
img = ImageTk.PhotoImage(image)
nb = tkinter.Button(top,text="Stop",width=1080,command=top.destroy,image=img)
nb.pack()
top.mainloop()