from customtkinter import *
import datetime
import pandas
from Scripts import funcs
from PIL import Image
from Scripts import funcs

app = CTk()
app.geometry("300x500")
app.wm_title("ReVisor")
#app.iconbitmap("Assets/icon.ico")
app._set_appearance_mode('dark')
set_default_color_theme("green")
streak_img = Image.open('Assets/Images/Streak.png')
streak_img.resize([1000,1000])


with open('Assets/data/streak.txt', 'r') as file:
    streak = int(file.read())

csv=pandas.read_csv('Assets/data/data.csv')
try:
    if csv["Date"][len(csv.index)-2] != str(funcs.daychange(-1)):
        with open('Assets/data/streak.txt', 'w') as file:
            file.write('0')
except KeyError:
    pass

def button_func():
    csv_old=pandas.read_csv('Assets/data/data.csv')

    if csv_old["Date"][len(csv_old.index)-1] != str(datetime.date.today()):
        data={"Date":[datetime.date.today()],
                "Lecture":[Lecture_check.get()],
                "Notes":[Notes_check.get()],
                "DPP":[DPP_check.get()],
                "Module":[Module_check.get()],
                "Matime":[Matime_check.get()],
                "Revisathree":[Revisathree_check.get()]}
        csv_new=pandas.DataFrame(data)
        csv_combined = pandas.concat([csv_old, csv_new])
        csv_combined.to_csv('Assets/data/data.csv', index=False)
        csv_combined = pandas.read_csv('Assets/data/data.csv')
        if csv_combined["Date"][len(csv_combined.index)-2] == str(funcs.daychange(-1)) and csv_combined["Lecture"][len(csv_combined.index)-1] == 1 and csv_combined["Notes"][len(csv_combined.index)-1] == 1 and csv_combined["DPP"][len(csv_combined.index)-1] == 1 and csv_combined["Module"][len(csv_combined.index)-1] == 1 and csv_combined["Matime"][len(csv_combined.index)-1] == 1 and csv_combined["Revisathree"][len(csv_combined.index)-1] == 1:
            with open('Assets/data/streak.txt', 'w') as file:
                global streak
                streak+=1
                file.write(str(streak))
        else:
            with open('Assets/data/streak.txt', 'w') as file:
                file.write('0')            



frame_1 = CTkFrame(master=app, fg_color="#ff9900", border_width=5)
frame_1.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=50, pady=50)

title = CTkLabel(master=frame_1, text='Did You?', text_color='#ccddff', font=("Cascadia Mono SemiBold", 25), justify="center")
button = CTkButton(master=frame_1, text="Add", command=button_func, font=("Cascadia Mono", 15))
Lecture_check = CTkCheckBox(master=frame_1, text="Lecture", font=("Cascadia Mono", 15), corner_radius=20, fg_color='#ff3333', checkmark_color='#66ff33', text_color='#ffe6e6', checkbox_width=30, hover_color='#ff4d4d')
Notes_check = CTkCheckBox(master=frame_1, text="Notes", font=("Cascadia Mono", 15), corner_radius=20, fg_color='#ff3333', checkmark_color='#66ff33', text_color='#ffe6e6', checkbox_width=30, hover_color='#ff4d4d')
DPP_check = CTkCheckBox(master=frame_1, text="DPP", font=("Cascadia Mono", 15), corner_radius=20, fg_color='#ff3333', checkmark_color='#66ff33', text_color='#ffe6e6', checkbox_width=30, hover_color='#ff4d4d')
Module_check = CTkCheckBox(master=frame_1, text="Module", font=("Cascadia Mono", 15), corner_radius=20, fg_color='#ff3333', checkmark_color='#66ff33', text_color='#ffe6e6', checkbox_width=30, hover_color='#ff4d4d')
Matime_check = CTkCheckBox(master=frame_1, text="Matime", font=("Cascadia Mono", 15), corner_radius=20, fg_color='#ff3333', checkmark_color='#66ff33', text_color='#ffe6e6', checkbox_width=30, hover_color='#ff4d4d')
Revisathree_check = CTkCheckBox(master=frame_1, text="Revisathree", font=("Cascadia Mono", 15), corner_radius=20, fg_color='#ff3333', checkmark_color='#66ff33', text_color='#ffe6e6', checkbox_width=30, hover_color='#ff4d4d')
Streak_holder = CTkLabel(master=frame_1, text=streak, image=CTkImage(light_image=streak_img, dark_image=streak_img))

title.pack(expand=True, pady=(30, 15), padx= 20)
Lecture_check.pack(pady=5, padx=5)
Notes_check.pack(pady=5, padx=5)
DPP_check.pack(pady=5, padx=5)
Module_check.pack(pady=5, padx=5)
Matime_check.pack(pady=5, padx=5)
Revisathree_check.pack(pady=5, padx=5)
Streak_holder.pack()
button.pack(expand=True, fill="both", pady=(30, 15), padx=30)


app.mainloop()
