import os
import webbrowser
import requests

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
                    return file_path + "\start_headless_server.bat"
    
    def write_to_file(self):
        file = open(self.file_path, "r")
        user_info = []
        
        for x in range(2):
            user_info.append(file.readline())
        for y in range(6):
            user_info.append(file.readline())

        user_info.append(f"""valheim_server -nographics -batchmode -name "{self.server_name}" -port 2456 -world "{self.world_name}" -password "{self.password}""")


        file = open(self.file_path, "w")
        for i in user_info:
            file.write(i)
        file.close()



