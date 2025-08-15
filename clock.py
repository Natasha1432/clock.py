import tkinter as tk 
import time 
def update_clock():     
   current_time = time.strftime("%H:%M:%S %p")                  
   clock_label.config(text=current_time)
   clock_label.after(1000, update_clock) 
root = tk.Tk() 
root.title("Digital clock using python") 
root.geometry("500x250") 
root.resizable(False, False)
root.configure(bg="#000000") 
heading = tk.Label(root, text="TimeWave", font=("DS-Digital", 24, "bold"), fg="#00FF99", bg="#000000") 
heading.pack(pady=10) 
clock_label = tk.Label(root, font=("DS-Digital", 80, "bold"), fg="#00FF00", bg="#000000")
clock_label.pack() 
update_clock() 
root.mainloop()