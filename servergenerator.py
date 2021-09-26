import os
import webbrowser
import requests
import time

class Actions:


    def __init__(self, server_name, world_name, password):
        self.server_name = server_name
        self.world_name = world_name
        self.password = password
        self.filename = "start_headless_server.bat"
        

    def wlan_site(self):
        try:
            requests.get("http://192.168.0.1/")
            webbrowser.open("http://192.168.0.1/")


        except requests.exceptions.ConnectionError:
            requests.get("http://192.168.1.1/")
            webbrowser.open("http://192.168.1.1/") 


    def locate_file(self):

        first = time.perf_counter()

        for root, dirs, files in os.walk("C:\\"):
            if self.filename in files:
                file_path = os.path.join(root,self.filename)
                return file_path


            else:
                second = time.perf_counter()
                difference = second - first

                if(difference > 10):
                    return False
                    





#def file_write(server_name, world, password):
#    file = open(locate_file(), "r")
#    read_file = file.read()
#    splitted = read_file.split("\n")
#    splitted.pop(-1)
#    splitted.append(f"""valheim_server -nographics -batchmode -name "{server_name}" -port 2456 -world "{world}" -password "{password}" """)
#    file.close()

#    file = open(locate_file(), "w")
    
#    for i in range (len(splitted)):
#        file.write(splitted[i] + "\n")
#    file.close()
#    print("Kirjoitettu!")
#    quit()
