import tkinter
from tkinter import messagebox
import connectmysql
from cryptography.fernet import Fernet
import MainGUI

cipherKey = "k_5kBfW6Eq4eUEl7FzOZ09eQpJr35yZ6XbSAdVjiS7o="

def showAddPage():
    addWindow = tkinter.Tk()
    addWindow.title("GROUP#9 BSCPE-1D")
    addWindow.geometry("500x350")
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
    frameTitle = tkinter.Frame(addWindow)
    frameFirstName = tkinter.Frame(addWindow)
    frameLastName = tkinter.Frame(addWindow)
    frameEmailAdd = tkinter.Frame(addWindow)
    framePassword = tkinter.Frame(addWindow)
    frameButtons = tkinter.Frame(addWindow,pady=(20))

    labelTitle = tkinter.Label(frameTitle)
    labelTitle.config(text="Add User", font=("Arial", 25, "bold"), fg="red")

    labelFirstName = tkinter.Label(frameFirstName)
    labelFirstName.config(text="First Name:", font=("Arial", 15), padx=(15), pady=(10))
    entryFirstName = tkinter.Entry(frameFirstName)
    entryFirstName.config(font=("Arial", 15))

    labelLastName = tkinter.Label(frameLastName)
    labelLastName.config(text="Last Name:", font=("Arial", 15), padx=(15), pady=(10))
    entryLastName = tkinter.Entry(frameLastName)
    entryLastName.config(font=("Arial", 15))

    labelEmailAdd = tkinter.Label(frameEmailAdd)
    labelEmailAdd.config(text="Email Address:", font=("Arial", 15), padx=(15), pady=(10))
    entryEmailAdd = tkinter.Entry(frameEmailAdd)
    entryEmailAdd.config(font=("Arial", 15))

    labelPassword = tkinter.Label(framePassword)
    labelPassword.config(text="Password:", font=("Arial", 15), padx=(15), pady=(10))
    entryPassword = tkinter.Entry(framePassword)
    entryPassword.config(font=("Arial", 15))

    def addUser():
        SQLConnection = connectmysql.connectToSQL()
        SQLCursor = SQLConnection.cursor()
        sqlCommand = "INSERT INTO user (FirstName, LastName, EmailAdd, Password) VALUES (%s, %s, %s, %s)"
        firstName = entryFirstName.get()
        lastName = entryLastName.get()
        emailAdd = entryEmailAdd.get()
        password = entryPassword.get()
        if(firstName=="" or lastName=="" or emailAdd=="" or password==""):
            tkinter.messagebox.showwarning(title="Error!", message="Please fill out all the required information")
        else:
            #encrypting the password
            password = password.encode()
            cipherMode = Fernet(cipherKey)
            encryptedPassword = cipherMode.encrypt(password)

            sqlValues = (firstName, lastName, emailAdd, encryptedPassword)
            SQLCursor.execute(sqlCommand, sqlValues)
            SQLConnection.commit()
            SQLCursor.close()
            SQLConnection.close()
            messagebox.showinfo("Success", "User has been added Successfully!")
            addWindow.destroy()
            MainGUI.start()
    def cancel():
        addWindow.destroy()
        MainGUI.start()
    addButton = tkinter.Button(frameButtons, text="Add User", font=("Arial",15), command=addUser)
    cancelButton = tkinter.Button(frameButtons, text="Cancel", font=("Arial", 15), command=cancel)
    frameTitle.pack()
    frameFirstName.pack()
    frameLastName.pack()
    frameEmailAdd.pack()
    framePassword.pack()

    labelTitle.pack()
    labelFirstName.pack(side="left")
    entryFirstName.pack(side="left")
    labelLastName.pack(side="left")
    labelEmailAdd.pack(side="left")
    labelPassword.pack(side="left")
    entryLastName.pack(side="left")
    entryEmailAdd.pack(side="left")
    entryPassword.pack(side="left")
    cancelButton.pack(side="left")
    labelsa = tkinter.Label(frameButtons,text="   ")
    labelsa.pack(side="left")
    addButton.pack(side="left")
    frameButtons.pack()

