import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import datetime
import time
import threading
import winsound

alarm_ringing = False
stop_alarm_flag = False

def alarm_checker(target_datetime):
    global alarm_ringing, stop_alarm_flag
    while True:
        time.sleep(1)
        if stop_alarm_flag:
            break
            
        current_now = datetime.datetime.now()
        current_str = current_now.strftime("%Y-%m-%d %H:%M")
        
        if current_str == target_datetime:
            alarm_ringing = True
            status_label.config(text="⏰ WAKE UP! Alarm Ringing... ⏰", fg="red")
            while alarm_ringing and not stop_alarm_flag:
                winsound.Beep(2000, 500)
                time.sleep(0.3)
            break

def submit_alarm():
    global stop_alarm_flag, alarm_ringing
    stop_alarm_flag = False
    alarm_ringing = False
    
    year = year_box.get()
    month = month_box.get().zfill(2)
    day = day_box.get().zfill(2)
    h = hour_entry.get().zfill(2)
    m = minute_entry.get().zfill(2)
    
    if not (h.isdigit() and m.isdigit()) or int(h) > 23 or int(m) > 59:
        messagebox.showerror("Error", "Please enter a valid time (00-23 hours, 00-59 minutes).")
        return
        
    target_str = f"{year}-{month}-{day} {h}:{m}"
    
    try:
        target_dt = datetime.datetime.strptime(target_str, "%Y-%m-%d %H:%M")
        if target_dt < datetime.datetime.now():
            messagebox.showwarning("Warning", "The chosen date/time has already passed!")
            return
    except ValueError:
        messagebox.showerror("Error", "Invalid Date combination entered.")
        return
        
    status_label.config(text=f"⏰ Set for: {target_str}", fg="green")
    
    alarm_thread = threading.Thread(target=alarm_checker, args=(target_str,), daemon=True)
    alarm_thread.start()

def stop_alarm():
    global alarm_ringing, stop_alarm_flag
    stop_alarm_flag = True
    alarm_ringing = False
    status_label.config(text="Alarm stopped / deactivated.", fg="gray")

root = tk.Tk()
root.title("Python Advanced Alarm Clock")
root.geometry("400x280")
root.resizable(False, False)

current_date = datetime.datetime.now()

header_label = tk.Label(root, text="Set Alarm Date & Time (24hr format)", font=("Arial", 11, "bold"))
header_label.pack(pady=10)

date_frame = tk.Frame(root)
date_frame.pack(pady=5)

tk.Label(date_frame, text="Year:", font=("Arial", 10)).grid(row=0, column=0, padx=2)
year_box = ttk.Combobox(date_frame, values=[str(y) for y in range(2026, 2031)], width=6, state="readonly")
year_box.set(str(current_date.year))
year_box.grid(row=0, column=1, padx=5)

tk.Label(date_frame, text="Month:", font=("Arial", 10)).grid(row=0, column=2, padx=2)
month_box = ttk.Combobox(date_frame, values=[str(m).zfill(2) for m in range(1, 13)], width=4, state="readonly")
month_box.set(str(current_date.month).zfill(2))
month_box.grid(row=0, column=3, padx=5)

tk.Label(date_frame, text="Day:", font=("Arial", 10)).grid(row=0, column=4, padx=2)
day_box = ttk.Combobox(date_frame, values=[str(d).zfill(2) for d in range(1, 32)], width=4, state="readonly")
day_box.set(str(current_date.day).zfill(2))
day_box.grid(row=0, column=5, padx=5)

time_frame = tk.Frame(root)
time_frame.pack(pady=10)

tk.Label(time_frame, text="Hour (HH):", font=("Arial", 10)).grid(row=0, column=0, padx=2)
hour_entry = tk.Entry(time_frame, width=4, font=("Arial", 12), justify="center")
hour_entry.grid(row=0, column=1, padx=5)
hour_entry.insert(0, current_date.strftime("%H"))

tk.Label(time_frame, text="Minute (MM):", font=("Arial", 10)).grid(row=0, column=2, padx=2)
minute_entry = tk.Entry(time_frame, width=4, font=("Arial", 12), justify="center")
minute_entry.grid(row=0, column=3, padx=5)
minute_entry.insert(0, current_date.strftime("%M"))

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

set_button = tk.Button(button_frame, text="Set Alarm", command=submit_alarm, font=("Arial", 10, "bold"), bg="#4CAF50", fg="white", padx=10)
set_button.grid(row=0, column=0, padx=10)

stop_button = tk.Button(button_frame, text="Stop Alarm", command=stop_alarm, font=("Arial", 10, "bold"), bg="#F44336", fg="white", padx=10)
stop_button.grid(row=0, column=1, padx=10)

status_label = tk.Label(root, text="No active alarm.", font=("Arial", 10, "italic"), fg="gray")
status_label.pack(pady=10)

root.mainloop()