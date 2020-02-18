import saving
import login
import not_registered
import registered
import employe
import admin
from datetime import datetime
from datetime import date

def main():
    while(True):
        today = date.today() 
        print("\nDanasnji dan je", today)
        print("__________________________________________\n")
        print("[1] Uloguj se ( ADMIN )")
        print("[2] Uloguj se ( ZAPOSLENI )")
        print("[3] Uloguj se ( REGISTROVANI )")
        print("[4] Opcija neregistrovanog korisnika")
        print("\n[5] Izadji iz aplikacije")
        print("__________________________________________")
        
        x = input(">> Unesite funkciju : ")

        if x == "1":
            print("__________________________________________")
            user = login.login(x)
            
            name = user['name']
            role = user['role']
            
            if role == "3": # Admin
                print(">> --ADMINISTRATOR--")
                exit_sys = admin.member()
                
                if exit_sys == 1:
                    print("\n>> Shutting down ...")
                    break
                if exit_sys == 0:
                    pass

        elif x == "2":
            print("__________________________________________")
            user = login.login(x)
            
            name = user['name']
            role = user['role']

            if role == "2": # Zaposleni
                print(">> --ZAPOSLENI--")
                employe.member()
                pass

        elif x == "3":
            print("__________________________________________")
            user = login.login(x)
            
            name = user['name']
            role = user['role']

            if role == "1": # Registrovani
                print(">> --REGISTROVANI--")
                registered.member(name)
                pass

        elif x == "4":
            not_registered.member()
            break

        elif x == "5":
            print("\n>> Shutting down ...")
            break

        else:
            print("\nUnesi pravilnu vrednost ( 1 / 2 / 3 )\n")
            pass
main()