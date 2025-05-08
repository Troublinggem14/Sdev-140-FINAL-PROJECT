import tkinter as tk  # GUI toolkit
from tkinter import messagebox, Toplevel  # For popup warnings and additional windows
import webbrowser  # To open external URLs (like GitHub)

# --- Function to validate task input ---
def validate_input(task):
    if not task.strip():  # Check if the input is empty or only spaces
        messagebox.showwarning("Input Error", "Task cannot be empty.")  # Show warning popup
        return False  # Invalid input
    return True  # Valid input

# --- Function to add a task to the listbox ---
def add_task():
    task = entry_task.get()  # Get text from the entry field
    if validate_input(task):  # Only proceed if input is valid
        listbox_tasks.insert(tk.END, task)  # Insert task at the end of the list
        entry_task.delete(0, tk.END)  # Clear the entry field after adding

# --- Function to delete the selected task ---
def delete_task():
    try:
        selected = listbox_tasks.curselection()  # Get index of selected task
        if not selected:
            raise IndexError  # Raise error if nothing is selected
        listbox_tasks.delete(selected)  # Remove selected task from the listbox
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected.")  # Show warning if no selection

# --- Function to toggle check/uncheck on tasks ---
def Check_task():
    try:
        selected = listbox_tasks.curselection()  # Get selected task index
        if not selected:  # If no task is selected
            raise IndexError
        index = selected[0]  # Extract the actual index value
        task_text = listbox_tasks.get(index)  # Retrieve the text of the selected task

        if task_text.startswith("\u2714 "):  # If task is already checked (✔ )
            listbox_tasks.delete(index)  # Remove task to update its checked state
            listbox_tasks.insert(index, task_text[2:])  # Re-insert without checkmark
        else:
            listbox_tasks.delete(index)  # Remove task to update its checked state
            listbox_tasks.insert(index, "\u2714 " + task_text)  # Re-insert with checkmark
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected.")  # Warn if no task was selected

# --- Function to exit the application ---
def exit_app():
    root.destroy()  # Close the main application window

# --- Function to open the About/User Manual window ---
def open_about_window():
    about_window = Toplevel(root)  # Create a new pop-up window
    about_window.title("About")  # Set window title
    about_window.geometry("300x400")  # Set fixed window size

    # Labels with app instructions and info
    tk.Label(about_window, text="To-Do List App v1.0", font=("Helvetica", 12, "bold")).pack(pady=10)
    tk.Label(
        about_window,
        text=(
            "How to enter Tasks:\n- Enter your task in the text field.\n"
            "\nAdd Task: Adds your task to the list."
            "\nDelete Task: Deletes the selected task."
            "\nCheck Task: Toggles a checkmark on the selected task."
            "\nExit: Closes the application."
            "\nAbout/User Manual: Opens this window."
            "\nGitHub Link: Opens project page."
        ),
        wraplength=250
    ).pack(pady=10)

    tk.Button(about_window, text="Close", command=about_window.destroy).pack(pady=10)  # Close button

# --- Main application window setup ---
root = tk.Tk()
root.title("To-Do List")
root.geometry("600x600")
root.config(bg="#2c3e50")

# --- Load window images ---
task_image = tk.PhotoImage(file="task.png")  # Main image inside window
icon_image = tk.PhotoImage(file="icon.png")  # App icon image

# --- App title ---
title_label = tk.Label(root, text="To-Do-List Tasks :)", font=("Helvetica", 16), bg="#2c3e50", fg="white")
title_label.pack(pady=10)

# --- Display task image ---
task_icon_label = tk.Label(root, image=task_image, bg="#2c3e50")
task_icon_label.place(x=50, y=40)

# --- Entry field to type tasks ---
entry_task = tk.Entry(root, width=30, font=("Helvetica", 12), bg="#34495e", fg="white")
entry_task.pack(pady=5)

# --- Button container ---
frame_buttons = tk.Frame(root, bg="#2c3e50")
frame_buttons.pack(pady=10)

# --- Task control buttons ---
tk.Button(frame_buttons, text="Add Task", width=10, command=add_task, bg="#2980b9", fg="white").grid(row=0, column=0, padx=5)
tk.Button(frame_buttons, text="Delete Task", width=10, command=delete_task, bg="#e74c3c", fg="white").grid(row=0, column=1, padx=5)
tk.Button(frame_buttons, text="Check Task", width=10, command=Check_task, bg="#9b59b6", fg="white").grid(row=0, column=2, padx=5)
tk.Button(frame_buttons, text="Exit", width=10, command=exit_app, bg="#16a085", fg="white").grid(row=0, column=3, padx=5)

# --- About/User Manual button ---
tk.Button(root, text="About/User Manual", command=open_about_window, bg="#f39c12", fg="white").pack(pady=5)

# --- Task list display area ---
listbox_tasks = tk.Listbox(root, width=40, height=10, bg="#34495e", fg="white")
listbox_tasks.pack(pady=10)

# --- Informational footer ---
tk.Label(root, text="For more information, visit my GitHub!", font=("Arial", 9), bg="#2c3e50", fg="white").pack(pady=5)
tk.Label(root, text="Use 'About/User Manual' for project info.", font=("Arial", 9), bg="#2c3e50", fg="white").pack()

# --- Open GitHub project page in browser ---
def open_github():
    webbrowser.open("https://github.com/Troublinggem14/Sdev-140-FINAL-PROJECT")

# --- GitHub hyperlink label ---
github_label = tk.Label(root, text="Click me for my github link!", font=("Arial", 10, "bold"), fg="white", cursor="hand2", bg="#34495e")
github_label.pack(pady=10)

# Bind click event to GitHub label so it opens the link when clicked
github_label.bind("<Button-1>", lambda e: open_github())

# --- Set the application icon ---
root.iconphoto(True, icon_image)

# --- Run the GUI event loop ---
root.mainloop()
