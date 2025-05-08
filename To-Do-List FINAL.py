import tkinter as tk  # Imports tkinter
from tkinter import messagebox, Toplevel  # messagebox for popup warnings, Toplevel for new windows
import webbrowser  # Used to open GitHub link in default web browser

# --- Function to validate task input ---
def validate_input(task):
    if not task.strip():  # If the input is empty or only spaces
        messagebox.showwarning("Input Error", "Task cannot be empty.")  # Show warning
        return False  # Input is invalid
    return True  # Input is valid

# --- Function to add a task to the listbox ---
def add_task():
    task = entry_task.get()  # Get task from entry field
    if validate_input(task):  # Validate input
        listbox_tasks.insert(tk.END, task)  # Add task to the end of the listbox
        entry_task.delete(0, tk.END)  # Clear the entry field after adding

# --- Function to delete the selected task ---
def delete_task():
    try:
        selected = listbox_tasks.curselection()  # Get the index of the selected task
        if not selected:
            raise IndexError  # Raise error if nothing is selected
        listbox_tasks.delete(selected)  # Delete the selected task
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected.")  # Show warning if nothing is selected



# -- Function to Check Items off the list --
def Check_task():
    try:
        selected = listbox_tasks.curselection()
        if not selected:
            raise IndexError
        index = selected[0]
        task_text = listbox_tasks.get(index)

        if task_text.startswith("✔ "):
            # Uncheck the task
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, task_text[2:])
        else:
            # Check the task
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, "✔ " + task_text)
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected.")


# --- Function to close the application ---
def exit_app():
    root.destroy()  # Closes the main window and exits the app

# --- Function to create an "About/User Manual" popup window ---
def open_about_window():
    about_window = Toplevel(root)  # Create a new top-level window
    about_window.title("About")  # Title for the window
    about_window.geometry("300x400")  # Size of the about window

    # Add labels with instructions and information
    tk.Label(about_window, text="To-Do List App v1.0", font=("Helvetica", 12, "bold")).pack(pady=10)
    tk.Label(about_window, text="How to enter Tasks-- Enter your task in the empty bar below the To-Do-List Tasks :) text, and use the following buttons to use the GUI"
                                "\n\nAdd Task- Press this button when you are ready to add your task to the list"
                                "\n\nDelete Task- Press this when you have a selected task you would like to delete"
                                "\n\nExit- Press this when you are finished with your tasks and would like to exit the GUI"
                                "\n\nAbout/User Manual- Used to get here!"
                                "\n\nClick me for my github link!- Click that link for more information on this assignment!"
                                "", wraplength=250).pack(pady=10)

    # Close button for the About window
    tk.Button(about_window, text="Close", command=about_window.destroy).pack(pady=10)

# --- Set up the main GUI window ---
root = tk.Tk()  # Create the main application window
root.title("To-Do List")  # Set the window title
root.geometry("600x600")  # Set the size of the window
root.config(bg="#2c3e50")  # Set the background color

# --- Load image files (replace with actual image paths) ---
task_image = tk.PhotoImage(file="task.png")  # Image for display inside the window
icon_image = tk.PhotoImage(file="icon.png")  # Icon for the window/tab

# --- Title label for the app ---
title_label = tk.Label(root, text="To-Do-List Tasks :)", font=("Helvetica", 16), bg="#2c3e50", fg="white")
title_label.pack(pady=10)  # Add padding above and below the title

# --- Display image (task icon) on the window ---
task_icon_label = tk.Label(root, image=task_image, bg="#2c3e50")
task_icon_label.place(x=50, y=40)  # Position the image on the window

# --- Entry field for typing in new tasks ---
entry_task = tk.Entry(root, width=30, font=("Helvetica", 12), bg="#34495e", fg="white")
entry_task.pack(pady=5)  # Add padding below the entry field

# --- Frame to hold the task control buttons (Add, Delete, Exit) ---
frame_buttons = tk.Frame(root, bg="#2c3e50")  # Create frame with same background color
frame_buttons.pack(pady=10)  # Add padding around the button frame

# --- Add Task button ---
tk.Button(frame_buttons, text="Add Task", width=10, command=add_task, bg="#2980b9", fg="white").grid(row=0, column=0, padx=5)

# --- Delete Task button ---
tk.Button(frame_buttons, text="Delete Task", width=10, command=delete_task, bg="#e74c3c", fg="white").grid(row=0, column=1, padx=5)

# --- Check Task button ---
tk.Button(frame_buttons, text="Check Task", width=10, command=Check_task, bg="#9b59b6", fg="white").grid(row=0, column=2, padx=5)


# --- Exit button ---
tk.Button(frame_buttons, text="Exit", width=10, command=exit_app, bg="#16a085", fg="white").grid(row=0, column=3, padx=5)

# --- About/User Manual button ---
tk.Button(root, text="About/User Manual", command=open_about_window, bg="#f39c12", fg="white").pack(pady=5)

# --- Listbox to display the list of tasks ---
listbox_tasks = tk.Listbox(root, width=40, height=10, bg="#34495e", fg="white")
listbox_tasks.pack(pady=10)

# --- Informational labels at the bottom of the window ---
tk.Label(root, text="For more information, visit my GitHub!", font=("Arial", 9), bg="#2c3e50", fg="white").pack(pady=5)
tk.Label(root, text="Use 'About/User Manual' for project info.", font=("Arial", 9), bg="#2c3e50", fg="white").pack()

# --- Function to open a GitHub link in the default web browser ---
def open_github():
    webbrowser.open("https://github.com/Troublinggem14/Sdev-140-FINAL-PROJECT")

# --- Label that acts as a clickable GitHub link ---
github_label = tk.Label(root, text="Click me for my github link!", font=("Arial", 10, "bold"), fg="white", cursor="hand2", bg="#34495e")
github_label.pack(pady=10)  # Add padding below the link

# --- Bind a mouse click on the label to open the GitHub link, little weird why I have to do this, but it doesn't work unless I do ---
github_label.bind("<Button-1>", lambda e: open_github())

# --- Set the application window icon ---
root.iconphoto(True, icon_image)

# --- Start the main event loop (keeps the window open and responsive) ---
root.mainloop()
