def car_print(search,option):
    f_in = open("automobili.txt","r")
    autos = f_in.readlines()

    print("\nID    |  Tablica  |     Naziv     |  Broj sedista  |  Klima  |  Cena po danu (Eur)  |  Tip motora  |  Kilometraza  |      Boja      |  Dostupnost")
    print("------I-----------I---------------I----------------I---------I----------------------I--------------I---------------I----------------I------------------")
    
    auto_list = []
    for auto in autos:
        auto_dict = {}
        auto = auto.split("|")

        auto_dict['id'] = auto[0]
        auto_dict['num_plate'] = auto[1]
        auto_dict['name'] = auto[2]
        auto_dict['seats'] = auto[3]
        auto_dict['air_cond'] = auto[4]
        auto_dict['engine'] = auto[5]
        auto_dict['color'] = auto[6]
        auto_dict['distance'] = auto[7]
        auto_dict['price'] = auto[8]
        auto_dict['availability'] = auto[9]

        auto_list.append(auto_dict)
    
    check = False
    for auto in auto_list:
        final_print = auto['id'].ljust(8) + auto['num_plate'].ljust(13) + auto['name'].ljust(20).rjust(20) + \
                        auto['seats'].ljust(15) + auto['air_cond'].ljust(15) + auto['price'].ljust(16) + \
                        auto['engine'].ljust(18) + auto['distance'].ljust(16) + auto['color'].ljust(14) + auto['availability']

        if option == "1":
            if search == auto['id']:
                print(final_print)
                check = True

        elif option == "2":
            if search == auto['num_plate']:
                print(final_print)
                check = True
        
        elif option == "3":
            if search == auto['seats']:
                print(final_print)
                check = True
        
        elif option == "4":
            if search == auto['air_cond']:
                print(final_print)
                check = True
        
        elif option == "5":
            if search == auto['engine']:
                print(final_print)
                check = True
        
        elif option == "6":
            if search == auto['color']:
                print(final_print)
                check = True
        
        elif option == "7":
            if search == auto['distance']:
                print(final_print)
                check = True
        
        elif option == "8":
            if search == "1":
                if auto['availability'] == "dostupan":
                    print(final_print)
                    check = True
            
            elif search == "2":
                if auto['availability'] == "nije dostupan":
                    print(final_print)
                    check = True

    if check == False:
        print("\n!!! Nazalost nemamo takav automobil na raspolaganju !!!\n")
    pass
      
def car_search():
    print("\n1) Po ID-u automobila")
    print("2) Nazivu")
    print("3) Broju tablice")
    print("4) Klimi")
    print("5) Tipu motora")
    print("6) Boji")
    print("7) Ceni")
    print("8) Dostupnosti\n")    
    x = input(">> Unesite funkciju : ")

    if x == "1": 
        search = input(">> ID : ")
        car_print(search,"1")

    elif x == "2": 
        search = input(">> Naziv : ")
        car_print(search,"2")

    elif x == "3": 
        search = input(">> Broj tablice : ")
        car_print(search,"3")
    
    elif x == "4": 
        search = input(">> Da li postoji klima (da/ne) : ")
        car_print(search,"4")
    
    elif x == "5": 
        search = input(">> Tip motora : ")
        car_print(search,"5")
    
    elif x == "6": 
        search = input(">> Boja : ")
        car_print(search,"6")
    
    elif x == "7": 
        search = input(">> Cena : ")
        car_print(search,"7")
    
    elif x == "8": 
        print("\n1) Dostupan")
        print("2) Nije dostupan\n")
        search = input(">> Dostupnost : ")
        
        car_print(search,"8")

    else:
        print("\n!!! Unesi pravilnu vrednost !!!\n")

