import new
import not_registered
import random as r
import saving
from datetime import datetime
from datetime import date

def reservation(username):
    reservation = {}
    
    reservation['res_id'] = r.randint(100000,999999)

    res_auto = input("Unesite ID automobila koji bi hteli da rezevisete : ")
    reservation['res_auto'] = res_auto
    
    day_of_res = datetime.now()
    reservation['day_of_res'] = str(day_of_res)

    date_start_res = input("Unesite datum kada biste preuzeli automobil (u obliku yyyy-mm-dd) : ")
    reservation['date_start_res'] = date_start_res

    date_end_res = input("Unesite datum kada biste vratili automobil (u obliku yyyy-mm-dd) : ")
    reservation['date_end_res'] = date_end_res
    
    reservation['res_state'] = "nije zapoceta" 

    reservation['username'] = username
    
    return reservation

def car_print():
    f_in = open("automobili.txt","r")

    automobiles = f_in.readlines()

    print("\n  ID   |      Naziv        | Cena po danu (Eur) |  Tip motora  |    Boja     |   Dostupnost")
    print("--------------------------------------------------------------------------------------------------")
    for auto in automobiles:
        auto = auto.split("|")
        
        auto_id = auto[0]
        auto_name = auto[2]
        auto_motor = auto[5]
        auto_color = auto[6]
        auto_price = auto[8]
        availability = auto[9].strip("\n")

        final_print = auto[0].ljust(12) + auto_name.ljust(25) + auto_price.ljust(15) + \
                    auto_motor.ljust(15) + auto_color.ljust(15) + availability
        
        print(final_print)
    
    f_in.close()
    
def reservation_receipt(name,state_time):
    f_in = open("rezervacije.txt","r")

    reservations = f_in.readlines()
    
    check = False
    
    
    for reservation in reservations:
        reservation = reservation.split("|")

        res_id = reservation[0]
        auto = reservation[1]
        creation_date = reservation[2][0:19]
        start = reservation[3]
        end = reservation[4]
        state = reservation[5]
        username = reservation[6].strip("\n")
        name = name.strip("\n")
        username = username.strip("\n")
        
        if name == username and state == state_time:
            print("\n  ID   |    Auto     |  Datum kreiranja rezervacije  |  Pocetak rezervacije  |  Kraj rezervacije  |  Stanje   ")
            print("-------------------------------------------------------------------------------------------------------------------")
            res_print = res_id.ljust(11) + auto.ljust(16) + creation_date.ljust(32) + start.ljust(24) + end.ljust(18) + state + "\n"
            print(res_print)
            check = True

    if check == False:
        print("\n!!! Nemate ni jednu ovakvu rezervaciju !!!\n")

    f_in.close()

def reservation_print(name):

    print("\n1) Rezervacije koje su gotove")
    print("2) Rezervacije koje jos nisu zapocete")
    print("3) Rezervacije koje su u toku\n")
    search = input(">> Unesi funkciju : ")

    if search == "1":
        reservation_receipt(name,"gotova")
    
    elif search == "2":
        reservation_receipt(name,"nije zapoceta")
    
    elif search == "3":
        reservation_receipt(name,"zapoceta")
    
    else:
        print("\n!!! Unesi broj u opsegu 1-3 !!!\n")
        

def check_reservation_duration():
    today = date.today()
    f_in = open("rezervacije.txt","r")
    reservations = f_in.readlines()
    f_out = open("rezervacije.txt","w")

    for reservation in reservations:
        reservation_temp = reservation.split("|")
        start_date_temp = reservation_temp[3] 
        start_date = datetime.strptime(start_date_temp,'%Y-%m-%d') #pretvaranje iz str u datetime
        start_date = start_date.date()
        
        end_date_temp = reservation_temp[4]
        end_date = datetime.strptime(end_date_temp,'%Y-%m-%d') #pretvaranje iz str u datetime
        end_date = end_date.date()
        
        res_state = reservation_temp[5]

        if today >= end_date:   #ako je danasnji datum veci od datuma vracanja kola            
            f_out.write(reservation.replace(res_state,"gotova"))

        elif today <= start_date:
            f_out.write(reservation.replace(res_state,"nije zapoceta"))

        elif today >= start_date:
            f_out.write(reservation.replace(res_state,"zapoceta"))
    
    f_in.close()
    f_in.close()

def check_auto(check_id):
    f_in = open("automobili.txt","r")
    autos = f_in.readlines()
    f_out = open("automobili.txt","w")

    check = False

    for auto in autos:
        auto_temp = auto.split("|")
        auto_id = auto_temp[0]
        availability = auto_temp[9].strip("\n")

        if check_id == auto_id  and availability == "dostupan":
            print(check_id,availability)
            f_out.write(auto.replace(availability,"nije dostupan"))
            check = True

        else:
            f_out.write(auto)
    
    if check == True:
        return True

    f_in.close()
    f_out.close()

