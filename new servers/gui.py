from tkinter import *
import vclient
from messenger_client import *
import messenger_client
#from uvalidation import *




my_port = 5551
my_host = "192.168.43.224"
        # my_port = 5556
receiver = messenger_client.Receiver(my_host, my_port)
receiver.start()
        # server_host = input("server host: ")
        # server_port = int(input("server port: "))

server_host = "192.168.43.177"
server_port = 5555
#def sub():

    #user_name = str(var.get())
    #root1.destroy()
 #   sender = messenger_client.Sender(server_host, server_port, my_host, my_port)
    #treads = [receiver.start(), sender.start()]
  #  treads =  [sender.start()]







choice=""
root = Tk()
root.title("Login")
root.config(background='purple4')
root.geometry("300x200")
root.overrideredirect(True)


def VotingPage():
    def sub():
        messenger_client.my_vote= str(var.get())
        root1.destroy()
        usernam=str(var.get())
        sender = messenger_client.Sender(server_host,usernam, server_port, my_host, my_port)
        # treads = [receiver.start(), sender.start()]
        treads = [sender.start()]

    def sel():

        selection = "You selected the option " + str(var.get())
        label3.config(text=selection, bg='purple4')
        choice = str(var.get())

    root1 = Tk()
    root1.title("VOTING")
    root1.config(background='purple4')
    root1.geometry("300x200")
    var = IntVar()

    r1 = Radiobutton(root1, text="Option 1", variable=var, value=1, command=sel, bg='purple4')
    r1.pack(anchor=W)

    r2 = Radiobutton(root1, text="Option 2", variable=var, value=2, command=sel, bg='purple4')
    r2.pack(anchor=W)

    r3 = Radiobutton(root1, text="Option 3", variable=var, value=3, command=sel, bg='purple4')
    r3.pack(anchor=W)

    label3 = Label(root1)
    label3.pack()


    submitbutton = Button(root1, text="Submit", activebackground="LightBlue",command=sub, relief="raised")
    submitbutton.pack()
    print(choice)
    root1.mainloop()


#def validate(u,p):
#body
    #return 1

def newpg():

    un = username.get()
    pw = password.get()
    if vclient.validate(un, pw) == "yes":
        root.destroy()
        VotingPage()


    else:
        print("error")



#####################################################################################################
#start of execution
#LOGIN PAGE

label1 = Label(root, text="E-VOTING", bg='purple4', bd='8').grid(row=0, column=1)

a = Label(root, text="USERNAME", bg='purple4', bd='8').grid(row=5, column=0)

b = Label(root, text="PASSWORD", bg='purple4', bd='8').grid(row=6, column=0)
username = StringVar()
password = StringVar()

e = Entry(root, textvariable=username).grid(row=5, column=1)

f = Entry(root, show="*", textvariable=password).grid(row=6, column=1)

LoginButton = Button(text="Login", activebackground="LightBlue", relief="raised", command=newpg).grid(columnspan=2)
user_name=username.get()
user_pass=password.get()
myvote=str(choice)
#print(myvote)
#treads=[messenger_client.receiver.start() , messenger_client.sender.start()]

root.mainloop()
