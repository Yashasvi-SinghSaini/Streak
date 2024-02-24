from customtkinter import *
import datetime
import pandas
from Scripts import funcs
from PIL import Image
from Scripts import funcs
import playsound

app = CTk()
app.geometry("400x600")
app.wm_title("Streak")
app.iconbitmap("Assets/icon/icon.ico")
app._set_appearance_mode('dark')
set_default_color_theme("green")
streak_img = Image.open('Assets/Images/Streak.png')


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
                playsound.playsound('Assets/sound/click.wav')
                Streak_holder.pack()
        else:
            with open('Assets/data/streak.txt', 'w') as file:
                file.write('0')
                playsound.playsound('Assets/sound/click.wav')
                Streak_holder.pack()
    else:
        error.pack(expand=True, padx=10, pady=(0,5))
        playsound.playsound('Assets/sound/click.wav')


frame_1 = CTkFrame(master=app, fg_color="#347B98", border_width=5)
frame_1.grid(row=0, column=0, rowspan=3, sticky="nsew", padx=50, pady=50)

title = CTkLabel(master=frame_1, text='Did You?', text_color='#ccddff', font=("Commissioner ExtraBold Italic", 30), justify="center")
button = CTkButton(master=frame_1, text="ADD!!!", command=button_func, fg_color='#342309', font=("Commissioner Italic", 15), hover_color='#160f04')
Lecture_check = CTkCheckBox(master=frame_1, text="Lecture", font=("Commissioner Medium Italic", 15), corner_radius=25, fg_color='#FB9902', checkmark_color='#FE2712', text_color='#F7D7D4', checkbox_width=30, hover_color='#FFAF38')
Notes_check = CTkCheckBox(master=frame_1, text="Notes", font=("Commissioner Medium Italic", 15), corner_radius=25, fg_color='#FB9902', checkmark_color='#FE2712', text_color='#F7D7D4', checkbox_width=30, hover_color='#FFAF38')
DPP_check = CTkCheckBox(master=frame_1, text="DPP", font=("Commissioner Medium Italic", 15), corner_radius=25, fg_color='#FB9902', checkmark_color='#FE2712', text_color='#F7D7D4', checkbox_width=30, hover_color='#FFAF38')
Module_check = CTkCheckBox(master=frame_1, text="Module", font=("Commissioner Medium Italic", 15), corner_radius=25, fg_color='#FB9902', checkmark_color='#FE2712', text_color='#F7D7D4', checkbox_width=30, hover_color='#FFAF38')
Matime_check = CTkCheckBox(master=frame_1, text="Matime", font=("Commissioner Medium Italic", 15), corner_radius=25, fg_color='#FB9902', checkmark_color='#FE2712', text_color='#F7D7D4', checkbox_width=30, hover_color='#FFAF38')
Revisathree_check = CTkCheckBox(master=frame_1, text="Revisathree", font=("Commissioner Medium Italic", 15), corner_radius=25, fg_color='#FB9902', checkmark_color='#FE2712', text_color='#F7D7D4', checkbox_width=30, hover_color='#FFAF38')
Streak_holder = CTkLabel(master=frame_1, text=streak, font=("Bungee Spice Regular", 40), image=CTkImage(light_image=streak_img, dark_image=streak_img, size=[100,100]), text_color="#D4DAF7")
error = CTkLabel(master=frame_1, text="You already added your progress\nfor today once", text_color='#b52309', font=('Commissioner Thin', 17))

title.pack(expand=True, pady=(30, 15), padx= 20)
Lecture_check.pack(pady=5, padx=5)
Notes_check.pack(pady=5, padx=5)
DPP_check.pack(pady=5, padx=5)
Module_check.pack(pady=5, padx=5)
Matime_check.pack(pady=5, padx=5)
Revisathree_check.pack(pady=5, padx=5)
Streak_holder.pack()
button.pack(expand=True, fill="both", pady=(30, 10), padx=30)


app.mainloop()
