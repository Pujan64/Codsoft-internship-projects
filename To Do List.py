import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
import threading

# Main application window
root = tk.Tk()
root.title("To-Do List Application")
root.geometry("600x700")  # Increased width for better centering
root.configure(bg="#F5F5F5")  # Light background for an aesthetic look

# List to hold tasks with timestamps
tasks = []

# Function to update the task list display
def update_task_list():
    task_list.delete(0, tk.END)
    for task, timestamp in tasks:
        task_list.insert(tk.END, f"{task:<40} {timestamp}")  # Align task and timestamp

# Function to add a new task
def add_task():
    task = task_entry.get()
    if task and task != "Enter a task":  # Ensure valid input
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        tasks.append((task, timestamp))
        update_task_list()
        task_entry.delete(0, tk.END)
        task_entry.insert(0, "Enter a task")  # Reset placeholder
    else:
        messagebox.showwarning("Warning", "Please enter a task before adding!")

# Function to delete the selected task
def delete_task():
    try:
        selected_index = task_list.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# Function to clear all tasks
def clear_tasks():
    confirm = messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks?")
    if confirm:
        tasks.clear()
        update_task_list()

# Function to show the real-time clock
def update_clock():
    while True:
        current_time = time.strftime("%Y-%m-%d %H:%M:%S")
        clock_label.config(text=f"Current Time: {current_time}")
        time.sleep(1)

# Start the clock in a separate thread
def start_clock():
    threading.Thread(target=update_clock, daemon=True).start()

# Function to add placeholder behavior in the entry box
def set_placeholder(event):
    if task_entry.get() == "":
        task_entry.insert(0, "Enter a task")
        task_entry.config(fg="#888888")  # Gray text for placeholder

def remove_placeholder(event):
    if task_entry.get() == "Enter a task":
        task_entry.delete(0, tk.END)
        task_entry.config(fg="#333333")  # Normal text color

# Title at the top
title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 40, "bold"), fg="#333333", bg="#F5F5F5")
title_label.pack(pady=(10, 0))

# Clock label
clock_label = tk.Label(root, font=("Helvetica", 14), fg="#333333", bg="#F5F5F5")
clock_label.pack(pady=10)

# Centered content frame
content_frame = tk.Frame(root, bg="#F5F5F5", padx=40, pady=10)  # Added padding for centering
content_frame.pack(fill=tk.BOTH, expand=True)

# Entry field for task input with placeholder
task_entry = tk.Entry(content_frame, font=("Helvetica", 14), bg="#FFFFFF", fg="#888888")
task_entry.insert(0, "Enter a task")
task_entry.bind("<FocusIn>", remove_placeholder)
task_entry.bind("<FocusOut>", set_placeholder)
task_entry.pack(pady=10, fill=tk.X)

# Buttons with aesthetic color scheme
add_button = tk.Button(content_frame, text="Add Task", command=add_task, font=("Arial", 15,"bold"), width=15, height=2, bg="#4CC9FE", fg="white", padx=20, pady=10, relief="flat")
add_button.pack(pady=(10, 5))

delete_button = tk.Button(content_frame, text="Delete Task", command=delete_task, font=("Arial", 15,"bold"), width=15, height=2, bg="#4CC9FE", fg="white" , padx=20, pady=10,relief="flat" )
delete_button.pack(pady=(5, 5))

clear_button = tk.Button(content_frame, text="Clear All Tasks", command=clear_tasks, font=("Arial", 15,"bold"), width=15, height=2, bg="#4CC9FE", fg="white", padx=20, pady=10,relief="flat")
clear_button.pack(pady=(5, 10))

# Headers for the task and time columns
header_frame = tk.Frame(content_frame, bg="#F5F5F5")
header_frame.pack(fill=tk.X, pady=(10, 0))

task_label = tk.Label(header_frame, text="Tasks", font=("Helvetica", 12, "bold"), fg="#333333", bg="#F5F5F5", anchor="w")
task_label.pack(side=tk.LEFT, padx=(10, 0))

time_label = tk.Label(header_frame, text="Time", font=("Helvetica", 12, "bold"), fg="#333333", bg="#F5F5F5", anchor="e")
time_label.pack(side=tk.RIGHT, padx=(0, 10))

# Listbox to display tasks and timestamps
task_list = tk.Listbox(content_frame, font=("Helvetica", 12), height=15, selectmode=tk.SINGLE, bg="#FFFFFF", fg="#333333")
task_list.pack(pady=10, fill=tk.BOTH, expand=True)

start_clock()
# Run the application
root.mainloop()