def check_if_auto_done(name):
    f_in = open("automobili.txt","r")
    autos = f_in.readlines()

    f_in_r = open("rezervacije.txt","r")
    reservations = f_in_r.readlines()

    id_list = []
    for reservation in reservations:
        reservation = reservation.split("|")

        auto_res_id = reservation[1]
        state = reservation[5]

        if state == "gotova":
            id_list.append(auto_res_id)

    f_out = open("automobili.txt","w")

    for auto in autos:
        auto_temp = auto.split("|")

        auto_id = auto_temp[0]
        availability = auto_temp[9].strip("\n")

        if auto_id in id_list:
            f_out.write(auto.replace(availability,"dostupan"))
        else:
            f_out.write(auto)

def auto_grading(name):
    f_in1 = open("rezervacije.txt","r")
    f_in2 = open("ocenjene_rezervacije.txt","r") 

    reservations = f_in1.readlines()
    reservations_backup = reservations
    auto_res_id_list = []
    
    f_out1 = open("rezervacije.txt","w")
    
    graded_autos = f_in2.readlines()

    for reservation in reservations:
        reservation_temp = reservation.split("|")

        res_id = reservation_temp[0]
        auto_res_id = reservation_temp[1]
        state = reservation_temp[5]
        user = reservation_temp[6].strip("\n")

        if name == user and state == "gotova":
            grade = input(">> Ocenite vasu rezervaciju ( ID : {0} ) ocenom od 1 do 5 : ".format(res_id))
            
            if grade == "1" or grade == "2" or grade == "3" or grade == "4" or grade == "5":
                #reservations.remove(reservation)
                res_print = auto_res_id + "|" + grade

                for reservation in reservations:
                    f_out1.write(reservation)

            else:
                print("\n!!! Unesite broj u opsegu 1-5 !!!\n")
                for reservation in reservations_backup:
                    f_out1.write(reservation)
                return

    res_print_temp = res_print.split("|")
    res_print_id = res_print_temp[0]
    res_print_grade = res_print_temp[1].strip("\n")
    
    f_out2 = open("ocenjene_rezervacije.txt","w")
    check = False
    for graded_auto in graded_autos:
        graded_auto_temp = graded_auto.split("|")

        graded_auto_id = graded_auto_temp[0]
        old_grades = graded_auto_temp[1].strip("\n")
        # print(old_grades)
        # print(res_print_id)
        # print(graded_auto_id)
        if res_print_id == graded_auto_id:
            new_grades = graded_auto_id + "|" + old_grades + "," + res_print_grade + "\n"
            f_out2.write(graded_auto.replace(graded_auto,new_grades))
            check = True
      
        else:
            f_out2.write(graded_auto)
        
    if check == False:
        f_out2.write(res_print + "\n")
        
        
    f_in1.close()
    f_in2.close()
    f_out1.close()
    f_out2.close()

def number_of_done_res(name):
    f_in = open("rezervacije.txt","r")
    reservations = f_in.readlines()
    
    notification = 0
    for reservation in reservations:
        reservation = reservation.split("|")

        state = reservation[5]
        user = reservation[6].strip("\n")

        if state == "gotova"  and  user == name:
            notification += 1
    
    return notification

    f_in.close()

def member(name):
    while(True):
        check_reservation_duration()
        check_if_auto_done(name)
        notification = number_of_done_res(name)
        print("\n ````````````````````````````````````````")
        print("{0}, Dobrodosao !".format(name))
        print("__________________________________________\n")
        print("[1] Kreiraj rezervaciju")
        print("[2] Pregled rezervacija")
        print("[3] Pregled automobila")
        print("[4] Prikaz najbolje ocenjenih automobila")
        print("[5] Pretraga automobila")
        if notification > 0:
            print("[6] Ocenjivanja automobila ({0} neocenjena)".format(notification))
        else:
            print("[6] Nemate ni jedan automobil za ocenjivanje")
        print("\n[7] Odjava sa sistema")
        print("__________________________________________")

        x = input(">> Unesite funkciju (registrovani) : ")

        if x == "1":
            res = reservation(name)
            auto_id = res['res_auto']

            check = check_auto(auto_id)
            if check == True:
                saving.save_reservation(saving.reservation_to_str(res))
            else:
                print("\n!!! Auto sa takvim ID-om ne postoji ILI je rezervisan !!!\n")

            pass

        elif x == "2":
            check_reservation_duration()
            check_if_auto_done(name)
            #check_if_auto_busy(name)
            reservation_print(name)
            pass

        elif x == "3":
            car_print()
            pass

        elif x == "4":
            not_registered.best_cars()
            pass

        elif x == "5":
            not_registered.car_search()
            pass

        elif x == "6":
            if notification != 0:
                auto_grading(name)
            else:
                print("\n !!! Nemate ni jedan auto za ocenjivanje !!! \n")
            pass

        elif x == "7":
            return

        else:
            print("\n Unesi ispravnu vrednost \n")