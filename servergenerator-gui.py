from time import sleep
from typing import ClassVar, Text
import servergenerator
import tkinter as tk
from tkinter import messagebox



class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Generic Settings
        self.resizable(False, False)
        self.geometry("500x400")
        self.configure(bg="grey")
        self.title("Valheim server generator")


        # General Info About The Program
        general_info = tk.Label(text = """About\n This program makes it easy to create a dedicated\nservers for valheim. When a server is built using\n this program you are the host!\n\nPrerequisites
        You have to have Valheim dedicaterd server\n downloaded from steam! Also You have to\nport forward ports 2456-2458 both (UDP&TCP)\nfrom your router settings. Your router page\nsettings should open automatically  when\nthe script is executed.\n
        General\n Servername shold be anything below 20 letters\nthe name cannot include the password!\nWorld name can be anything unless you\n want to use your already existing world\nIf you want to use an already existing world
        you have to make sure you have the world file\n in your pc and the new worldname should be\n exactly the same as before
        """)
        general_info.place(x=220,y=10)


        # Entrys + Info labels
        self.entry_info = tk.Label(text="Enter the server details below", bg = "grey",font = ("Helvetica", 10,"bold"))
        self.entry_info.place(x=10, y=20)

        self.servername_label = tk.Label(self, text="Server name(3)", bg = "grey")
        self.servername_entry = tk.Entry(width=20)

        self.worldname_label = tk.Label(self,text="World name(3)", bg = "grey" )
        self.worldname_entry = tk.Entry()

        self.password_label = tk.Label(self,text="Server password (5)", bg = "grey")
        self.password_entry = tk.Entry()

        self.servername_label.place(x=10, y=50)
        self.servername_entry.place(x=10, y=70)

        self.worldname_label.place(x=10, y=100)
        self.worldname_entry.place(x=10, y=120)

        self.password_label.place(x=10, y=150)
        self.password_entry.place(x=10, y=170)

        self.file_found_label = tk.Label(text="Server file found!", font=("Helvetica", 10,"bold"))
        self.file_not_found_label = tk.Label(text="Server file not found!", font=("Helvetica", 10,"bold"))

        # Buttons
        self.create_button = tk.Button(self,text="Create Server", width=70, command = self.create_server)
        self.create_button.place(x=0, y=375)

        # Checkbuttons
        self.bool_var = tk.BooleanVar()
        self.router_tick = tk.Checkbutton(text = "Open router settings?", variable = self.bool_var, onvalue = True, offvalue = False)
        self.router_tick.place(x=10, y = 205)



    # Main creation function
    def create_server(self):
        if(self.file_write_info() == True, self.router_settings()):
            print("placeholder")


    # Sub functions below
    def file_write_info(self):

        if(len(self.password_entry.get()) < 5 or len(self.worldname_entry.get()) < 3 or len(self.servername_entry.get()) < 3 or self.servername_entry.get() in self.password_entry.get()):
            messagebox.showinfo("Field Error!", "Make sure you met the requirements on servername, worldname and password!")

        elif(len(self.password_entry.get()) >= 5):
            self.create_button.config(state="disabled", text="Wait... Trying to locate the server file!")

            world = servergenerator.Actions(self.servername_entry.get(), self.worldname_entry.get(), self.password_entry.get())

            self.servername_entry.delete(0, "end")
            self.worldname_entry.delete(0, "end")
            self.password_entry.delete(0, "end")

            is_str = isinstance(world.file_path, str)

            if(is_str == True):
                self.file_found_label.place(x=0,y=355)
                self.create_button.config(text="Creating Server...")
                world.write_to_file()
                return True
            
            elif(is_str == False):
                self.file_not_found_label.place(x=0,y=355)
                self.create_button.config(state="normal", text="Create Server")
                return False


    def router_settings(self):
        if(self.bool_var.get() == True):
            servergenerator.Actions.wlan_site(self)
            





if __name__ == "__main__":
    app = App()
    app.mainloop()
