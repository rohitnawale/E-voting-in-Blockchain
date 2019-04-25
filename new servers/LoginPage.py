from tkinter import *
import VotingPage
from tkinter import messagebox
import vclient

root = Tk()
username=""
password=""


def main():
    root = Tk()
    root.title("Login")
    root.geometry("1600x8000")

    Tops = Frame(root, width=1600, relief=SUNKEN)
    Tops.grid()

    f1 = Frame(root, width=800, height=700, relief=SUNKEN)
    f1.grid()

    def VPage():
        user=e.get()
        pas=f.get()
        print(user,pas)

        if vclient.validate(user,pas)=="yes":
            root.destroy()
            VotingPage.main()

        else:
            messagebox.showinfo("ERROR" ,"Either username or password is invalid. Please try again.")

#****************************      LOGIN PAGE       *******************************

    label1 = Label(Tops, text="E-VOTING",  bd='8', font=('helvetica', 50, 'bold'))
    label1.grid(row=0, column=0)

    a = Label(f1, font=('arial', 16, 'bold'), text="USERNAME", bd='8')
    a.grid(row=5, column=10, sticky=E)

    b = Label(f1, font=('arial', 16, 'bold'), text="PASSWORD", bd='8')
    b.grid(row=6, column=10, sticky=E)

    username = StringVar()
    password = StringVar()

    e = Entry(f1, font=('arial', 16, 'bold'), textvariable=username, insertwidth=6, bg="MediumPurple1", bd=10)
    e.grid(row=5, column=11)

    f = Entry(f1, font=('arial', 16, 'bold'), show="*", textvariable=password, insertwidth=4, bg="MediumPurple1", bd=10)
    f.grid(row=6, column=11)






    LoginButton = Button(f1, font=('arial', 16, 'bold'),text="Login", activebackground="LightBlue",
                         relief="raised", command=VPage, bd=10, bg="MediumPurple1")
    LoginButton.grid(row=8, column=2)

    root.mainloop()
