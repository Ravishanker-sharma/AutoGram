import customtkinter as CTK
import tkinter as tk
import os

def start():
    pass

def stop():
    pass

def tags():
    def save_text():
        text_to_save = text_box.get("1.0", "end-1c")  # Get text from textbox
        with open("tags.txt", "w") as file:
            file.write(text_to_save)
            file.close()
        tagger.destroy()

    # Create main window
    tagger = CTK.CTk()
    tagger.title("TAGS - AUTOGRAM")

    # Textbox to input text
    text_box = tk.Text(tagger, height=15, width=50, bg="lightpink")
    text_box.pack(pady=10)

    # Button to save text
    save_button = CTK.CTkButton(tagger, text="Save", hover_color="lime", command=save_text)
    save_button.pack(pady=10)

    # Run the Tkinter event loop
    tagger.mainloop()

def set_timer():
    try:
        hours = int(hours_spinbox.get())
        minutes = int(minutes_spinbox.get())
        seconds = int(seconds_spinbox.get())

        total_seconds = hours * 3600 + minutes * 60 + seconds
        if total_seconds == 0:
            return 1800
        else:
            return total_seconds
    except:
        return 1800

def logout():
    if os.path.exists("x_eca_234"):
        os.remove("x_eca_234")

    gui.destroy()
    login()


def Help():
    pass
def get_user_pass():
    if not os.path.exists("x_eca_234"):
        username = usernameentry.get()
        password = passwordentry.get()
    else:
        with open("x_eca_234",'r') as f:
            info = f.read()
            username = info.splitlines()[0]
            password = info.splitlines()[1]
            f.close()
    return username , password
def GUI():
    global gui,hours_spinbox,minutes_spinbox,seconds_spinbox
    username = (get_user_pass()[0])
    password = (get_user_pass()[1])
    try:
        if login_save.get() == 1:
            with open("x_eca_234","w") as f:
                f.write(f"{usernameentry.get()}\n{passwordentry.get()}")
                f.close()
        root.destroy()
    except:
        pass
    gui = CTK.CTk()
    gui.geometry()
    gui.minsize(400, 600)
    gui.maxsize(400, 600)
    gui.title("Autogram")
    CTK.CTkLabel(gui,text="AUTOGRAM",text_color="skyblue",font=("",40)).grid(row=0,column=0,columnspan=2)
    start_button = CTK.CTkButton(gui,text="START",text_color="white",width=150,height=50,hover_color="green",command=start)
    start_button.grid(row=1,column=0,padx=20,pady=20)
    stop_button = CTK.CTkButton(gui, text="STOP", text_color="white", width=150, height=50, hover_color="red",
                                 command=stop)
    stop_button.grid(row=1, column=1, padx=20, pady=10)
    frame = CTK.CTkFrame(gui)
    frame.grid(row=2, column=0,padx=10, pady=10,columnspan=2)

    CTK.CTkLabel(frame, text="LOOP TIMER",text_color="red",font=("",20)).grid(row=0, column=0,columnspan=2, pady=7)
    # Hours
    CTK.CTkLabel(frame, text="Hours:").grid(row=1, column=0,pady=3)
    hours_spinbox = tk.Spinbox(frame, from_=0, to=24,font=" 40",fg="blue",bg='skyblue')
    hours_spinbox.grid(row=1, column=1)

    # Minutes
    CTK.CTkLabel(frame, text="Minutes:").grid(row=2, column=0,pady=3)
    minutes_spinbox = tk.Spinbox(frame, from_=0, to=59,font=" 40",fg="blue",bg='skyblue')
    minutes_spinbox.grid(row=2, column=1)

    # Seconds
    CTK.CTkLabel(frame, text="Seconds:").grid(row=3, column=0,padx=10)
    seconds_spinbox = tk.Spinbox(frame, from_=0, to=59,font=" 40",fg="blue",bg='skyblue')
    seconds_spinbox.grid(row=3, column=1,padx=20)

    set_button = CTK.CTkButton(gui, text="`Set Timer", text_color="white", width=250, height=40, hover_color="Blue",
                               command=set_timer)
    set_button.grid(row=3, column=0, padx=20, pady=10,columnspan=2)

    tag_button = CTK.CTkButton(gui, text="`TAGS", text_color="Navy", width=250, height=40,hover_color="lime",
                                command=tags)
    tag_button.grid(row=4, column=0, padx=20, pady=10,columnspan=2)

    logout_button = CTK.CTkButton(gui, text="LOGOUT", text_color="white", width=100, height=30, hover_color="red",
                               command=logout)
    logout_button.grid(row=5, column=1, padx=20, pady=130)

    help_button = CTK.CTkButton(gui, text="Help?", text_color="white", width=100, height=30,
                                  command=Help)
    help_button.grid(row=5, column=0, padx=20, pady=130)

    gui.mainloop()
def login():
    global login_save,root,usernameentry,passwordentry
    root = CTK.CTk()
    root.geometry()
    root.minsize(500,200)
    root.maxsize(500,200)
    root.title("Autogram Login")
    usernameentry=CTK.CTkEntry(root,width=400,height=30,placeholder_text="E-mail or Username")
    usernameentry.grid(row=0,column=0,padx=40,pady=10)
    passwordentry=CTK.CTkEntry(root,width=400,height=30,placeholder_text="Password",show="*")
    passwordentry.grid(row=1,column=0,padx=40)
    CTK.CTkButton(root,text="Login",command=GUI).grid(padx=30,pady=15)
    login_save = CTK.CTkCheckBox(root, text="Save Info")
    login_save.grid()
    root.mainloop()

if __name__ == '__main__':
    if not os.path.exists("x_eca_234"):
        login()
    else:
        GUI()

