import tkinter
from tkinter import ttk
from cryptography.fernet import Fernet
from tkinter.simpledialog import askstring
import connectmysql
import EditGUI
import SearchGUI
import AddGUI
import DeleteGUI

def start():
    mainWindow = tkinter.Tk()
    mainWindow.title("GROUP#9 BSCPE-1D")
    mainWindow.geometry("1000x500")
    mainWindow.resizable("False","False")

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
    center(mainWindow)

    frameButtons = tkinter.Frame(mainWindow, pady=(20))

    def addPage():
        mainWindow.destroy()
        AddGUI.showAddPage()
    def searchPage():
        mainWindow.destroy()
        SearchGUI.showSearchPage()
    def editPage():
        user = askstring('Edit', 'Enter the UserID you want to edit.')
        if(user == ""):
            tkinter.messagebox.showwarning(title="Error!", message="Please enter UserID")
        elif (user==None):
            pass
        else:
            mainWindow.destroy()
            EditGUI.showEditPage(user)
    def deletePage():
        user = askstring('Delete', 'Enter the UserID you want to delete.')
        if (user == ""):
            tkinter.messagebox.showwarning(title="Error!", message="Please enter UserID")
        elif (user==None):
            pass
        else:
            mainWindow.destroy()
            DeleteGUI.showDeletePage(user)
    addButton = tkinter.Button(frameButtons, text="Add User", font=("Arial",15), padx=(15), command=addPage)
    editButton = tkinter.Button(frameButtons, text="Edit User", font=("Arial",15), padx=(15), command=editPage)
    deleteButton = tkinter.Button(frameButtons, text="Delete User", font=("Arial",15), padx=(15), command=deletePage)
    searchButton = tkinter.Button(frameButtons, text="Search User", font=("Arial",15), padx=(10), command=searchPage)


    frameShow = tkinter.Frame(mainWindow)
    def show():
        SQLConnection = connectmysql.connectToSQL()
        SQLCursor = SQLConnection.cursor()
        sqlCommand = "SELECT * FROM user"
        SQLCursor.execute(sqlCommand)
        rows = SQLCursor.fetchall()

        frm = tkinter.Frame(frameShow)
        frm.pack(side=tkinter.LEFT)
        style = ttk.Style()
        style.configure('Treeview.Heading', font=('Calibri', 12, 'bold'),pady=(50))
        tv = ttk.Treeview(frm, columns=("UserID", "FirstName", "LastName", "EmailAdd", "Password"), show="headings",height="25")
        tv.pack()

        rowse = list(rows)
        for column in tv["columns"]:
            tv.column(column, anchor=tkinter.CENTER)  # This will center text in rows
            tv.heading(column, text=column)

        for i in rows:
            cipherKey = "k_5kBfW6Eq4eUEl7FzOZ09eQpJr35yZ6XbSAdVjiS7o="
            cipherMode = Fernet(cipherKey)
            bytePass = str(i[4])
            decryptedPass = cipherMode.decrypt(bytes(bytePass, 'utf-8'))
            decryptedPassword = decryptedPass.decode()

            tv.insert('', 'end', values=(i[0], i[1], i[2], i[3], decryptedPassword))
    show()


    frameButtons.pack()
    frameShow.pack()
    addButton.pack(side="left")
    editButton.pack(side="left")
    deleteButton.pack(side="left")
    searchButton.pack(side="left")
    mainWindow.mainloop()
start()