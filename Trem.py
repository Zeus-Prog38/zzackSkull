#!/usr/bin/python3
import os
import time
senha = input("Informe ao zzack,qual e a senha?")
if senha < "777":
    print("acesso não concedido!")
    exit ()
elif senha == "666":  
     print("LOADING")      
     time.sleep(3)
     os.system("clear")
else:
     print(" ______         _____ _  __")
     print("|___  /   /\   / ____| |/ /")
     print("   / /   /  \ | |    | ' / ")
     print(" / /   / /\ \| |    |  &lt;")  
     print(" / /__ / ____ \ |____| . \ ")
     print(" /_____/_/    \_\_____|_|\_")
     print(".        PUXAR DADOS!      ")         
     print("LOADING...")        
     time.sleep(2)
     os.system("clear")
     os.system("sl")
     time.sleep(1)
     
print("████▀░░░░░░░░░░░░░░░░░▀████")
print("███│░░░░░░░░░░░░░░░░░░░│███")
print("██▌│░░░░░░░░░░░░░░░░░░░│▐██")
print("██░└┐░░░░░░░░░░░░░░░░░┌┘░██")
print("██░░└┐░░░░░░░░░░░░░░░┌┘░░██")
print("██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██")
print("██▌░│██████▌░░░▐██████│░▐██")
print("███░│▐███▀▀░░▄░░▀▀███▌│░███")
print(" ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██")
print("██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██")
print("████▄─┘██▌░░░░░░░▐██└─▄████")
print("█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████")
print("████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████")
print("█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████")
print("███████▄░░░░░░░░░░░▄██████")    

print("01:ATUALIZAR TERMUX")
print("02:gerar vírus")
print("03:IP TRACKER")
escolha = False
while escolha == False:
     nivel = int(input("Qual opção: "))
     if (nivel == 1):
         os.system("pkg update && pkg upgrade")
     
     elif (nivel == 2):
         os.system("pkg install nmap")
     
     elif (nivel == 3):
         os.system("git clone https://github.com/DeepSociety/IP-Tracker")
      
