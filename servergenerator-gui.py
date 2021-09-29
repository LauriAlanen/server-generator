from time import sleep
from typing import Text
import servergenerator
import tkinter as tk
from tkinter import messagebox
import ctypes


ctypes.windll.shcore.SetProcessDpiAwareness(1)

def get_server_details():
    if(len(password_entry.get()) < 5):
        messagebox.showinfo("Password is too short", "Password has to be atleast 5 letters!")


    elif(len(password_entry.get()) >= 5):
        create_button.config(state="disabled", text="Wait... Trying to locate the server file!")
        detail_dict = {
        "server_name" : servername_entry.get(),
        "worldname" : worldname_entry.get(),
        "password" : password_entry.get()
    }
        world = servergenerator.Actions(detail_dict["server_name"], detail_dict["worldname"], detail_dict["password"])

        servername_entry.delete(0, "end")
        worldname_entry.delete(0, "end")
        password_entry.delete(0, "end")

        is_str = isinstance(world.file_path, str)

        if(is_str == True):
            file_found_label.place(x=0,y=355)
            create_button.config(text="Creating Server...")
            world.write_to_file()
            return detail_dict
        
        elif(is_str == False):
            file_not_found_label.place(x=0,y=355)
            create_button.config(state="normal", text="Create Server")




window = tk.Tk()
window.resizable(False, False)
window.geometry("500x400")
window.configure(bg="grey")
window.title("Valheim server generator")


general_info = tk.Label(text = """About\n This program makes it easy to create a dedicated\nservers for valheim. When a server is built using\n this program you are the host!\n\nPrerequisites
You have to have Valheim dedicaterd server\n downloaded from steam! Also You have to\nport forward ports 2456-2458 both (UDP&TCP)\nfrom your router settings. Your router page\nsettings should open automatically  when\nthe script is executed.\n
General\n Servername shold be anything below 20 letters\nthe name cannot include the password!\nWorld name can be anything unless you\n want to use your already existing world\nIf you want to use an already existing world
you have to make sure you have the world file\n in your pc and the new worldname should be\n exactly the same as before
""")

entry_info = tk.Label(text="Enter the server details below", bg = "grey",font = ("Helvetica", 10,"bold"))

servername_label = tk.Label(window, text="Server name", bg = "grey")
servername_entry = tk.Entry(width=20)

worldname_label = tk.Label(window,text="World name", bg = "grey" )
worldname_entry = tk.Entry()

password_label = tk.Label(window,text="Server password (5)", bg = "grey")
password_entry = tk.Entry()

create_button = tk.Button(window,text="Create Server", width=70, command=get_server_details)



file_found_label = tk.Label(text="Server file found!", font=("Helvetica", 10,"bold"))
file_not_found_label = tk.Label(text="Server file not found!", font=("Helvetica", 10,"bold"))


entry_info.place(x=10, y=20)

servername_label.place(x=10, y=50)
servername_entry.place(x=10, y=70)

worldname_label.place(x=10, y=100)
worldname_entry.place(x=10, y=120)

password_label.place(x=10, y=150)
password_entry.place(x=10, y=170)

create_button.place(x=0, y=375)

general_info.place(x=220,y=10)



window.mainloop()   

