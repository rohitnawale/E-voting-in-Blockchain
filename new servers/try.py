from tkinter import *




def sel1():


    root3 = Tk()
    root3.title("SUBMIT")
    root3.config(background='purple4')
    root3.geometry("1600x8000")

        #print(var.get(),"sfvfsvfv")
    selection = "You Have Voted For " + var.get()
    label3 = Label(root3, bg='purple4', font=('arial', 16, 'bold'))

    label3.config(text=selection, bg='purple4')
    label3.pack()

    label4= Label(root3,bg='purple4', font=('arial', 16, 'bold'),text="Thanks for Voting ")
    label4.pack()

    homebutton = Button(root3, text="Go To Home Page", activebackground="LightBlue", relief="raised",
                              font=('arial', 16, 'bold'), bd=10, bg="MediumPurple1")
    homebutton.pack(side=LEFT)

    #confirmbutton = Button(root2, text="Confirm", activebackground="LightBlue", relief="raised",
     #                         font=('arial', 16, 'bold'), bd=10, bg="MediumPurple1")
    #confirmbutton.pack(side=LEFT)
root2 = Tk()
root2.title("VOTING")
root2.config(background='purple4')
root2.geometry("1600x8000")
var = StringVar()

r1 = Radiobutton(root2, text="Bhartiya Janta Party ", font=('arial', 16, 'bold'), variable=var, value="BJP", bg='purple4', command=sel1)
r1.pack(anchor=W)

r2 = Radiobutton(root2, text="Aam Aadmi Party", font=('arial', 16, 'bold'), variable=var, value="AAP", bg='purple4', command=sel1)
r2.pack(anchor=W)

r3 = Radiobutton(root2, text="Congress", font=('arial', 16, 'bold'), variable=var, value="CONGRESS", bg='purple4', command=sel1)
r3.pack(anchor=W)

r4 = Radiobutton(root2, text="Shivsena", font=('arial', 16, 'bold'), variable=var, value="SHIVSENA", bg='purple4', command=sel1)
r4.pack(anchor=W)

r5 = Radiobutton(root2, text="MNS", font=('arial', 16, 'bold'), variable=var, value="MNS", bg='purple4', command=sel1)
r5.pack(anchor=W)

root2.mainloop()