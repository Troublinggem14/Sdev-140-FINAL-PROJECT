import tkinter as tk
from tkinter import messagebox, Toplevel
import webbrowser

# --- input validate function used to tell if the task input is empty, so you can't create empty tasks ---
def validate_input(task):
    if not task.strip():
        messagebox.showwarning("Input Error", "Task cannot be empty.")
        return False
    return True

# --- function used to add tasks by creating listboxes ---
def add_task():
    task = entry_task.get()
    if validate_input(task):
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)

# --- function used to delete tasks, also displays an error if no task is being selected ---
def delete_task():
    try:
        selected = listbox_tasks.curselection()
        if not selected:
            raise IndexError
        listbox_tasks.delete(selected)
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected.")

# --- creates an exit button to leave the to-do-list ---
def exit_app():
    root.destroy()

# --- function to create an about button, that opens the second window needed for the project, just has basic info---
def open_about_window():
    about_window = Toplevel(root)
    about_window.title("About")
    about_window.geometry("300x400")
    tk.Label(about_window, text="To-Do List App v1.0", font=("Helvetica", 12, "bold")).pack(pady=10)
    tk.Label(about_window, text="How to enter Tasks-- Enter your task in the empty bar below the To-Do-List Tasks :) text, and use the following buttons to use the GUI"
                                "\n\nAdd Task- Pess this button when you are ready to add your task to the list"
                                "\n\nDelete Task- Press this when you have a selected task you would like to delete"
                                "\n\nExit- Press this when you are finished with your tasks and would like to exit the GUI"
                                "\n\nAbout/User Manual- Used to get here!"
                                "\n\nClick me for my github link!- Click that link for more information on this assignment!"
                                "", wraplength=250).pack(pady=10)
    tk.Button(about_window, text="Close", command=about_window.destroy).pack(pady=10)

# --- basic GUI Setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x600")

# --- change background color of the main window ---
root.config(bg="#2c3e50")

# --- two images used for the icon in the top right, and the task in the  ---
task_image = tk.PhotoImage(file="task.png")  # Replace with your task image file
icon_image = tk.PhotoImage(file="icon.png")  # Replace with your icon image file

# --- title label with image next to it ---
title_label = tk.Label(root, text="To-Do-List Tasks :)", font=("Helvetica", 16), bg="#2c3e50", fg="white")
title_label.pack(pady=10)

# --- used to add the task.png image in the background ---
task_icon_label = tk.Label(root, image=task_image, bg="#2c3e50")
task_icon_label.place(x=50, y=40)  # Adjust x and y for position


# --- entry box used for inputting tasks ---
entry_task = tk.Entry(root, width=30, font=("Helvetica", 12), bg="#34495e", fg="white")
entry_task.pack(pady=5)

# --- buttons for all the functions above ---
frame_buttons = tk.Frame(root, bg="#2c3e50")
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Add Task", width=10, command=add_task, bg="#2980b9", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Delete Task", width=10, command=delete_task, bg="#e74c3c", fg="white").grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Exit", width=10, command=exit_app, bg="#16a085", fg="white").grid(row=0, column=2, padx=5)
tk.Button(root, text="About/User Manual", command=open_about_window, bg="#f39c12", fg="white").pack(pady=5)

# --- used to create a listbox (the ability to scroll) ---
listbox_tasks = tk.Listbox(root, width=40, height=10, bg="#34495e", fg="white")
listbox_tasks.pack(pady=10)

# ---labels for the text telling you information at the bottom of the window---
tk.Label(root, text="For more information, visit my GitHub!", font=("Arial", 9), bg="#2c3e50", fg="white").pack(pady=5)
tk.Label(root, text="Use 'About/User Manual' for project info.", font=("Arial", 9), bg="#2c3e50", fg="white").pack()

# --- function to open my GitHub link ---
def open_github():
    webbrowser.open("https://github.com/Troublinggem14/Sdev-140-FINAL-PROJECT")

# --- adds a clickable label for the GitHub link ---
github_label = tk.Label(root, text="Click me for my github link!", font=("Arial", 10, "bold"), fg="white", cursor="hand2", bg="#34495e")
github_label.pack(pady=10)

#---  bind the label to open the GitHub link when clicked to allow it to actually open ---
github_label.bind("<Button-1>", lambda e: open_github())

# --- Set the window icon ---
root.iconphoto(True, icon_image)

# --- mainloop ---
root.mainloop()
