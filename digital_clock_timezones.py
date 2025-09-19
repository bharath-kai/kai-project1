import tkinter as tk
from datetime import datetime
import pytz

# List of time zones to display
TIMEZONES = [
    ('UTC', 'UTC'),
    ('New York', 'America/New_York'),
    ('London', 'Europe/London'),
    ('Paris', 'Europe/Paris'),
    ('India', 'Asia/Kolkata'),
    ('Tokyo', 'Asia/Tokyo'),
]

def update_time():
    for label, zone in labels:
        tz = pytz.timezone(zone)
        current_time = datetime.now(tz).strftime('%H:%M:%S')
        label.config(text=current_time)
    root.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock - Multiple Time Zones")
root.geometry("350x220")
root.resizable(False, False)

labels = []
for city, zone in TIMEZONES:
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=5)
    tk.Label(frame, text=city, font=('Arial', 14, 'bold'), width=10, anchor='w').pack(side=tk.LEFT)
    time_label = tk.Label(frame, text="", font=('Arial', 14), width=10, anchor='e')
    time_label.pack(side=tk.LEFT, padx=10)
    labels.append((time_label, zone))

update_time()
root.mainloop()