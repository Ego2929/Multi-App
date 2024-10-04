import qrcode
import os
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import random

def create():
    global url
    url = enter.get()
    
    if not url:
        messagebox.showerror("Error", "Invalid Value")
        enter.delete(0, "end")
        return
    elif not url.startswith(('http://', 'https://')):
        messagebox.showerror("Error", "Invalid Value")
        enter.delete(0, "end")
        return
    
    # Create the QR code
    img = qrcode.make(url)
    
    # Resize the image to thumbnail size
    img = img.resize((150, 150), Image.ANTIALIAS)
    img_tk = ImageTk.PhotoImage(img)
    
    # Display the QR code on the label
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    qr_label.place(x=170, y=230)

def delete():
    enter.delete(0, "end")

def download():
    if not url:
        messagebox.showerror("Error", "No QR code to save. Please create a QR code first.")
        return

    img = qrcode.make(url)
    
    desktop_path = os.path.expanduser("~") + "/Desktop/"
    
    i = 1
    while os.path.exists(os.path.join(desktop_path, f"qr_{i}.png")):
        i += 1
    file_path = os.path.join(desktop_path, f"qr_{i}.png")
    
    img.save(file_path, "PNG")

    messagebox.showinfo("Success", f"QR code successfully created and saved to desktop: {file_path}")

def open_qr_page():
    form.destroy()
    qr_page()

def open_guess_page():
    form.destroy()
    guess_page()

def open_calculator_page():
    form.destroy()
    calculator_page()

def qr_page():
    global enter, qr_label, url
    
    qr_form = Tk()
    qr_form.title("QR Code Maker")
    qr_form.geometry("500x500")
    qr_form.config(bg="yellow")
    
    border_label = Label(qr_form, borderwidth=90, relief="raised", 
                         highlightthickness=20, highlightbackground="black", anchor="center", height=100, width=50)
    border_label.pack()
    
    name_label = Label(qr_form, text="Enter the URL: ", font="Times 13")
    name_label.place(x=190, y=120)
    
    enter = Entry(qr_form)
    enter.place(x=185, y=147)
    
    create_button = Button(qr_form, text="Create", command=create, font="Times 12 bold", bg="lightgreen")
    create_button.place(x=150, y=180)
    
    delete_button = Button(qr_form, text="Delete", command=delete, font="Times 12 bold", bg="salmon")
    delete_button.place(x=230, y=180)
    
    download_button = Button(qr_form, text="Download", command=download, font="Times 12 bold", bg="lightblue")
    download_button.place(x=310, y=180)
    
    qr_label = Label(qr_form, image=None, highlightbackground="black", relief="sunken", highlightthickness=0)
    qr_label.place_forget()

    qr_form.mainloop()

def guess_page():
    guess_form = Tk()
    guess_form.title("Guess Game Page")
    guess_form.geometry("500x500")
    guess_form.config(bg="orange")

    game_var = StringVar(value="")

    def play():
        user_choice = game_var.get()
        if user_choice not in ["Rock", "Paper", "Scissors"]:
            messagebox.showerror("Error", "Please make a valid selection!")
            return
        
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        if user_choice == computer_choice:
            result = "It's a tie! Try again."
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            result = f"You win! Computer's choice: {computer_choice}"
        else:
            result = f"You lose! Computer's choice: {computer_choice}"

        result_label.config(text=result)
        result_label.place(x=150, y=300)

    Label(guess_form, text="Make your choice: ", font="Times 16", bg="orange").pack(pady=10)

    button_frame = Frame(guess_form, bg="orange")
    button_frame.pack(pady=20)

    Button(button_frame, text="Rock", font="Times 14 bold", bg="lightblue", fg="black", 
           width=12, height=2, relief="raised", command=lambda: game_var.set("Rock")).pack(side=LEFT, padx=5)
    
    Button(button_frame, text="Paper", font="Times 14 bold", bg="lightgreen", fg="black", 
           width=12, height=2, relief="raised", command=lambda: game_var.set("Paper")).pack(side=LEFT, padx=5)
    
    Button(button_frame, text="Scissors", font="Times 14 bold", bg="lightcoral", fg="black", 
           width=12, height=2, relief="raised", command=lambda: game_var.set("Scissors")).pack(side=LEFT, padx=5)

    play_button = Button(guess_form, text="Play", font="Times 14 bold", bg="yellow", fg="black", width=20, height=2, command=play)
    play_button.pack(pady=20)

    result_label = Label(guess_form, text="", font="Times 16", bg="white", fg="black")
    result_label.place(x=150, y=300)
    result_label.place_forget()

    home_button = Button(guess_form, text="Home", font="Times 14 bold", bg="lightgrey", fg="black", width=20, height=2, command=lambda: (guess_form.destroy(), main_page()))
    home_button.pack(pady=10)
    home_button.place(x=125, y=425)

    guess_form.mainloop()

