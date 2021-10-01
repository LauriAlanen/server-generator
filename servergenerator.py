import os
import webbrowser
import requests
import win32gui, win32con
from time import sleep

class Actions:


    def __init__(self, server_name, world_name, password):
        self.server_name = server_name
        self.world_name = world_name
        self.password = password
        self.filename = "Valheim dedicated server"
        self.file_path = self.locate_file()



    def wlan_site(self):
        try:
            requests.get("http://192.168.0.1/")
            webbrowser.open("http://192.168.0.1/")

        except requests.exceptions.ConnectionError:
            requests.get("http://192.168.1.1/")
            webbrowser.open("http://192.168.1.1/") 


    def locate_file(self):
        drive_names = ["C","D","E","F","G","None"]
        for location in drive_names:
            if(location == "None"):
                return False
            for root, dirs, files in os.walk(f"{location}:\\Program Files (x86)"):
                if self.filename in dirs:
                    file_path = os.path.join(root,self.filename)
                    final_path = file_path + "\start_headless_server.bat"
                    return final_path
    
    def write_to_file(self):
        file = open(self.locate_file(), "r")
        user_info = []
        
        for x in range(8):
            user_info.append(file.readline())
        user_info.append(f"""valheim_server -nographics -batchmode -name "{self.server_name}" -port 2456 -world "{self.world_name}" -password "{self.password}""")
        
        file = open(self.locate_file(), "w")
        backup_file= open(self.locate_file().replace("\start_headless_server.bat", "\start_headless_server_backup.bat"), "w")
        for i in user_info:
            file.write(i)
            backup_file.write(i)
        file.close()
        backup_file.close()

    def start_server(self):
        os.chdir(self.locate_file().replace("\start_headless_server.bat",""))
        os.startfile("start_headless_server.bat")
        sleep(0.5)
        minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(minimize , win32con.SW_MINIMIZE)
    
    


