import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry_task.get()
    if task:
        tasks.append((task, False))
        set_listbox_display()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        del tasks[index]
        set_listbox_display()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete")

def toggle_completion():
    try:
        index = listbox_tasks.curselection()[0]
        task, completed = tasks[index]
        tasks[index] = (task, not completed)
        set_listbox_display()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed")

def update_task():
    try:
        index = listbox_tasks.curselection()[0]
        task, _ = tasks[index]
        new_task = entry_task.get()
        tasks[index] = (new_task, False)
        set_listbox_display()
        entry_task.delete(0, tk.END)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update")

def set_listbox_display():
    listbox_tasks.delete(0, tk.END)
    for task, completed in tasks:
        if completed:
            listbox_tasks.insert(tk.END, f"✓ {task}")
        else:
            listbox_tasks.insert(tk.END, f"✗ {task}")

root = tk.Tk()
root.title("To-Do List")
root.geometry("900x500")
root.configure(background="LIGHT GREEN")

tasks = []

frame_tasks = tk.Frame(root, width=600, height=300)
frame_tasks.pack(pady=20)

listbox_tasks = tk.Listbox(frame_tasks, height=15, width=105)
listbox_tasks.pack(side=tk.LEFT)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=110)
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task  ", command=add_task, width=20, height=2)
button_add_task.place(x=310, y=350)

button_toggle_completion = tk.Button(root, text="Mark as Complete", command=toggle_completion, width=20, height=2)
button_toggle_completion.place(x=490, y=400)

button_update_task = tk.Button(root, text="Update Task", command=update_task, width=20, height=2)
button_update_task.place(x=310, y=400)

button_delete_task = tk.Button(root, text="Delete Task", command=delete_task, width=20, height=2)
button_delete_task.place(x=490, y=350)

set_listbox_display()

root.mainloop()
