import registered
import not_registered
import new
import saving

def salon_grade_check():
    f_in1 = open("automobili.txt","r")
    f_in2 = open("saloni.txt","r")
    f_in3 = open("ocenjene_rezervacije.txt","r")

    autos = f_in1.readlines()
    saloons = f_in2.readlines()
    graded_autos = f_in3.readlines()

    auto_list = []
    
    for auto in autos:
        auto_dict = {}
        auto = auto.split("|")

        auto_dict['id'] = auto[0]
        auto_dict['saloon'] = auto[10].strip("\n")
        auto_list.append(auto_dict)
    
    graded_auto_list = []

    for graded_auto in graded_autos: # pravi prosecnu ocenu iz ocenjenih rezervacija
        graded_auto_dict = {}
        grades = [] # sortiranje
        graded_auto = graded_auto.split("|")

        graded_auto_id = graded_auto[0]
        graded_auto_grades = graded_auto[1].strip("\n").split(",")

        
        for graded_auto_grade in graded_auto_grades:
            grade = float(graded_auto_grade)
            grades.append(grade)

        grade = sum(grades) / len(grades)
    
        graded_auto_dict['id'] = graded_auto_id
        graded_auto_dict['grade'] = grade

        graded_auto_list.append(graded_auto_dict)

    
    f_out = open("saloni.txt","w")
    
    for saloon in saloons:
        saloon_temp = saloon.split("|")
        
        saloon_id = saloon_temp[0]
        saloon_name = saloon_temp[1]
        saloon_address = saloon_temp[2]
        saloon_autos = saloon_temp[3]
        saloon_grade = saloon_temp[4]

        new_saloon_grade = 0
        x = 1
        
        for auto in auto_list:
            for graded_auto in graded_auto_list:
                if auto['id'] == graded_auto['id'] and saloon_id == auto['saloon']:
                    new_saloon_grade += graded_auto['grade']
                   # print(new_saloon_grade,auto['saloon'])
                    new_saloon_grade = new_saloon_grade / x # prosecna ocena salona 
                    x += 1 
        
        updated_saloon = saloon_id + "|" + saloon_name + "|" + saloon_address + "|" + \
            saloon_autos + "|" + str(new_saloon_grade)[0:4] + "\n"
                    

        f_out.write(saloon.replace(saloon,updated_saloon))
       # print(new_saloon_grade)

    
    f_in1.close()
    f_in2.close()
    f_in3.close()

def saloon_cars_check():
    f_in1 = open("saloni.txt","r")
    f_in2 = open("automobili.txt","r")

    saloons = f_in1.readlines()
    autos = f_in2.readlines()

    auto_list = []
    for auto in autos:
        auto_dict = {}
        auto = auto.split("|")

        auto_dict['id'] = auto[0]
        auto_dict['saloon_id'] = auto[10].strip("\n")
        
        auto_list.append(auto_dict)
    # print(auto_list)

    f_out = open("saloni.txt","w")

    for saloon in saloons:
        saloon_temp = saloon.split("|")

        saloon_id = saloon_temp[0]
        saloon_car_list = saloon_temp[3]
        saloon_car_list_temp = saloon_car_list.split(";")
        print(saloon_car_list_temp)    
        
        for auto in auto_list:
            if auto['id'] not in saloon_car_list_temp and auto['saloon_id'] == saloon_id:
                new_saloon_car_list = saloon_car_list + ";" + auto['id']
                f_out.write(saloon.replace(saloon_car_list,new_saloon_car_list))
                saloons.remove(saloon)

    for saloon in saloons:
        f_out.write(saloon)

        

def employe_search():
    f_in = open("zaposleni.txt")

    members = f_in.readlines()
    employes = []

    for member in members:                  #uzima korisnike koji imaju security level 2(zaposleni)
        member = member.split("|")
        member_pos = member[6].strip("\n")
        if member_pos == "2":
            employes.append(member)
            
    print(employes)

    print("__________________________________________\n")
    print("1) Imenu")
    print("2) Prezimenu")
    print("3) Korisnickom imenu")
    print("4) E-mail adresi")
    print("5) Ulozi")
    print("_________________________________________")
    opt = input(">>Unesite funkciju : ")
    
    if opt == "1":
        name = input(">> Ime : ")
        
        for employe in employes:
            employe_name = employe[2]
            if employe_name == name:
                print("\nZaposleni : \n",employe)
        if employe_name != name:
            print("!!! Ne postoji dati zaposleni !!!")

    elif opt == "2":
        lname = input(">> Prezime : ")
        
        for employe in employes:
            employe_lname = employe[3]
            if employe_lname == lname:
                print("\nZaposleni : \n",employe)
        if employe_lname != lname:
            print("!!! Ne postoji dati zaposleni !!!")
        
    elif opt == "3":
        username = input(">> Korisnicko ime : ")
        
        for employe in employes:
            employe_username = employe[0]
            if employe_username == username:
                print("\nZaposleni : \n",employe)
        if employe_username != username:
            print("!!! Ne postoji dati zaposleni !!!")

    elif opt == "4":
        email = input(">> E-mail : ")
        
        for employe in employes:
            employe_email = employe[5]
            if employe_email == email:
                print("\nZaposleni : \n",employe)   
        if employe_email != email:
            print("!!! Ne postoji dati zaposleni !!!")
            
    elif opt == "5":
        job = input(">> Uloga (posao) : ")
        
        for employe in employes:
            employe_job = employe[8].strip("\n")
            if employe_job == job:
                print("\nZaposleni : \n",employe)   
        if employe_job != job:
            print("!!! Ne postoji dati zaposleni !!!")
    else:
        print("!!! Unesite pravilnu vrednost !!!")

    f_in.close()

