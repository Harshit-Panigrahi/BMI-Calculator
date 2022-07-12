from tkinter import *

window = Tk()

window.title("BMI Calculator")
window.geometry("400x400")
window.configure(bg = "lightcyan")

def calculate_bmi():
  weight = int(weight_entry.get())
  height = int(height_entry.get()) / 100
  bmi = weight / (height * height)
  bmi = round(bmi, 1)
  name = username.get()

  result_label.destroy()

  msg = ""
  if bmi < 18.5:
    msg = " you are underweight"
  elif bmi > 18.5 and bmi <= 24.9:
    msg = " you are in the normal range"
  elif bmi > 25 and bmi <= 29.9:
    msg = " you are overweight"
  elif bmi > 30:
    msg = " you are obese"
  else:
    msg = " Something went wrong"
  output_label = Label(result_frame, text = name + ", your BMI is " + str(bmi) + " and" + msg + ".", bg = "lightcyan", font=("Arial", 15), width = 45)
  output_label.place(x = 20, y = 20)
  output_label.pack()

app_label = Label(window, text = "BMI Calculator", bg = "lightcyan", font = ("Arial", 20), bd = 15)
app_label.place(x=90, y=20)

name_label = Label(window, text="Your Name: ", bg="lightcyan", font=("Arial", 15), bd=5)
name_label.place(x=20, y=90)

username = Entry(window, text="", bd=2, width=25)
username.place(x=150, y=98)

height_label = Label(window, text="Your height (cm): ", bg="lightcyan", font=("Arial", 15), bd=5)
height_label.place(x=20, y=150)

height_entry = Entry(window, text="", bd=2, width=25)
height_entry.place(x=200, y=158)

weight_label = Label(window, text="Your weight (kg): ", bg="lightcyan", font=("Arial", 15), bd=2)
weight_label.place(x=20, y=180)

weight_entry = Entry(window, text="", bd=2, width=25)
weight_entry.place(x=200, y=188)

calculate_button = Button(window, text = "Calculate", bg = "lightcyan", bd = 4, command = calculate_bmi)
calculate_button.place(x = 20, y = 250)

result_frame = LabelFrame(window, text = "Result", bg = "lightcyan", font = ("Arial", 15))
result_frame.pack(padx = 20, pady = 20)
result_frame.place(x = 20, y = 300)

result_label = Label(result_frame, text = "Your result will be displayed here", bg = "lightcyan", font=("Arial", 15), width = 30)
result_label.place(x = 20, y = 20)
result_label.pack()

window.mainloop()