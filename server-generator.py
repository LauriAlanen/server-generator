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
        

    def add_rules(self):
        os.system(f"""netsh advfirewall firewall add rule name="Valheim-server TCP 2456-2458" dir=in action=allow protocol=TCP localport=2456-2458""")
        os.system(f"""netsh advfirewall firewall add rule name="Valheim-server UDP 2456-2458" dir=in action=allow protocol=UDP localport=2456-2458""")


    def delete_rules(self):
        os.system(f"""netsh advfirewall firewall delete rule name="Valheim-server TCP 2456-2458" protocol=TCP localport=2456-2458""")
        os.system(f"""netsh advfirewall firewall delete rule name="Valheim-server UDP 2456-2458" protocol=UDP localport=2456-2458""")


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
                return print(file_path)


            else:
                second = time.perf_counter()
                difference = second - first

                if(difference > 10):
                    print("Failed to locate the file!")
                    





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





new = Actions("lmao", "ok",123)
new.locate_file()









"""def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False"""


"""if is_admin():"""


"""else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None,1)"""