def calculator_page():
    def append_to_entry(value):
        current_text = entry.get()
        entry.delete(0, "end")
        entry.insert(0, current_text + value)

    def calculate():
        try:
            expression = entry.get()
            result = eval(expression)
            result_label.config(text=f"Result: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Invalid input: {e}")

    def clear_entry():
        entry.delete(0, "end")

    calculator_form = Tk()
    calculator_form.title("Calculator")
    calculator_form.geometry("400x600")
    calculator_form.config(bg="lightgrey")

    entry = Entry(calculator_form, font="Times 20", width=15, borderwidth=2, relief="solid")
    entry.pack(pady=20)

    calculate_button = Button(calculator_form, text="Calculate", font="Times 16", command=calculate, width=20, bg="lightgreen")
    calculate_button.pack(pady=10)

    result_label = Label(calculator_form, text="Result: ", font="Times 15", bg="lightgrey")
    result_label.pack(pady=20)

    clear_button = Button(calculator_form, text="C", font="Times 16", command=clear_entry, width=20, bg="salmon")
    clear_button.pack(pady=10)

    button_frame = Frame(calculator_form, bg="lightgrey")
    button_frame.pack(pady=10)

    buttons = [
        ('7', '8', '9', '/'),
        ('4', '5', '6', '*'),
        ('1', '2', '3', '-'),
        ('0', '.', '=', '+')
    ]
    
    button_colors = [
        ('lightblue', 'lightcoral', 'lightgreen', 'lightyellow'),
        ('lightpink', 'lightcyan', 'lightgoldenrod', 'lightgray'),
        ('lightcoral', 'lightpink', 'lightblue', 'lightgreen'),
        ('lightyellow', 'lightgray', 'lightcyan', 'lightgoldenrod')
    ]

    for row_index, (row, color_row) in enumerate(zip(buttons, button_colors)):
        for col_index, (button, color) in enumerate(zip(row, color_row)):
            btn = Button(button_frame, text=button, font="Times 16", width=4, height=2, bg=color, 
                         command=lambda b=button: (calculate() if b == '=' else append_to_entry(b)))
            btn.grid(row=row_index, column=col_index, padx=10, pady=10)

    home_button2 = Button(calculator_form, text="Home", font="Times 16", command=lambda: (calculator_form.destroy(), main_page()), width=20, bg="lightblue")
    home_button2.pack(pady=20)

    calculator_form.mainloop()

def main_page():
    global form
    form = Tk()
    form.title("Main Page")
    form.geometry("500x500")
    form.config(bg="lightblue")

    welcome_label = Label(form, text="Welcome to the Multi-App", font=("Times New Roman", 24, "bold"), bg="white", fg="darkblue")
    welcome_label.pack(pady=20)

    qr_button = Button(form, text="QR Code Maker", font="Times 16", bg="lightgreen", width=20, height=2, command=open_qr_page)
    qr_button.pack(pady=10)

    guess_button = Button(form, text="Guess Game", font="Times 16", bg="orange", width=20, height=2, command=open_guess_page)
    guess_button.pack(pady=10)

    calculator_button = Button(form, text="Calculator", font="Times 16", bg="lightyellow", width=20, height=2, command=open_calculator_page)
    calculator_button.pack(pady=10)

    form.mainloop()

main_page()