def advanced_car_print(car):
    f_in = open("automobili.txt","r")
    autos = f_in.readlines()

    print("\nID    |  Tablica  |     Naziv     |  Broj sedista  |  Klima  |  Cena po danu (Eur)  |  Tip motora  |  Kilometraza  |      Boja      |  Dostupnost")
    print("------I-----------I---------------I----------------I---------I----------------------I--------------I---------------I----------------I------------------")
    
    auto_list = []
    for auto in autos:
        auto_dict = {}
        auto = auto.split("|")

        auto_dict['id'] = auto[0]
        auto_dict['num_plate'] = auto[1]
        auto_dict['name'] = auto[2]
        auto_dict['seats'] = auto[3]
        auto_dict['air_cond'] = auto[4]
        auto_dict['engine'] = auto[5]
        auto_dict['color'] = auto[6]
        auto_dict['distance'] = auto[7]
        auto_dict['price'] = auto[8]
        auto_dict['availability'] = auto[9]

        auto_list.append(auto_dict)
    
    check = False


    for auto in auto_list:
        # print(car.items())
        # print(auto.items())
        result = all(elem in auto.items()  for elem in car.items()) #Proverava da li neki auto sadrzi elemente trazenog 
        
        if result == True:                                           #automobila
            final_print = auto['id'].ljust(8) + auto['num_plate'].ljust(13) + auto['name'].ljust(20).rjust(20) + \
                        auto['seats'].ljust(15) + auto['air_cond'].ljust(15) + auto['price'].ljust(16) + \
                        auto['engine'].ljust(18) + auto['distance'].ljust(16) + auto['color'].ljust(14) + auto['availability']
            print(final_print)
            check = True

    if check == False:
        print("\n!!! Nazalost nemamo takav automobil na raspolaganju !!!\n")
        pass


def advanced_car_search():
    f_in = open("automobili.txt","r")
    autos = f_in.readlines()
    stop_id = 0
    stop_name = 0
    stop_num_plate = 0
    stop_air_cond = 0
    stop_engine = 0
    stop_color = 0
    stop_price = 0
    stop_availability = 0
    
    y = "da"

    auto = {}
    while (True):
        if y == "da":
            if stop_id == 0:
                print("1) Po ID-u automobila")
            
            if stop_name == 0:
                print("2) Nazivu")
            
            if stop_num_plate == 0:
                print("3) Broju tablice")
            
            if stop_air_cond == 0:
                print("4) Klimi")
            
            if stop_engine == 0:
                print("5) Tipu motora")
            
            if stop_color == 0:
                print("6) Boji")
            
            if stop_price == 0:
                print("7) Ceni")
            
            if stop_availability == 0:
                print("8) Dostupnosti\n")    
            
            x = input(">> Unesite funkciju : ")
            
            if x == "1" and stop_id == 0:
                auto['id'] = input(">> ID trazenog automobila : ")
                stop_id = 1

            elif x == "2" and stop_name == 0:
                auto['name'] = input(">> Naziv trazenog automobila : ")
                stop_name = 1

            elif x == "3" and stop_num_plate == 0:
                auto['num_plate'] = input(">> Naziv tablice : ")
                stop_num_plate = 1

            elif x == "4" and stop_air_cond == 0:
                auto['air_cond'] = input(">> Da li postoji klima : ")
                stop_air_cond = 1

            elif x == "5" and stop_engine == 0:
                auto['engine'] = input(">> Tip motora : ")
                stop_engine = 1

            elif x == "6" and stop_color == 0:
                auto['color'] = input(">> Boja : ")
                stop_color = 1

            elif x == "7" and stop_price == 0:
                auto['price'] = input(">> Cena na dan : ")
                stop_price = 1
                

            elif x == "8" and stop_availability == 0:
                print("\n1) Dostupan")
                print("2) Nije dostupan\n")
                z = input(">> Dostupnost : ")
                
                if z == "1":
                    auto['availability'] = "dostupan"
                    stop_availability = 1

                elif z == "2":
                    auto['availability'] = "nije dostupan"
                    stop_availability = 1

                else: 
                    print("\n !!! Unesite ispravnu vrednost !!!\n")
                    pass
            
            else:
                print("\n!!! Unesi ispravnu vrednost !!!\n")
                pass

            y = input("\n>> Nastaviti (da/ne) : ")
            
        elif y == "ne":
            advanced_car_print(auto)
            break
        
        elif y != "da" or y != "ne":
            print("\n!!! Unesi ispravnu vrednost !!!\n")
            break