def auto_del():
    f_in = open("automobili.txt","r")
    autos = f_in.readlines()
    f_out = open("automobili.txt","w")

    erased_auto = input("Koji auto zelite da izbrisete? : ")
    print(autos)

    for auto in autos:
        auto1 = auto.split("|")
        auto_name = auto1[2]
        if auto_name == erased_auto:
            autos.remove(auto)
        else:
            pass
    
    for auto in autos:
        print(auto)
        f_out.write(auto)

    
    f_in.close()
    f_out.close()

def employe_del():
    f_in = open("zaposleni.txt","r")
    members = f_in.readlines()
    f_out = open("zaposleni.txt","w")
    employes = []

    for member in members:                  #uzima korisnike koji imaju security level 2(zaposleni)
        member = member.split("|")
        member_pos = member[6].strip("\n")
        if member_pos == "2":
            employes.append(member)
    
    for employe in employes:
        print(employe)
    
    erased_employe = input("Kog zaposlenog clana zelite da uklonite : ")

    for employe in employes:
        employe_username = employe[0]

        if employe_username == erased_employe:
            employes.remove(employe)
            print("!!! Zaposleni je uspesno uklonjen !!!")
    else:
        print("\n!!! Takav zaposleni ne postoji !!!\n")

    for employe in employes:
        username = employe[0]
        password = employe[1]
        name = employe[2]
        lname = employe[3]
        phone_number = employe[4]
        email = employe[5]
        position = employe[6]
        saloon_id = employe[7]
        job = employe[8]

        employe = username + "|" + password + "|" + name + "|" + lname + "|" + phone_number + "|" + email + "|" + position + "|" + saloon_id + "|" + job 
        
        f_out.write(employe + "\n")


    f_in.close()
    f_out.close()
    
def save_employe(employe):
    f_in = open("zaposleni.txt","a")
    f_in.write(employe)
    f_in.close()

def saloon_update(option):
    if option == "1":#saloni
        f_in1 = open("saloni.txt","r")

        saloons = f_in1.readlines()

        i = 1
        for saloon in saloons:
            saloon = saloon.split("|")
            saloon_name = saloon[1]
            
            print("{0}) {1}".format(i,saloon_name))
            i += 1

        search = input("\n>> Koj salon zelite da azurirate (unesi ime salona) : ")

        f_out1 = open("saloni.txt","w")
        for saloon in saloons:
            saloon_temp = saloon.split("|")
            
            saloon_name = saloon_temp[1]
            saloon_address = saloon_temp[2]
            saloon_autos = saloon_temp[3]

            if search == saloon_name:
                print("\n1) Azuriranje imena")
                print("2) Azuriranje adrese\n")
                print("3) Azuriranje automobila\n")
                y = input(">> Unesite funkciju : ") 
                
                if y == "1":
                    new_name = input(">> Novo ime salona : ")
                    f_out1.write(saloon.replace(saloon_name,new_name))
                    saloons.remove(saloon)
                elif y == "2":
                    new_address = input(">> Novo ime adrese : ")
                    f_out1.write(saloon.replace(saloon_address,new_address))
                    saloons.remove(saloon)
                else:
                    print("!!! Unesite ispravnu vrednost !!!")
        
        for saloon in saloons:
            f_out1.write(saloon)

    elif option == "2":#zaposleni

        pass
        
    elif option == "3":#auto
        f_in2 = open("automobili.txt")

        autos = f_in2.readlines()

        i = 1
        for auto in autos:
            auto = auto.split("|")
            
            auto_name = auto[2]
            auto_distance = auto[7]
            auto_price = auto[8]

            print("{0}) {1}     {2} km    {3} EUR".format(i,auto_name.ljust(16),auto_distance.ljust(8),auto_price))
            i += 1

    else:
        print("!!! Unesi ispravnu vrednost !!!")

