from tkinter import *
import tkinter.ttk

class RegistrationUI():
    def insert(self):
        self.n=self.e1.get()
        self.ei=self.e2.get()
        self.uh=self.e3.get()
        self.p=self.e1.get()
        self.rp=self.e1.get()
        if(self.p==self.rp):
            self.uh="@"+self.uh

            print(self.n)
            print(self.ei)
            print(self.uh)
            print(self.p)

    def __init__(self, master):
        self.master=master
        self.f1 = Frame(master)
        self.f1.pack(fill="both", expand=True, padx=20, pady=20)
        self.master.title("_________ Forum - Registration Section")
        self.master.geometry('1024x768')
        self.f2=Frame(master)
        self.f2.place(in_=self.f1, anchor="c", relx=.5, rely=.5)

        #Labels
        self.l1=Label(self.f2,text="Enter User Name :")
        self.l1.grid(row=1,column=1,padx=10, pady=10)

        self.l2=Label(self.f2,text="Enter User Email ID :")
        self.l2.grid(row=2,column=1,padx=10, pady=10)

        self.l5=Label(self.f2,text="Enter User Handle :")
        self.l5.grid(row=3,column=1,padx=10, pady=10)

        self.l3=Label(self.f2,text="Enter Password :")
        self.l3.grid(row=4,column=1,padx=10, pady=10)

        self.l4=Label(self.f2,text="Reenter Password :")
        self.l4.grid(row=5,column=1,padx=10, pady=10)

        #Entry
        self.e1=Entry(self.f2,width=20)
        self.e1.grid(row=1,column=2,padx=10, pady=10)

        self.e2=Entry(self.f2,width=20)
        self.e2.grid(row=2,column=2,padx=10, pady=10)

        self.e5=Entry(self.f2,width=20)
        self.e5.grid(row=3,column=2,padx=10, pady=10)

        self.e3=Entry(self.f2,width=20)
        self.e3.grid(row=4,column=2,padx=10, pady=10)

        self.e4=Entry(self.f2,width=20)
        self.e4.grid(row=5,column=2,padx=10, pady=10)

        #Register Button
        self.register=Button(self.f2,text="Register",command=lambda:self.insert())
        self.register.grid(row=6,column=1,padx=10, pady=10)
        
        #Cancel Button
        self.cancel=Button(self.f2,text="Cancel")
        self.cancel.grid(row=6,column=2,padx=10, pady=10)
        
    



root = Tk()
my_gui = RegistrationUI(root)
root.mainloop()