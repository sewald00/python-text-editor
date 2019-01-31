from tkinter import *
from tkinter import filedialog

root = Tk()
savefile=('')

title=root.title('Py-Note')
root.attributes('-fullscreen', False)





# Place holder function
def minimize():
    root.attributes('-fullscreen', False)

def maximize():
    root.attributes('-fullscreen', True)

def hello():
    print ("hello!")

def openfile():
    global savefile

    savefile=filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("text files","*.txt"),("python files","*.py*"),("all files","*.*")))
    load=open(savefile,'r')
    loaded=load.read()

    load.close()
    page.delete(1.0, END)
    page.insert(END, loaded)

def save_as():

    global savefile
    savefile = filedialog.asksaveasfilename(initialdir="/", title="Select file",filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    print(savefile)
    save = open(savefile, "w+")

    contents = page.get(1.0, END)
    save.write(contents)


def save_new():
    global savefile
    save=open(savefile, "w+")
    contents = page.get(1.0, END)
    save.write(contents)

def about():
    info=Tk()
    info.title("About")
    e=Entry(info)
    e.pack()
    e.insert(END, "Created by Seth Ewald")
    info.mainloop()

def size():
    sizes=Tk()
    sizes.resizable(False,False)
    sizes.title("Select Font Size")
    sizes.geometry("400x50")
    w=Scale(sizes, orient=HORIZONTAL).pack()
    sizes.mainloop()

def font():
    fonts=Tk()
    fonts.title("Select Font")
    one=Radiobutton(fonts, text="Helvetica").pack(anchor=W)
    two = Radiobutton(fonts, text="Times").pack(anchor=W)
    fonts.mainloop()

def color():
    colors=Tk()
    colors.title("Select Text Color")
    colors.mainloop()

# create main menu bar
menubar = Menu(root)

# create file drop down in the main menu bar
filemenu = Menu(menubar, tearoff=1)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_command(label="Save", command=save_new)
filemenu.add_command(label="Save As", command=save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

# create edit drop down in main menu bar
editmenu = Menu(menubar, tearoff=1)
editmenu.add_command(label="Cut", command=hello)
editmenu.add_command(label="Copy", command=hello)
editmenu.add_command(label="Paste", command=hello)
menubar.add_cascade(label="Edit", menu=editmenu)

# create options drop down in main menu bar
optionsmenu= Menu(menubar, tearoff=1)
optionsmenu.add_command(label="Font", command=font)
optionsmenu.add_command(label="Size", command=size)
optionsmenu.add_command(label="Color", command=color)
optionsmenu.add_command(label="Spacing", command=hello)
optionsmenu.add_command(label="Maximize", command=maximize)
optionsmenu.add_command(label="Minimize", command=minimize)
menubar.add_cascade(label="Options", menu=optionsmenu)

# create help drop down in main menu bar
helpmenu = Menu(menubar, tearoff=1)
helpmenu.add_command(label="About", command=about)
menubar.add_cascade(label="Help", menu=helpmenu)

# create scroll bar for text widget
scrollbar = Scrollbar(root, width=20, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)


# display the menu
root.config(menu=menubar)

page=Text(root, yscrollcommand=scrollbar.set)
page.pack(expand=True, fill=BOTH)

scrollbar.config(command=page.yview)
mainloop()