def reservation_table():
    print("\n  ID   |    Auto     |  Datum kreiranja rezervacije  |  Pocetak rezervacije  |  Kraj rezervacije  |      Stanje       |  Korisnik ")
    print("-------I-------------I-------------------------------I-----------------------I--------------------I-------------------I------------")
       
def reservation_print(option,search):
    f_in = open("rezervacije.txt","r")

    reservations = f_in.readlines()

    reservation_list = []

    for reservation in reservations:
        reservation_dict = {}
        reservation = reservation.split("|")

        reservation_dict['res_id'] = reservation[0]
        reservation_dict['auto'] = reservation[1]
        reservation_dict['creation_date'] = reservation[2][0:19]
        reservation_dict['start'] = reservation[3]
        reservation_dict['end'] = reservation[4]
        reservation_dict['state'] = reservation[5]
        reservation_dict['username'] = reservation[6].strip("\n")
        
        reservation_list.append(reservation_dict)


    check = False
    

    for reservation in reservation_list:
        final_print = reservation['res_id'].ljust(11) + reservation['auto'].ljust(16) + reservation['creation_date'].ljust(32) + \
                    reservation['start'].ljust(24) + reservation['end'].ljust(20) + reservation['state'].ljust(18) + \
                    reservation['username'] + "\n"
        
        if option == "1":
            if search == reservation['creation_date']:
                reservation_table()
                print(final_print)
                check = True
        
        elif option == "2":
            if search == reservation['start']:
                reservation_table()
                print(final_print)
                check = True
        
        elif option == "3":
            if search ==  reservation['end']:
                reservation_table()
                print(final_print)
                check = True
        
        elif option == "4":
            if search == reservation['username']:
                reservation_table()
                print(final_print)
                check = True
        
        elif option == "5":
            if search == reservation['state']:
                reservation_table()
                print(final_print)
                check = True
            
    if check == False:
        print("\n!!! Ne postoji ni jedna ovakva rezervaciju !!!\n")

    f_in.close()

def reservation_search():
    print("\n1) Po datumu i vremenu kreiranja rezervacije")
    print("2) Datumu preuzimanja")
    print("3) Datumu povratka")
    print("4) Korisniku")
    print("5) Status rezervacije\n")
    x = input(">> Unesi funkciju : ")

    if x == "1":
        search = input(">> Datum i vreme kreiranja rezervacije : ")
        reservation_print(x,search)

    elif x == "2":
        search = input(">> Datum preuzimanja : ")
        reservation_print(x,search)     

    elif x == "3":
        search = input(">> Datum povratka : ")
        reservation_print(x,search)     

    elif x == "4":
        search = input(">> Korisnik : ")
        reservation_print(x,search)     

    elif x == "5":
        print("1) Gotova")
        print("2) Zapoceta")
        print("3) Nije zapoceta")
        search = input(">> Izaberi funkciju : ")
        
        if search == "1":
            reservation_print(x,"gotova")

        elif search == "2":
            reservation_print(x,"zapoceta")

        elif search == "3":
            reservation_print(x,"nije zapoceta")     

        else:
            print("\n !!! Unesi ispravnu vrednost !!!\n")


