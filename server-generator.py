import os
import webbrowser
import requests
import time
import ctypes
import sys


def add_rules():
    os.system(f"""netsh advfirewall firewall add rule name="Valheim-server TCP 2456-2458" dir=in action=allow protocol=TCP localport=2456-2458""")
    os.system(f"""netsh advfirewall firewall add rule name="Valheim-server UDP 2456-2458" dir=in action=allow protocol=UDP localport=2456-2458""")


def delete_rules():
    os.system(f"""netsh advfirewall firewall delete rule name="Valheim-server TCP 2456-2458" protocol=TCP localport=2456-2458""")
    os.system(f"""netsh advfirewall firewall delete rule name="Valheim-server UDP 2456-2458" protocol=UDP localport=2456-2458""")


def wlan_site():
    try:
        requests.get("http://192.168.0.1/")
        webbrowser.open("http://192.168.0.1/")


    except requests.exceptions.ConnectionError:
        requests.get("http://192.168.1.1/")
        webbrowser.open("http://192.168.1.1/") 


def file_write():

    f_name = "start_headless_server.bat"
    first = time.perf_counter()
    state = False

    for root, dirs, files in os.walk("C:\\"):
        if f_name in files:
            state = True
            file_path = os.path.join(root, f_name)
            print(file_path)
            break


        else:
            second = time.perf_counter()
            difference = second - first

            if(difference > 10):
                print("Failed to locate the file please enter it manually!")
                state = False
                break


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()

    except:
        return False


if is_admin():
    file_write()
else:
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None,1)