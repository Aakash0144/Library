from tkinter import*
from tkinter.ttk import Combobox

class LibraryManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Library Management System")
        self.root.geometry("720x480+0+0")

        lbltitle=Label(self.root,text="LIBRARY MANAGEMENT SYSTEM",bg="blue",fg="yellow",bd=20,font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)

        frame=Frame(self.root,bd=12,relief=RIDGE,bg="grey")
        frame.place(x=0,y=200,width=1365,height=450)


        lblMember=Label(frame,bg="grey",text="Name",font=("times new roman",15,"bold"))
        lblMember.grid(row=0,column=0,sticky=W)

        comMember=Combobox(frame,font=("times new roman",15,"bold"),width=27,state=WRITABLE)
        comMember.grid(row=0,column=1)
       

        lblMember=Label(frame,bg="grey",text="P. Name",font=("times new roman",15,"bold"))
        lblMember.grid(row=1,column=0,sticky=W)


        comMember=Combobox(frame,font=("times new roman",15,"bold"),width=27,state=WRITABLE)
        comMember.grid(row=1,column=1)



        lblMember=Label(frame,bg="grey",text="Age",font=("times new roman",15,"bold"))
        lblMember.grid(row=2,column=0,sticky=W)

        comMember=Combobox(frame,font=("times new roman",15,"bold"),width=27,state=WRITABLE)
        comMember["value"]=("20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35")
        comMember.grid(row=2,column=1)


    
        
if __name__ == "__main__":
    root=Tk()
    obj=LibraryManagementSystem(root)
    root.mainloop()