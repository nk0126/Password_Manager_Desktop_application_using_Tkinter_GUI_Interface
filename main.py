from tkinter import *
from tkinter import messagebox #use to print the message
from random import choice,randint,shuffle #used to print the random number with choices
import pyperclip  #used to copy the content in python automatically


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_Pass():   #function for generate the passowrd

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_letters= [choice(letters) for _ in range(randint(8,10))]
    password_sysmbols=[choice(symbols) for _ in range(randint(2, 4))]
    password_numbers=[choice(numbers) for _ in range(randint(2, 4))]


    password_list = password_numbers+password_sysmbols+password_letters  #creating the different combinatinos of password
    shuffle(password_list)
    password = "".join(password_list) #join the all types of passowrd strings
    password_entry.insert(0,password)  #adding the password in the password entry fill
    pyperclip.copy(password)   #to copy the password automatically



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():                      #to save the password in the txt file

    website=website_entry.get()   #using the get method calling the all entries
    email=email_entry.get()
    password=password_entry.get()

#printing the message for user after filling all enteries to get confrimation.


    is_ok=messagebox.askokcancel(title=website, message=f"Your details are successfully Entered: \nEmail:{email}" 
                                            f"\nPassword: {password} \nIs it ok to save?")



#here, i if statement for the user confrimation.

    if is_ok:

        with open("data.txt", "a") as data_file:

            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)  # removing the user entries for the input box
            email_entry.delete(0, END)
            password_entry.delete(0, END)

    else:

        messagebox.showinfo(title="Wrong Information",message="Re-Enter your Details")



# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title('Password Manager') #title of window
window.config(padx=50,pady=50) #size of window

canvas = Canvas(window, width=200, height=200) #here i use canvas to adding the image
logo_img = PhotoImage(file='logo.png') #adding img
canvas.create_image(100,100,image=logo_img)  #Position of image using the X and Y arguments like axis
canvas.grid(row=0, column=1)    #exract place of an image

#creating the labels

website_label = Label(text="Website :-")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username :-")  #here i create a labels and get them the proper size
email_label.grid(row=2, column=0)
password_label = Label(text="Password :-")
password_label.grid(row=3,column=0)

#Adding the Entry boxes and their sizes

website_entry =Entry(width=35)  #giving the sizing to the website entry box
website_entry.focus()   #addign the focus means the cursor will be continuously moving the in the box
website_entry.grid(row=1,column=1,columnspan=2) #size for the website entry and here use the columnspan for make the fill bigger
email_entry =Entry(width=35)
email_entry.focus()
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"example@gmail.com") #here add the pre-enter message to the entry fill at 0th position
password_entry =Entry(width=35)
password_entry.focus()
password_entry.grid(row=3,column=1,columnspan=2)

#Adding the buttons

generate_password_button = Button(text="Generate Password",command=generate_Pass) #adding the buttions and passing their funcion using command
generate_password_button.grid(row=3,column=2)
add_button = Button(text="Add",width=36,command=save)

add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()      #here end the window

