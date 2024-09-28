from tkinter import *
from tkinter import ttk

# List of options for the Combobox
cb_job = ['Company employee', 'Company executive', 'Student', 'Part-time worker', 'Security guard', 'Other']

# Create the window
root = Tk()

# Specify window size
root.geometry("320x240")

# Specify window title
root.title('Input Form')

frame1 = ttk.Frame(root, padding=(32))
frame1.grid()

# Name
label1 = ttk.Label(frame1, text='Name', padding=(5, 2))
label1.grid(row=0, column=0, sticky=E)

# Address
label2 = ttk.Label(frame1, text='Address', padding=(5, 2))
label2.grid(row=1, column=0, sticky=E)

# Job
label3 = ttk.Label(frame1, text='Job', padding=(5, 2))
label3.grid(row=2, column=0, sticky=E)

# Name input field
name = StringVar()
name_txt = ttk.Entry(
    frame1,
    textvariable=name,
    width=20)
name_txt.grid(row=0, column=1)

# Address input field
address = StringVar()
address_txt = ttk.Entry(
    frame1,
    textvariable=address,
    width=20)
address_txt.grid(row=1, column=1)

# Job selection using Combobox
job = StringVar()
job_cb = ttk.Combobox(
    frame1,
    textvariable=job,
    values=cb_job,
    width=20)
job_cb.set(cb_job[0])  # Set the initial value
job_cb.bind(
    '<<ComboboxSelected>>')
job_cb.grid(row=2, column=1)

# OK Button
button1 = ttk.Button(
    frame1, text='OK',
    command=lambda: print("%s, %s, %s" % (name.get(), address.get(), job.get())))
button1.grid(row=3, column=1)

# Keep the window displayed
root.mainloop()
