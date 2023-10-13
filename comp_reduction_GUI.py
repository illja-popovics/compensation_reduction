import tkinter as tk
from tkinter import ttk

def calculate_compensation():
    problem = problem_var.get()
    notification = notification_var.get()
    
    if problem not in ["delay", "cancelation", "denied boarding"]:
        result_label.config(text="Try again")
    else:
        distance = int(distance_var.get())
        delay_at_departure = int(delay_departure_var.get())
        delay_at_arrival = int(delay_arrival_var.get())
        
        if problem == "delay" and delay_at_arrival < 300:
            result_label.config(text="Case not valid, <3h delay")
        elif (notification in ["<7", "0"] and delay_at_departure <= -100) or (notification == "8-14" and delay_at_departure <= -200):
            result_label.config(text="No reduction!")
        elif (problem in ["cancelation", "denied boarding"] and delay_at_arrival < 200) or (problem in ["cancelation", "denied boarding"] and notification == "8-14" and delay_at_arrival < 400):
            result_label.config(text="Case not valid! Delay at arrival is not sufficient")
        elif distance >= 3500 and delay_at_arrival < 400:
            result_label.config(text="50% reduction, reduce 600 to 300")
        elif distance >= 1500 and delay_at_arrival < 300:
            result_label.config(text="50% reduction, reduce 400 to 200")
        else:
            result_label.config(text="No reduction")

def select_problem(selected_problem):
    problem_var.set(selected_problem)

def select_notification(selected_notification):
    notification_var.set(selected_notification)

app = tk.Tk()
app.title("Compensation Reduction Calculator")

style = ttk.Style()
style.theme_use("alt")  

problem_var = tk.StringVar()
notification_var = tk.StringVar()
distance_var = tk.StringVar()
delay_departure_var = tk.StringVar()
delay_arrival_var = tk.StringVar()

frame = ttk.Frame(app, padding=10)
frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))

problem_label = ttk.Label(frame, text="Select type of incident:")
problem_label.grid(column=0, row=0, padx=5, pady=5)

problem_buttons_frame = ttk.Frame(frame)
problem_buttons_frame.grid(column=1, row=0, padx=5, pady=5)

delay_button = ttk.Button(problem_buttons_frame, text="Delay", command=lambda: select_problem("delay"))
cancelation_button = ttk.Button(problem_buttons_frame, text="Cancelation", command=lambda: select_problem("cancelation"))
denied_boarding_button = ttk.Button(problem_buttons_frame, text="Denied Boarding", command=lambda: select_problem("denied boarding"))

delay_button.grid(column=0, row=0, padx=5)
cancelation_button.grid(column=1, row=0, padx=5)
denied_boarding_button.grid(column=2, row=0, padx=5)

notification_label = ttk.Label(frame, text="Select notification period:")
notification_label.grid(column=0, row=1, padx=5, pady=5)

notification_buttons_frame = ttk.Frame(frame)
notification_buttons_frame.grid(column=1, row=1, padx=5, pady=5)

notification_below_seven_button = ttk.Button(notification_buttons_frame, text="<7", command=lambda: select_notification("<7"))
notification_8_14_button = ttk.Button(notification_buttons_frame, text="8-14", command=lambda: select_notification("8-14"))
notification_delay_no_notification_button = ttk.Button(notification_buttons_frame, text="Delay, no notification", command=lambda: select_notification("0"))

notification_below_seven_button.grid(column=0, row=0, padx=5)
notification_8_14_button.grid(column=1, row=0, padx=5)
notification_delay_no_notification_button.grid(column=2, row=0, padx=5)

distance_label = ttk.Label(frame, text="Distance in KM:")
distance_label.grid(column=0, row=2, padx=5, pady=5)
distance_entry = ttk.Entry(frame, textvariable=distance_var)
distance_entry.grid(column=1, row=2, padx=5, pady=5)

delay_departure_label = ttk.Label(frame, text="Delay at departure (format like -0100, 0130):")
delay_departure_label.grid(column=0, row=3, padx=5, pady=5)
delay_departure_entry = ttk.Entry(frame, textvariable=delay_departure_var)
delay_departure_entry.grid(column=1, row=3, padx=5, pady=5)

delay_arrival_label = ttk.Label(frame, text="Delay at arrival (format like 0310,0100):")
delay_arrival_label.grid(column=0, row=4, padx=5, pady=5)
delay_arrival_entry = ttk.Entry(frame, textvariable=delay_arrival_var)
delay_arrival_entry.grid(column=1, row=4, padx=5, pady=5)

calculate_button = ttk.Button(frame, text="Calculate Compensation", command=calculate_compensation)
calculate_button.grid(column=0, row=5, columnspan=2, pady=10)

result_label = ttk.Label(frame, text="Result will be displayed here")
result_label.grid(column=0, row=6, columnspan=2, padx=5, pady=5)

app.mainloop()
