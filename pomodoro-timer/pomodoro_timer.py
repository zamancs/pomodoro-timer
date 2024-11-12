import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

WORK_TIME = 25 * 60
SHORT_BREAK_TIME = 5 * 60
LONG_BREAK_TIME = 15 * 60
time_left = WORK_TIME
timer_running = False

def update_display():
    minutes, seconds = divmod(time_left, 60)
    timer_label.config(text=f"{minutes:02}:{seconds:02}")
    progress["value"] = progress["maximum"] - time_left

def start_timer():
    global timer_running, time_left
    if not timer_running:
        timer_running = True
        time_left = WORK_TIME
        progress["maximum"] = WORK_TIME
        run_timer()

def set_break(duration):
    global timer_running, time_left
    if not timer_running:
        timer_running = True
        time_left = duration
        progress["maximum"] = duration
        run_timer()

def reset_timer():
    global timer_running, time_left
    timer_running = False
    time_left = WORK_TIME
    update_display()

def run_timer():
    global time_left, timer_running
    if timer_running and time_left > 0:
        minutes, seconds = divmod(time_left, 60)
        timer_label.config(text=f"{minutes:02}:{seconds:02}")
        progress["value"] = progress["maximum"] - time_left
        time_left -= 1
        root.after(1000, run_timer)
    else:
        timer_running = False
        messagebox.showinfo("Session Complete", "Time's up! Take a break or get back to work.")
        update_display()

root = tk.Tk()
root.title("Pomodoro Timer")
root.geometry("500x400")
root.configure(bg="#2E3440")

tk.Label(root, text="Pomodoro Timer", font=("Helvetica", 28, "bold"), fg="#FFFFFF", bg="#2E3440").pack(pady=20)
timer_label = tk.Label(root, text="25:00", font=("Helvetica", 54, "bold"), fg="#D08770", bg="#2E3440")
timer_label.pack()
progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate", maximum=WORK_TIME)
progress.pack(pady=20)
button_frame = tk.Frame(root, bg="#2E3440")
button_frame.pack(pady=10)

def create_button(text, command, color, col):
    tk.Button(button_frame, text=text, command=command, bg=color, fg="#2E3440", padx=12, pady=8).grid(row=0, column=col, padx=10, pady=10)

create_button("Start", start_timer, "#A3BE8C", 0)
create_button("Short Break", lambda: set_break(SHORT_BREAK_TIME), "#88C0D0", 1)
create_button("Long Break", lambda: set_break(LONG_BREAK_TIME), "#5E81AC", 2)
create_button("Reset", reset_timer, "#BF616A", 3)

root.mainloop()