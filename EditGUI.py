import tkinter
from tkinter import messagebox
import connectmysql
from cryptography.fernet import Fernet
import MainGUI

cipherKey = "k_5kBfW6Eq4eUEl7FzOZ09eQpJr35yZ6XbSAdVjiS7o="

def showEditPage(current):
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

    #def editUser():

    def cancel():
        addWindow.destroy()
        MainGUI.start()
    frameTitle = tkinter.Frame(addWindow)
    frameButtons = tkinter.Frame(addWindow,pady=(20))
    frameID = tkinter.Frame(addWindow)
    frameFName = tkinter.Frame(addWindow)
    frameLName = tkinter.Frame(addWindow)
    frameEmail = tkinter.Frame(addWindow)
    framePassword = tkinter.Frame(addWindow)

    labelTitle = tkinter.Label(frameTitle)
    labelTitle.config(text="Edit User Info", font=("Arial", 25, "bold"), fg="red")


    labelID = tkinter.Label(frameID, text="User ID:", font=("Arial", 15), padx=(15), pady=(10))
    contentID = tkinter.Label(frameID, text="", font=("Arial", 15), padx=(15), pady=(10))

    labelFName = tkinter.Label(frameFName, text="First Name:", font=("Arial", 15), padx=(15), pady=(10))
    contentFName = tkinter.Entry(frameFName, font=("Arial", 15))

    labelLName = tkinter.Label(frameLName, text="Last Name:", font=("Arial", 15), padx=(15), pady=(10))
    contentLName = tkinter.Entry(frameLName, font=("Arial", 15))

    labelEmail = tkinter.Label(frameEmail, text="Email Address:", font=("Arial", 15), padx=(15), pady=(10))
    contentEmail = tkinter.Entry(frameEmail, font=("Arial", 15))

    labelPassword = tkinter.Label(framePassword, text="Password:", font=("Arial", 15), padx=(15), pady=(10))
    contentPassword = tkinter.Entry(framePassword, font=("Arial", 15))

    frameTitle.pack()
    SQLConnection = connectmysql.connectToSQL()
    SQLCursor = SQLConnection.cursor()
    sqlCommand = "SELECT * FROM user WHERE UserID = " + current
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
            contentFName.insert(-1, eachResult[1])
            contentLName.insert(-1, eachResult[2])
            contentEmail.insert(-1, eachResult[3])
            contentPassword.insert(-1, decryptedPassword)
            print(eachResult)
    else:
        addWindow.destroy()
        tkinter.messagebox.showwarning(title="Data not found!", message="User does not exist.")
        MainGUI.start()
    def updateUser():
        SQLConnection = connectmysql.connectToSQL()
        SQLCursor = SQLConnection.cursor()
        firstName = str(contentFName.get())
        lastName = str(contentLName.get())
        emailAdd = str(contentEmail.get())
        password = str(contentPassword.get())
        password = password.encode()
        cipherMode = Fernet(cipherKey)
        encryptedPassword = cipherMode.encrypt(password)
        encryptedPassword = encryptedPassword.decode("utf-8")
        print(encryptedPassword)
        sqlCommand = "UPDATE user SET FirstName='"+firstName+"',LastName='"+lastName+"',EmailAdd='"+emailAdd+"',Password='"+encryptedPassword+"' WHERE UserID= " + current

        if (firstName == "" or lastName == "" or emailAdd == "" or password == ""):
            tkinter.messagebox.showwarning(title="Error!", message="Please fill out all the required information")
        else:
            # encrypting the password
            sqlValues = (firstName, lastName, emailAdd, encryptedPassword)
            SQLCursor.execute(sqlCommand)
            SQLConnection.commit()
            SQLCursor.close()
            SQLConnection.close()
            messagebox.showinfo("Success", "User info has been updated successfully!")
            addWindow.destroy()
            MainGUI.start()

    addButton = tkinter.Button(frameButtons, text="Update", font=("Arial", 15), command=updateUser)
    cancelButton = tkinter.Button(frameButtons, text="Cancel", font=("Arial", 15), command=cancel)
    labelTitle.pack()
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
    cancelButton.pack(side="left")
    labelsa = tkinter.Label(frameButtons, text="   ")
    labelsa.pack(side="left")
    addButton.pack(side="left")
    frameButtons.pack()