def advanced_employe_search():
    y = "da"
    employe = {}

    stop_last_name = 0
    stop_name = 0
    stop_user_name = 0
    stop_email = 0
    stop_job = 0
    while(True):
        if y == "da":
            if stop_name == 0:
                print("\n1) Ime")
            if stop_last_name == 0:
                print("2) Prezime")
            if stop_user_name == 0:
                print("3) Korisnicko ime")
            if stop_email == 0:
                print("4) E-mail adresa")
            if stop_job == 0:
                print("5) Uloga")
        
            x = input("\n>> Unesi funkciju : ")

            if x == "1" and stop_last_name == 0:
                employe['name'] = input(">> Ime : ")
                stop_last_name == 1

            elif x == "2" and stop_name == 0:
                employe['last_name'] = input(">> Prezime : ")
                stop_name == 1

            elif x == "3" and stop_user_name == 0:
                employe['username'] = input(">> Korisnicko ime : ")
                stop_user_name == 1

            elif x == "4" and stop_email == 0:
                employe['email'] = input(">> E-mail adresa : ")
                stop_email = 1

            elif x == "5" and stop_job == 0:
                employe['job'] = input(">> Uloga (posao) : ")
                stop_job == 1

            y = input("\n>> Nastaviti (da/ne) : ")
        
        elif y == "ne":
            advanced_employe_print(employe)
            break

        else:
            print("\n!!! Unesi ispravnu vrednost !!!\n")
            break

def employe_table():
    print("\n    Ime      |    Prezime    |  Korisnicko ime  |       E-mail adresa      |  Uloga")
    print("-------------I---------------I------------------I--------------------------I----------")

def advanced_employe_print(wanted_employe):
    f_in = open("zaposleni.txt","r")

    employes = f_in.readlines()

    employe_list = []

    for employe in employes:
        employe_dict = {}
        employe = employe.split("|")

        employe_dict['name'] = employe[2]
        employe_dict['last_name'] = employe[3]
        employe_dict['username'] = employe[0]
        employe_dict['email'] = employe[5]
        employe_dict['job'] = employe[8].strip("\n")

        employe_list.append(employe_dict)

    check = False
    for employe in employe_list:
        final_print = employe['name'].ljust(18) + employe_dict['last_name'].ljust(15) + employe_dict['username'].ljust(18) +\
                        employe_dict['email'].ljust(26) + employe_dict['job'] + "\n"
        
        result = all(elem in employe.items() for elem in wanted_employe.items())

        if result == True:
            employe_table()
            print(final_print)
            check = True
    
    if check == False:
        print("\n!!! Takva rezervacija ne postoji !!!\n")

def member():
    while(True):
        saloon_cars_check()
        salon_grade_check()
        print("__________________________________________\n")
        print("[1] Dodavanje automobila")
        print("[2] Dodavanje novih zaposlenih")
        print("[3] Azuriranje salona (izmena podataka o zaposlenim i automobilima)")
        print("[4] Brisanje automobila")
        print("[5] Brisanje zaposlenih")
        print("[6] Pregled automobila")
        print("[7] Pretraga automobila")
        print("[8] Pretraga zaposlenih")
        print("\n[b] Odjava")
        print("[x] Izadji iz aplikacije")
        print("__________________________________________")

        x = input(">> Unesite funkciju (Admin) : ")

        if x == "1":
            auto = new.automobile()
            if auto == 0:
                pass
            else:
                saving.save_auto(saving.auto_to_str(auto))
                saloon_cars_check()
            pass
       
        elif x == "2":
            employe = new.employe_from_admin()
            save_employe(saving.employe_to_stri(employe))
            pass
       
        elif x == "3":
            print("\n1) Izmena podataka salona")
            print("2) Izmena podataka zaposlenih")
            print("3) Izmena podataka automobila\n")
            y = input(">> Unesi funkciju : ")
            saloon_update(y)
            pass
       
        elif x == "4":
            auto_del()
            pass
     
        elif x == "5":
            employe_del()
            pass
       
        elif x == "6":
            not_registered.car_print()
            pass
       
        elif x == "7":
            not_registered.car_search()
            pass
      
        elif x == "8":            
            print("\n[1] Pretraga po jednom kriterijumu")
            print("[2] Pretraga po vise kriterijuma\n")
            x = input(">> Unesite funkciju : ")
            
            if x == "1":
                employe_search()
                pass
            elif x == "2":
                advanced_employe_search()
                pass
            else:
                print("\n !!! Unesi ispravnu vrednost !!!\n")
                pass
            pass
       
        elif x == "b":
            return 0
        elif x == "x":
            return 1
        else:
            print("\n!!! Unesi pravilnu vrednost !!!\n")