def advanced_reservation_search():
    stop_creation_date = 0
    stop_start_date = 0
    stop_end_date = 0
    stop_user = 0
    stop_state = 0

    y = "da"
    reservation = {}

    while(True):
        if y == "da":
            if stop_creation_date == 0:
                print("\n1) Po datumu i vremenu kreiranja rezervacije")
            if stop_start_date == 0:
                print("2) Datumu preuzimanja")
            if stop_end_date == 0:
                print("3) Datumu povratka")
            if stop_user == 0:
                print("4) Korisniku")
            if stop_state == 0:
                print("5) Status rezervacije\n")
            
            x = input(">> Unesi funkciju : ")

            if x == "1" and stop_creation_date == 0:
                reservation['creation_date'] = input(">> Datum i vreme kreiranja rezervacije : ")
                stop_creation_date = 1

            elif x == "2" and stop_start_date == 0:
                reservation['start_date'] = input(">> Datum preuzimanja : ")
                stop_start_date = 1

            elif x == "3" and stop_end_date == 0:
                reservation['end_date'] = input(">>  Datum povratka : ")
                stop_end_date = 1

            elif x == "4" and stop_user == 0:
                reservation['username'] = input(">> Korisnik : ")
                stop_user = 1

            elif x == "5" and stop_state == 0:
                print("\n1) Gotova")
                print("2) Zapoceta")
                print("3) Nije zapoceta")
                search = input("\n>> Izaberi funkciju : ")
                
                if search == "1":
                    reservation['state'] = "gotova"
                    stop_state = 1
                elif search == "2":
                    reservation['state'] = "zapoceta"
                    stop_state = 1
                elif search == "3":
                    reservation['state'] = "nije zapoceta"
                    stop_state = 1

                else:
                    print("\n !!! Unesi ispravnu vrednost !!!\n")
                    break
            
            y = input("\n>> Nastaviti (da/ne) : ")
            
        elif y == "ne":
            advanced_reservation_print(reservation)
            break
        
        else:  
            print("\n !!! Unesi ispravnu vrednost !!!\n")
            break


def advanced_reservation_print(wanted_reservation):
    f_in = open("rezervacije.txt","r")

    reservations = f_in.readlines()

    reservation_list = []

    for reservation in reservations:
        reservation_dict = {}
        reservation = reservation.split("|")

        reservation_dict['res_id'] = reservation[0]
        reservation_dict['auto'] = reservation[1]
        reservation_dict['creation_date'] = reservation[2][0:19]
        reservation_dict['start_date'] = reservation[3]
        reservation_dict['end_date'] = reservation[4]
        reservation_dict['state'] = reservation[5]
        reservation_dict['username'] = reservation[6].strip("\n")
        
        reservation_list.append(reservation_dict)


    check = False
    for reservation in reservation_list:
        final_print = reservation['res_id'].ljust(11) + reservation['auto'].ljust(16) + reservation['creation_date'].ljust(32) + \
                reservation['start_date'].ljust(24) + reservation['end_date'].ljust(20) + reservation['state'].ljust(18) + \
                reservation['username'] + "\n"
        
        result = all(elem in reservation.items() for elem in wanted_reservation.items()) #Proverava da li elementi trazene rezervacije postoje,ako postoje vraca True

        if result == True:
            reservation_table()
            print(final_print)
            check = True
        
    if check == False:
        print("\n!!! Takva rezervacija ne postoji !!!\n")

def report():
    f_in = open("rezervacije.txt","r")
    print("NE RADI NE RADI NE RADI NE RADI NE RADI NE RADI")
    print("1) Izvestaj na mesecnom nivou")
    print("2) Izvestaj na nedeljnom nivou")
    print("1) Izvestaj na dnevnom nivou")
    print("NE RADI NE RADI NE RADI NE RADI NE RADI NE RADI")
    rezervacije = f_in.readlines()
    
def member():
    while(True):
        print("__________________________________________")
        print("[1] Pretraga automobila")
        print("[2] Pretraga rezervacija")
        print("[3] Izvestavanje")

        print("[b] Odjava")
        print("__________________________________________")

        x = input(">> Unesite funkciju : ")
        
        if x == "1":
            print("\n[1] Pretraga po jednom kriterijumu")
            print("[2] Pretraga po vise kriterijuma\n")
            x = input(">> Unesite funkciju : ")

            if x == "1":
                car_search()
                pass
            elif x == "2":
                advanced_car_search()
                pass
            else:
                print("\n !!! Unesi ispravnu vrednost !!!\n")
                pass

        elif x == "2":            
            print("\n[1] Pretraga po jednom kriterijumu")
            print("[2] Pretraga po vise kriterijuma\n")
            x = input(">> Unesite funkciju : ")
            
            if x == "1":
                reservation_search()
                pass
            elif x == "2":
                advanced_reservation_search()
                pass
            else:
                print("\n !!! Unesi ispravnu vrednost !!!\n")
                pass
        
        elif x == "3":
            report()
            pass

        elif x == "b":
            return
        
        else:
            print("\n!!! Unesi pravilnu vrednost !!!\n")