import os
print("if you want use the service Install : ")
print(":django")
print(":vsftpd")
Select_usr = input("Do You Want Install django and vsftpd?:        [Y] or [N]")
if Select_usr == 'Y':
 os.system("pip3 install django")
 os.system("sudo apt install vsftpd")
print("[*]Services has been Installed")
print("Start FTP and DJANGO Service")
os.system("python3 start.py")
if Select_usr == 'N':
    exit()