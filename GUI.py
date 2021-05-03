import tkinter as tk
from selenium import webdriver 
import time 


def check_link():
	link = entry_link.get()
	browser = webdriver.Chrome(executable_path = r'C:\Program Files\Google\Chrome\Application\chrome.exe')
	browser.get(link)

	time.sleep(5)
	browser.close()


root = tk.Tk()
root.title('Autofill Form')
root.geometry("+30+30")

#add widget
canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

left_frame = tk.Frame(root, bg= '#adc0d8')
left_frame.place(relx=0, rely=0, relwidth = 0.5, relheight=1)

right_frame = tk.Frame(root, bg = '#c0c0c0')
right_frame.place(relx=0.5, rely=0, relwidth=0.5, relheight=1)

lb_link = tk.Label(left_frame, text = 'link', bg = '#adc0d8', font=("Courier", 14))
lb_link.place(relx=0.05, rely=0.05)

entry_link = tk.Entry(left_frame, font=("Courier", 14))
entry_link.place(relx=0.25, rely=0.05, relwidth = 0.5)

btn_check_link = tk.Button(left_frame, font = ("Courier", 12), text = "Check", command = check_link)
btn_check_link.place(relx = 0.76, rely = 0.05)



root.mainloop()