import tkinter as tk

cookies = 0

window = tk.Tk()
window.title('Hello world')


def something():
    print('You clicked the button!')
def add_cookie():
    global cookies
    cookies = cookies + 1
    mylabel.config(text=f"You have {cookies} cookies!")
def something_else():
    print('You clicked the checkbutton!')
    print(f'The button\'s value is: {myvar.get()}')
    
    # if myvar.get() == '1':
    #     mylabel.config(text='The checkbutton is checked')
    # else:
    #     mylabel.config(text="The checkbutton is not checked")
    

myvar = tk.Variable()

mytext = tk.Label(text="Kars for Kids")
mybutton = tk.Button(text="Thanks for clicking the iPhone 15", command=something)
mycheckbutton = tk.Checkbutton(command=something_else, variable=myvar)
mylabel = tk.Label(text="The checkbutton has not yet been clicked.")

mytext.pack()
mybutton.pack()
mycheckbutton.pack()
mylabel.pack()
window.mainloop()
