from tkinter import *
from tkinter import messagebox
from db import  Database

db = Database('students.db')


def show_student():
    student_list.delete(0,END)
    for row in db.fetch():
        student_list.insert(END, row)

def add_student():
    if part_text.get() == '' or student_text.get() == '' or Unversity_text.get() == '' or am_text.get() == '':
        messagebox.showerror('Required Fields', 'Please fill all fields')
        return
    db.insert(part_text.get(), student_text.get(),Unversity_text.get(),am_text.get())
    student_list.delete(0,END)
    student_list.insert(END,(part_text.get(), student_text.get(),Unversity_text.get(),am_text.get()))
    clear_student()
    show_student()


def select_item(event):
    try:
        global selected_item
        index = student_list.curselection()[0]
        selected_item = student_list.get(index)

        print(index)


        part_entry.delete(0,END)
        part_entry.insert(END,selected_item[1])
        student_entry.delete(0, END)
        student_entry.insert(END, selected_item[2])
        am_entry.delete(0, END)
        am_entry.insert(END, selected_item[4])
        Unversity_entry.delete(0, END)
        Unversity_entry.insert(END, selected_item[3])

    except IndexError:
        pass

def remove_student():
    db.remove(selected_item[0])
    clear_student()
    show_student()



def update_student():
    db.update(selected_item[0], part_text.get(), student_text.get(),Unversity_text.get(),am_text.get())
    show_student()

def clear_student():
    part_entry.delete(0, END)
    student_entry.delete(0, END)
    am_entry.delete(0, END)
    Unversity_entry.delete(0, END)



#Create Window
app = Tk()

#part
part_text= StringVar()
part_label = Label(app,text='Student Last Name', font=('bold,14'), pady=20)
part_label.grid(row=0, column=0, sticky=W)
part_entry = Entry(app, textvariable=part_text)
part_entry.grid(row=0, column=1)

#Student
student_text= StringVar()
student_label = Label(app,text='Student First Name', font=('bold,14'))
student_label.grid(row=0, column=2, sticky=W)
student_entry = Entry(app, textvariable=student_text)
student_entry.grid(row=0, column=3)


am_text= StringVar()
am_label = Label(app,text='Serial Tag', font=('bold,14'), pady=20)
am_label.grid(row=1, column=0, sticky=W)
am_entry = Entry(app, textvariable=am_text)
am_entry.grid(row=1, column=1)

Unversity_text= StringVar()
Unversity_label = Label(app,text='University Name', font=('bold,14'), pady=20)
Unversity_label.grid(row=1, column=2, sticky=W)
Unversity_entry = Entry(app, textvariable=Unversity_text)
Unversity_entry.grid(row=1, column=3)


student_list= Listbox(app, height=10, width=70, border=0)
student_list.grid(row=3,column=0,columnspan=3,rowspan=3,pady=20,padx=20)

#CREATE SCROLLBAR

scrollbar= Scrollbar(app)
scrollbar.grid(row=3,column=3)

#Bind select
student_list.bind('<<ListboxSelect>>', select_item)
#set scroll to listbox

student_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=student_list.yview)

#buttons

add_btn = Button(app, text='Add student', width=12, command=add_student)
add_btn.grid(row=2,column=0,padx=20)

remove_btn = Button(app, text='Remove student', width=12, command=remove_student)
remove_btn.grid(row=2,column=1)

update_btn = Button(app, text='Update student', width=12, command=update_student)
update_btn.grid(row=2,column=2)

clear_btn = Button(app, text='Clear Entries', width=12, command=clear_student)
clear_btn.grid(row=2,column=3)

#show_students
show_student()

app.title('Student Manager')

app.geometry('700x400')

#start programm
app.mainloop()