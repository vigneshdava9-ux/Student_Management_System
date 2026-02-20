import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Management System")
root.geometry("600x500")

def add_student():
    name = name_entry.get()
    age = age_scale.get()
    course = course_entry.get()
    gender = gender_var.get()

    if name == "" or course == "" or gender == "":
        messagebox.showwarning("Input Error", "Please fill all fields")
        return

    student_info = f"Name:{name} | Age:{age} | Course:{course} | Gender:{gender}"
    listbox.insert(tk.END, student_info)

    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    gender_var.set("")

def delete_student():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
    else:
        messagebox.showwarning("Selection Error", "Please select a student to delete")

title_label = tk.Label(root, text="Student Management System", font=("Arial", 16))
title_label.pack(pady=10)

frame = tk.Frame(root)
frame.pack(pady=10)

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame, text="Age").grid(row=1, column=0, padx=5, pady=5)
age_scale = tk.Scale(frame, from_=1, to=100, orient=tk.HORIZONTAL)
age_scale.set(30)
age_scale.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame, text="Course").grid(row=2, column=0, padx=5, pady=5)
course_entry = tk.Entry(frame)
course_entry.grid(row=2, column=1, padx=5, pady=5)

tk.Label(frame, text="Gender").grid(row=3, column=0, padx=5, pady=5)
gender_var = tk.StringVar()

male_radio = tk.Radiobutton(frame, text="Male", variable=gender_var, value="Male")
male_radio.grid(row=3, column=1, sticky="w")

female_radio = tk.Radiobutton(frame, text="Female", variable=gender_var, value="Female")
female_radio.grid(row=3, column=1, sticky="e")

add_button = tk.Button(root, text="Add Student", command=add_student)
add_button.pack(pady=10)

listbox = tk.Listbox(root, width=80, height=15)
listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Selected", command=delete_student)
delete_button.pack(pady=10)

root.mainloop()
