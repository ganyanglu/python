import tkinter as tk

root = tk.Tk()
root.geometry('400x300')
root.title('my test python')
txt = tk.StringVar()
label = tk.Label(root, textvariable = txt, background = 'blue',width = 30)
label.pack()

ent = tk.Entry(root,width = 60)
ent.pack()

def hit_me():
    my_text = ent.get()
    txt.set(my_text)

btn = tk.Button(root,text='hit me',command = hit_me)
btn.pack()

root.mainloop()