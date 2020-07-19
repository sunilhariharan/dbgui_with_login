from tkinter import *
import os
 
creds = 'tempfile.temp' # This just sets the variable creds to 'tempfile.temp'

from PIL import Image,ImageTk
import sqlite3







conn=sqlite3.connect('applications_issues.db')
c=conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS issues(
         name text,
         app text,
         issue text,
         solution text
         )""")
         
def Signup(): # This is the signup definition, 
    global pwordE # These globals just make the variables global to the entire script, meaning any definition can use them
    global nameE
    global roots
 
    roots = Tk() # This creates the window, just a blank one.
    roots.title('Signup') # This renames the title of said window to 'signup'
    intruction = Label(roots, text='Please Enter new Credidentials\n') # This puts a label, so just a piece of text saying 'please enter blah'
    intruction.grid(row=0, column=0, sticky=E) # This just puts it in the window, on row 0, col 0. If you want to learn more look up a tkinter tutorial :)
 
    nameL = Label(roots, text='New Username: ') # This just does the same as above, instead with the text new username.
    pwordL = Label(roots, text='New Password: ') # ^^
    nameL.grid(row=1, column=0, sticky=W) # Same thing as the instruction var just on different rows. :) Tkinter is like that.
    pwordL.grid(row=2, column=0, sticky=W) # ^^
 
    nameE = Entry(roots) # This now puts a text box waiting for input.
    pwordE = Entry(roots, show='*') # Same as above, yet 'show="*"' What this does is replace the text with *, like a password box :D
    nameE.grid(row=1, column=1) # You know what this does now :D
    pwordE.grid(row=2, column=1) # ^^
 
    signupButton = Button(roots, text='Signup', command=FSSignup) # This creates the button with the text 'signup', when you click it, the command 'fssignup' will run. which is the def
    signupButton.grid(columnspan=2, sticky=W)
    roots.mainloop() # This just makes the window keep open, we will destroy it soon
 
def FSSignup():
    with open(creds, 'w') as f: # Creates a document using the variable we made at the top.
        f.write(nameE.get()) # nameE is the variable we were storing the input to. Tkinter makes us use .get() to get the actual string.
        f.write('\n') # Splits the line so both variables are on different lines.
        f.write(pwordE.get()) # Same as nameE just with pword var
        f.close() # Closes the file
 
    roots.destroy() # This will destroy the signup window. :)
    Login() # This will move us onto the login definition :D
 
def Login():
    global nameEL
    global pwordEL # More globals :D
    global rootA
 
    rootA = Tk() # This now makes a new window.
    rootA.title('Login') # This makes the window title 'login'
 
    intruction = Label(rootA, text='Please Login\n') # More labels to tell us what they do
    intruction.grid(sticky=E) # Blahdy Blah
 
    nameL = Label(rootA, text='Username: ') # More labels
    pwordL = Label(rootA, text='Password: ') # ^
    nameL.grid(row=1, sticky=W)
    pwordL.grid(row=2, sticky=W)
 
    nameEL = Entry(rootA) # The entry input
    pwordEL = Entry(rootA, show='*')
    nameEL.grid(row=1, column=1)
    pwordEL.grid(row=2, column=1)
 
    loginB = Button(rootA, text='Login', command=CheckLogin) # This makes the login button, which will go to the CheckLogin def.
    loginB.grid(columnspan=2, sticky=W)
 

    rootA.mainloop()
 
def CheckLogin():
    with open(creds) as f:
        data = f.readlines() # This takes the entire document we put the info into and puts it into the data variable
        uname = data[0].rstrip() # Data[0], 0 is the first line, 1 is the second and so on.
        pword = data[1].rstrip() # Using .rstrip() will remove the \n (new line) word from before when we input it
 
    if nameEL.get() == uname and pwordEL.get() == pword: # Checks to see if you entered the correct data.
        global root
        root=Tk()
        root.title('gui for db')
        root.iconbitmap('codemy.ico')
        root.geometry("400x400")



     
        name=Entry(root,width=30)
        name.grid(row=0,column=1,padx=20,pady=(10,0))

        app=Entry(root,width=30)
        app.grid(row=1,column=1,padx=20)

        issue=Entry(root,width=30)
        issue.grid(row=2,column=1,padx=20)

        solution=Entry(root,width=30)
        solution.grid(row=3,column=1,padx=20)

        delete_box=Entry(root,width=30)
        delete_box.grid(row=7,column=1)

        name_label=Label(root,text='Name')
        name_label.grid(row=0,column=0,pady=(10,0))

        app_label=Label(root,text='app')
        app_label.grid(row=1,column=0)

        issue_label=Label(root,text='issue')
        issue_label.grid(row=2,column=0)

        solution_label=Label(root,text='solution')
        solution_label.grid(row=3,column=0)

        delete_box_label=Label(root,text="Select ID")
        delete_box_label.grid(row=7,column=0)

        
        submit_button=Button(root,text="Add Record To Database",command=submit)
        submit_button.grid(row=4,column=0,columnspan=2,pady=10,padx=10,ipadx=100)

        query_button=Button(root,text="Show Records",command=query)
        query_button.grid(row=5,column=0,columnspan=2,pady=10,padx=10,ipadx=137)

        delete_button=Button(root,text="Delete Record",command=delete)
        delete_button.grid(row=8,column=0,columnspan=2,pady=10,padx=10,ipadx=136)
        root.mainloop()
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()

    
def submit():
    conn=sqlite3.connect('applications_issues.db')
    c=conn.cursor()
    c.execute("INSERT INTO issues VALUES (:name,:app,:issue,:solution)",
         {
             'name':name.get(),
             'app':app.get(),
             'issue':issue.get(),
             'solution':solution.get(),
         })
    conn.commit()
    conn.close()
    name.delete(0,END)
    app.delete(0,END)
    issue.delete(0,END)
    solution.delete(0,END)
    
def delete():
    conn=sqlite3.connect('applications_issues.db')
    c=conn.cursor()
    c.execute("DELETE FROM issues WHERE oid="+delete_box.get())
    conn.commit()
    conn.close()


def query():
    conn=sqlite3.connect('applications_issues.db')
    c=conn.cursor()
    c.execute("SELECT *, oid FROM issues")
    records=c.fetchall()
    print(records)
    print_records=''
    for record in records:
        print_records+=str(record[0]) + " "+str(record[1]) + " "+str(record[2]) + " "+str(record[3]) + " "+str(record[4])+"\n"
    query_label=Label(root,text=print_records)
    query_label.grid(row=6,column=0,columnspan=2)
    conn.commit()
    conn.close()

conn.commit()
conn.close()

if os.path.isfile(creds):
    Login()
else: # This if else statement checks to see if the file exists. If it does it will go to Login, if not it will go to Signup :)
    Signup()
