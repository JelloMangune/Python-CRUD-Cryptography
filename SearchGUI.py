import tkinter
from tkinter import messagebox
import connectmysql
from cryptography.fernet import Fernet
import MainGUI

cipherKey = "k_5kBfW6Eq4eUEl7FzOZ09eQpJr35yZ6XbSAdVjiS7o="

def showSearchPage():
    addWindow = tkinter.Tk()
    addWindow.title("GROUP#9 BSCPE-1D")
    addWindow.geometry("500x450")
    addWindow.resizable("False","False")
    #addWindow.eval('tk::PlaceWindow . center')
    #Center the screen
    def center(win):
        win.update_idletasks()
        width = win.winfo_width()
        frm_width = win.winfo_rootx() - win.winfo_x()
        win_width = width + 2 * frm_width
        height = win.winfo_height()
        titlebar_height = win.winfo_rooty() - win.winfo_y()
        win_height = height + titlebar_height + frm_width
        x = win.winfo_screenwidth() // 2 - win_width // 2
        y = win.winfo_screenheight() // 2 - win_height // 2
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
        win.deiconify()
    center(addWindow)

    def addUser():
        SQLConnection = connectmysql.connectToSQL()
        SQLCursor = SQLConnection.cursor()
        search = entrySearch.get()
        sqlCommand = "SELECT * FROM user WHERE UserID = " + search
        if(search==""):
            tkinter.messagebox.showwarning(title="Error!", message="Please input the UserID")
        else:
            SQLCursor.execute(sqlCommand)
            selectResult = SQLCursor.fetchall()
            SQLCursor.close()
            SQLConnection.close()
            if selectResult:
                for eachResult in selectResult:
                    cipherKey = "k_5kBfW6Eq4eUEl7FzOZ09eQpJr35yZ6XbSAdVjiS7o="
                    cipherMode = Fernet(cipherKey)
                    bytePass = str(eachResult[4])
                    decryptedPass = cipherMode.decrypt(bytes(bytePass, 'utf-8'))
                    decryptedPassword = decryptedPass.decode()

                    contentID.config(text=eachResult[0])
                    contentFName.config(text=eachResult[1])
                    contentLName.config(text=eachResult[2])
                    contentEmail.config(text=eachResult[3])
                    contentPassword.config(text=decryptedPassword)
                    print(eachResult)
            else:
                tkinter.messagebox.showwarning(title="Data not found!", message="User does not exist.")
            #messagebox.showinfo("Success", "User has been added Successfully!")
            #addWindow.destroy()
            #MainGUI.start()
    def cancel():
        addWindow.destroy()
        MainGUI.start()

    frameTitle = tkinter.Frame(addWindow)
    frameSearch = tkinter.Frame(addWindow)
    frameButtons = tkinter.Frame(addWindow,pady=(20))
    frameID = tkinter.Frame(addWindow)
    frameFName = tkinter.Frame(addWindow)
    frameLName = tkinter.Frame(addWindow)
    frameEmail = tkinter.Frame(addWindow)
    framePassword = tkinter.Frame(addWindow)

    labelTitle = tkinter.Label(frameTitle)
    labelTitle.config(text="Search User ID", font=("Arial", 25, "bold"), fg="red")

    labelSearch = tkinter.Label(frameSearch)
    labelSearch.config(text="User ID:", font=("Arial", 15), padx=(15), pady=(10))
    entrySearch = tkinter.Entry(frameSearch)
    entrySearch.config(font=("Arial", 15))

    labelID = tkinter.Label(frameID, text="User ID:", font=("Arial", 15), padx=(15), pady=(10))
    contentID = tkinter.Label(frameID, text="", font=("Arial", 15), padx=(15), pady=(10))

    labelFName = tkinter.Label(frameFName, text="First Name:", font=("Arial", 15), padx=(15), pady=(10))
    contentFName = tkinter.Label(frameFName, text="", font=("Arial", 15), padx=(15), pady=(10))

    labelLName = tkinter.Label(frameLName, text="Last Name:", font=("Arial", 15), padx=(15), pady=(10))
    contentLName = tkinter.Label(frameLName, text="", font=("Arial", 15), padx=(15), pady=(10))

    labelEmail = tkinter.Label(frameEmail, text="Email Address:", font=("Arial", 15), padx=(15), pady=(10))
    contentEmail = tkinter.Label(frameEmail, text="", font=("Arial", 15), padx=(15), pady=(10))

    labelPassword = tkinter.Label(framePassword, text="Password:", font=("Arial", 15), padx=(15), pady=(10))
    contentPassword = tkinter.Label(framePassword, text="", font=("Arial", 15), padx=(15), pady=(10))

    addButton = tkinter.Button(frameButtons, text="Search User", font=("Arial",15), command=addUser)
    cancelButton = tkinter.Button(frameButtons, text="Cancel", font=("Arial", 15), command=cancel)
    frameTitle.pack()

    labelTitle.pack()
    frameSearch.pack()
    labelSearch.pack(side="left")
    entrySearch.pack(side="left")
    cancelButton.pack(side="left")
    labelsa = tkinter.Label(frameButtons,text="   ")
    labelsa.pack(side="left")
    addButton.pack(side="left")
    frameButtons.pack()
    frameID.pack()
    labelID.pack(side="left")
    contentID.pack(side="left")
    frameFName.pack()
    labelFName.pack(side="left")
    contentFName.pack(side="left")
    frameLName.pack()
    labelLName.pack(side="left")
    contentLName.pack(side="left")
    frameEmail.pack()
    labelEmail.pack(side="left")
    contentEmail.pack(side="left")
    framePassword.pack()
    labelPassword.pack(side="left")
    contentPassword.pack(side="left")

