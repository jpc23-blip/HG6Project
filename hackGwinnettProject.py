from tkinter import *
import customtkinter as ctk

#List of Questions

feat = ["Name", "DOB", "Disease Name", "Symptoms", "Previous Hospitals", "Treatment Experience"]
questList = {}


def createTable():
    print("No Errors!")
    table = ctk.CTkFrame(scroll, border_width = 24, border_color = "orange")
    table.grid(row = 2, column = 0, sticky = "nsew", padx = 24, pady = 24)
    table.grid_columnconfigure(0, weight = 1)

    for i in range(len(feat)):
        label = ctk.CTkLabel(table, text = feat[i], bg_color = "gray").grid(row = 2*i, column = 0)
        if (i > 2):
            answerText = answers[i].get("0.0", "end-1c")
        else:
            answerText = answers[i].get()
        if answerText.strip() == "":
            answerText = "N/A"
        answer = ctk.CTkLabel(table, text = answerText, bg_color = "white", text_color = "black", border_color = "black").grid(row = 1+2*i, column = 0, padx = 24, sticky = "nsew")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

#Creating the 
window = ctk.CTk()
window.title("Prep Time")
window.geometry("1000x800")
window.grid_columnconfigure(0, weight = 1)


title = ctk.CTkLabel(window, text = "Prep Time", text_color = "white")
title.grid(row = 0, column = 0)


scroll = ctk.CTkScrollableFrame(window, width = 1000, height = 750)
scroll.grid(row = 1, column = 0, sticky = "nsew")
scroll.grid_columnconfigure(0, weight = 1)
#Creating the 

enter_button = ctk.CTkButton(scroll, text = "Turn into a Form", text_color = "black", command = createTable)
enter_button.grid(row = 0, column = 0, sticky = "nsew")

form = ctk.CTkFrame(scroll)
form.grid_columnconfigure(1, weight = 1)

featList = {
    "Name": ctk.CTkEntry(form),
    "DOB": ctk.CTkEntry(form),
    "Disease Name": ctk.CTkEntry(form),
    "Symptoms": ctk.CTkTextbox(form),
    "Previous Hospitals": ctk.CTkTextbox(form),
    "Treatment Experience": ctk.CTkTextbox(form)
}

form.grid(row = 1, column = 0, sticky = "nsew", padx = 24, pady = 24)

answers = []
for i in range(len(feat)):
    label = ctk.CTkLabel(form, text = feat[i]).grid(row = i, column = 0)

    answers.append(featList[feat[i]])
    answers[i].grid(row = i, column = 1, padx = 10, pady = 10, sticky = "nsew")

window.mainloop()