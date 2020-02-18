import new
import saving
import math

def car_print():
    f_in = open("automobili.txt","r")

    automobiles = f_in.readlines()

    print("\n       Naziv       | Cena po danu (Eur) |   Tip motora    |   Boja")
    print("-------------------I--------------------I-----------------I---------")

    for auto in automobiles:
        auto = auto.split("|")
        
        auto_name = auto[2]
        auto_motor = auto[5]
        auto_color = auto[6]
        auto_price = auto[8].strip("\n") # U tekstualnom fajlu na kraju reda se nalazi enter pa se njega resavamo

        final_print = auto_name.ljust(28) + auto_price.ljust(18) + auto_motor.ljust(16) + auto_color
        
        print(final_print)
    
    f_in.close()

def car_search():
    f_in = open("automobili.txt","r")

    automobili = f_in.readlines()
    print("__________________________________________")
    print("[1] Po nazivu")
    print("[2] Po tipu motora")
    # print("[3] Po oceni") implementovacu posle kada budem imao rezervacije
    x = input("Po kom kriterijumu biste hteli da pretrazite : ")

    if x == "1":
        print("__________________________________________")
        search = input("Naziv automobila : ")
        print("\n       Naziv       | Cena po danu (Eur) |   Tip motora    |   Boja")
        print("-------------------I--------------------I-----------------I---------")
        for auto in automobili:
            autos = auto.split("|")
           
            auto_name = autos[2]
            auto_motor = autos[5]
            auto_color = autos[6]
            auto_price = autos[8].strip("\n")

            if search == auto_name:
                final_print = auto_name.ljust(28) + auto_price.ljust(18) + auto_motor.ljust(16) + auto_color
                print(final_print)


    elif x == "2":
        print("__________________________________________")
        search = input("Motor : ")
        print("\n       Naziv       | Cena po danu (Eur) |   Tip motora    |   Boja")
        print("-------------------I--------------------I-----------------I---------")
        for auto in automobili:
            autos = auto.split("|")
           
            auto_name = autos[2]
            auto_motor = autos[5]
            auto_color = autos[6]
            auto_price = autos[8].strip("\n")

            if search == auto_motor:
                final_print = auto_name.ljust(28) + auto_price.ljust(18) + auto_motor.ljust(16) + auto_color
                print(final_print)

    else:
        print("\nUnesite pravilnu vrednost ( 1/2 ) \n ")
        pass

    
    f_in.close()

def best_cars():
    f_in1 = open("automobili.txt","r")
    f_in2 = open("ocenjene_rezervacije.txt","r")

    autos = f_in1.readlines()
    graded_autos = f_in2.readlines()

    auto_list = []
    
    for auto in autos:
        auto_dict = {}
        auto = auto.split("|")

        auto_dict['id'] = auto[0]
        auto_dict['name'] = auto[2]

        auto_list.append(auto_dict)
    
    
    graded_auto_list = []
    
    for graded_auto in graded_autos: # pravi prosecnu ocenu iz ocenjenih rezervacija
        grades = [] # radi sortiranja ocena
        graded_auto_dict = {}
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

    print("\n   ID  |    Auto    |  Ocena")
    print("-------I----------- I-------")
    
    top_grades = []

    for auto in auto_list:
        for graded_auto in graded_auto_list:
            if auto['id'] == graded_auto['id']:    

                top_grades.append(graded_auto['grade'])
                top_grades.sort( reverse = True )
    
    for auto in auto_list:
        for graded_auto in graded_auto_list:

            if auto['id'] == graded_auto['id'] and top_grades[0] == graded_auto['grade']:    
                fin_print = auto['id'].ljust(10) + auto['name'].ljust(14) + str(graded_auto['grade'])[0:3]
                print(fin_print)
                
            if auto['id'] == graded_auto['id'] and top_grades[1] == graded_auto['grade']:    
                fin_print = auto['id'].ljust(10) + auto['name'].ljust(14) + str(graded_auto['grade'])[0:3]
                print(fin_print)
                
            if auto['id'] == graded_auto['id'] and top_grades[2] == graded_auto['grade']:    
                fin_print = auto['id'].ljust(10) + auto['name'].ljust(14) + str(graded_auto['grade'])[0:3]
                print(fin_print)
                
            if auto['id'] == graded_auto['id'] and top_grades[3] == graded_auto['grade']:    
                fin_print = auto['id'].ljust(10) + auto['name'].ljust(14) + str(graded_auto['grade'])[0:3]
                print(fin_print)
                
            if auto['id'] == graded_auto['id'] and top_grades[4] == graded_auto['grade']:    
                fin_print = auto['id'].ljust(10) + auto['name'].ljust(14) + str(graded_auto['grade'])[0:3]
                print(fin_print)
    
    f_in1.close()
    f_in2.close()

def member():
    while(True):
        print("__________________________________________")
        print("[1] Registracija")
        print("[2] Pregled automobila")
        print("[3] Pretraga automobila")
        print("[4] Prikaz najbolje ocenjenih automobila")
        print("\n[5] Izadji iz aplikacije")
        print("__________________________________________")

        
        x = input(">>Unesite funkciju (neregistrovani) : ")

        if x == "1":
            mem = new.member_from_not_registered_user()
            mem_str = saving.member_to_stri(mem)
            saving.save_member(mem_str + "\n")                  
            pass

        elif x == "2":
            car_print()
            pass
    
        elif x == "3":
            car_search()
            pass
    
        elif x == "4": 
            best_cars()
            pass
    
        elif x == "5":
            print("\nShutting down ...")
            break
    
        else:
            print("\n!!! Unesite pravilnu vrednost !!!\n")
            pass