from tkinter import *
import BackPage
import FirstPage

def main():
    party=""

    def sel(p):

        def finish():
            def home():
                root3.destroy()
                FirstPage.main()

            #print(var.get())
            root1.destroy()
            root2.destroy()
            root3 = Tk()
            root3.title("FINISH")
            root3.config(background='purple4')
            root3.geometry("1600x8000")
            label4 = Label(root3, font=('arial', 16, 'bold'), text="THANKS FOR VOTING", bd='8',bg='purple4')
            label4.pack()
            homebutton = Button(root3, font=('arial', 16, 'bold'), text="Go to Home Page",command =home, activebackground="LightBlue",
                                  relief="raised", bd=10, bg="MediumPurple1")

            homebutton.pack(side=TOP)

        #def back():
         #   root1.destroy()
          #  root2.destroy()
           # BackPage.main()

        root2 = Tk()
        root2.title("SUBMIT")
        root2.config(background='purple4')
        root2.geometry("1600x8000")

        #print(var.get(),"sfvfsvfv")
        selection = "You Have Voted For " + p
        label3 = Label(root2, bg='purple4', font=('arial', 16, 'bold'))

        label3.config(text=selection, bg='purple4')
        label3.pack()

        #backbutton = Button(root2, text="Back", activebackground="LightBlue", relief="raised",
         #                     font=('arial', 16, 'bold'), bd=10, bg="MediumPurple1",command=back)
        #backbutton.pack(side=LEFT)

        confirmbutton = Button(root2, text="Confirm", activebackground="LightBlue", relief="raised",
                              font=('arial', 16, 'bold'), bd=10, bg="MediumPurple1", command=finish)
        confirmbutton.pack(side=LEFT)

    root1 = Tk()
    root1.title("VOTING")
    root1.config(background='purple4')
    root1.geometry("1600x8000")
    var = StringVar()

    r1 = Radiobutton(root1, text="Bhartiya Janta Party ", font=('arial', 16, 'bold'), variable=var, value="BJP", bg='purple4')
    r1.pack(anchor=W)

    r2 = Radiobutton(root1, text="Aam Aadmi Party", font=('arial', 16, 'bold'), variable=var, value="AAP", bg='purple4')
    r2.pack(anchor=W)

    r3 = Radiobutton(root1, text="Congress", font=('arial', 16, 'bold'), variable=var, value="CONGRESS", bg='purple4')
    r3.pack(anchor=W)

    r4 = Radiobutton(root1, text="Shivsena", font=('arial', 16, 'bold'), variable=var, value="SHIVSENA", bg='purple4')
    r4.pack(anchor=W)

    r5 = Radiobutton(root1, text="MNS", font=('arial', 16, 'bold'), variable=var, value="MNS", bg='purple4')
    r5.pack(anchor=W)
    party=var.get()
    print(party)
    sel(party)

    root1.mainloop()