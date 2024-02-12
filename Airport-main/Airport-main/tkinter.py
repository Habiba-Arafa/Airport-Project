import tkinter
from tkinter import ttk
from tkinter import messagebox
import os
import openpyxl

all_data = []
airportname = []
countryname = []
date = []


def read_airport():
    file = open("datafinal2.txt", "r")

    for line in file:
        vals = line.split(",")

        x = dict(country_name=vals[0], airport_name=vals[1], x=vals[2], y=vals[3], date=vals[4])

        all_data.append(x)
        airportname.append(vals[1])
        countryname.append(vals[0])
        date.append(vals[4])


read_airport()


def enter_data():
    accepted = accept_var.get()

    if accepted == "Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        phone_number = phone_entry.get()
        email = email_entry.get()
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()

            # airport info
            vaccination_status = vac_status_var.get()
            numpassengers = numpassengers_spinbox.get()
            country1 = country1_combobox.get()
            country2 = country2_combobox.get()
            airport1 = airport1_combobox.get()
            airport2 = airport1_combobox.get()
            date = date_combobox.get()
            airportclass = airportclass_combobox.get()

            meal = meal_combobox.get()

            print("First name: ", firstname, "Last name: ", lastname)
            print("phone number: ", phone_number)
            print("email: ", email)
            print('country1: ', country1)
            print('country2', country2)
            print('first airport', airport1)
            print('first airport', airport2)
            print('available date:', date)
            print("class:", airportclass)
            print("number of passengers: ", numpassengers)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("the meal is :", meal)
            print("vaccination status", vaccination_status)
            print("------------------------------------------")
            filepath = "E:\OneDrive\Desktop\loc.xlsx"

            if not os.path.exists(filepath):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["First Name", "Last Name", "Title", "Age", "Nationality", 'email', 'numpassengers', "meal",
                           "date", "airport1", "airport2", "airportclass", "vaccination status"]
                sheet.append(heading)
                workbook.save(filepath)
            workbook = openpyxl.load_workbook(filepath)
            sheet = workbook.active
            sheet.append(
                [firstname, lastname, title, age, nationality, email, numpassengers, meal, date, airport1, airport2,
                 airportclass, vaccination_status])
            workbook.save(filepath)

        else:
            tkinter.messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        tkinter.messagebox.showwarning(title="Error", message="You have not accepted the terms")


window = tkinter.Tk(className='Python Examples - Window Color')

window.title("Data Entry Form")
window.geometry("650x650")
frame = tkinter.Frame(window)
window['background'] = '#B0D2F1'

frame.pack()

# Saving User Info
user_info_frame = tkinter.LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name")
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name")
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

phone_label = tkinter.Label(user_info_frame, text="phone number")
phone_label.grid(row=2, column=1)
phone_entry = tkinter.Entry(user_info_frame)
phone_entry.grid(row=3, column=1)

email_label = tkinter.Label(user_info_frame, text="email")
email_label.grid(row=2, column=0)
email_entry = tkinter.Entry(user_info_frame)
email_entry.grid(row=3, column=0)

title_label = tkinter.Label(user_info_frame, text="Title")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=4, column=0)
age_spinbox.grid(row=5, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame,
                                    values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania",
                                            "South America"])
nationality_label.grid(row=4, column=1)
nationality_combobox.grid(row=5, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# passenger Information
data_frame = tkinter.LabelFrame(frame)
data_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

vaccinated_label = tkinter.Label(data_frame)

vac_status_var = tkinter.StringVar(value="Not vaccinated")
vaccination_check = tkinter.Checkbutton(data_frame, text="vaccinated",
                                        variable=vac_status_var, onvalue="VACCINATED", offvalue="Not VACCINATED")

vaccinated_label.grid(row=6, column=0)
vaccination_check.grid(row=7, column=0)

numpassengers_spinbox = tkinter.Spinbox(data_frame, from_=0, to=20)
numpassengers_label = tkinter.Label(data_frame, text="Number of passengers")
numpassengers_label.grid(row=0, column=0)
numpassengers_spinbox.grid(row=1, column=0)

for i in range(len(countryname)):
    country1_label = tkinter.Label(data_frame, text="From")
    country1_combobox = ttk.Combobox(data_frame, values=countryname[1:])
    country1_label.grid(row=0, column=1)
    country1_combobox.grid(row=1, column=1)

    country2_label = tkinter.Label(data_frame, text="To")
    country2_combobox = ttk.Combobox(data_frame, values=countryname[1:])
    country2_label.grid(row=0, column=2)
    country2_combobox.grid(row=1, column=2)

for i in range(len(countryname)):
    airport1_label = tkinter.Label(data_frame, text="First Airport ")
    airport1_combobox = ttk.Combobox(data_frame, values=airportname[1:])
    airport1_label.grid(row=2, column=0)
    airport1_combobox.grid(row=3, column=0)

    airport2_label = tkinter.Label(data_frame, text="Second Airport")
    airport2_combobox = ttk.Combobox(data_frame, values=airportname[1:5])
    airport2_label.grid(row=2, column=1)
    airport2_combobox.grid(row=3, column=1)

date_label = tkinter.Label(data_frame, text="Available date")
date_combobox = ttk.Combobox(data_frame, values=['28/03/2023', '28/04/2023', '28/05/2023', '28/06/2023'])
date_label.grid(row=4, column=0)
date_combobox.grid(row=5, column=0)

meal_label = tkinter.Label(data_frame, text="Available meal")
meal_combobox = ttk.Combobox(data_frame, values=['Fish', "Meat", "Chicken"])
meal_label.grid(row=2, column=2)
meal_combobox.grid(row=3, column=2)

airportclass_label = tkinter.Label(data_frame, text="Airport Class")
airportclass_combobox = ttk.Combobox(data_frame, values=["Economy", "Business"])
airportclass_label.grid(row=4, column=1)
airportclass_combobox.grid(row=5, column=1)

for widget in data_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions")
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text="I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted")
terms_check.grid(row=0, column=0)

# Button
button = tkinter.Button(frame, text="submit", command=enter_data, fg='white', bg='#1687ED')
button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

window.mainloop()
