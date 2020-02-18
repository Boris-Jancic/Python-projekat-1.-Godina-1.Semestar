import datetime
from datetime import date,timedelta,datetime
import time
import random as r

def member():
    member = {}
    
    print("__________________________________________")
    username = input(">> Unesi korisnicko ime : ")
    member['username'] = username
    password = input(">> Unesi lozinku : ")
    member['password'] = password
    name = input(">> Unesi ime : ")
    member['name'] = name
    last_name = input(">> Unesi prezime : ")
    member['last_name'] = last_name
    phone = input(">> Unesi broj telefona : ")
    member['phone'] = phone 
    email = input (">> Unesi Email adresu : ")
    member['email'] = email
    position = input(">> Unesi nivo uloge : ")
    member['position']= position
    print("\n Uspesno dodat korisnik \n")
    print("__________________________________________")

    return member

def member_from_not_registered_user():
    member = {}

    print("__________________________________________")
    username = input("\n>> Unesi korisnicko ime : ")
    member['username'] = username
    password = input(">> Unesi lozinku : ")
    member['password'] = password
    name = input(">> Unesi ime : ")
    member['name'] = name
    last_name = input(">> Unesi prezime : ")
    member['last_name'] = last_name
    phone = input(">> Unesi broj telefona : ")
    member['phone'] = phone 
    email = input (">> Unesi Email adresu : ")
    member['email'] = email
    member['position']= "1"

    return member
        

def employe_from_admin():
    member = {}

    print("__________________________________________")
    username = input("\n>> Unesi korisnicko ime : ")
    member['username'] = username
    password = input(">> Unesi lozinku : ")
    member['password'] = password
    name = input(">> Unesi ime : ")
    member['name'] = name
    last_name = input(">> Unesi prezime : ")
    member['last_name'] = last_name
    phone = input(">> Unesi broj telefona : ")
    member['phone'] = phone 
    email = input (">> Unesi Email adresu : ")
    member['email'] = email
    member['position'] = "2"
    member['saloon'] = saloon_id()
    job = input(">> Uloga zaposlenog : ")
    member['job'] = job

    return member

def saloon_id():
    f_in = open("saloni.txt","r")

    saloons = f_in.readlines()

    i = 1
    
    for saloon in saloons:
        saloon = saloon.split("|")
        saloon_name = saloon[1]
       # print(saloon_name,i)
        
        print("{0}) {1}".format(i,saloon_name))
        i += 1


    option = input(">> U koj salon zelite da smestite automobil (slovima) : ")
    check = False

    for saloon in saloons:
        saloon = saloon.split("|")
        
        saloon_id = saloon[0]
        saloon_name = saloon[1]
    
        if option == saloon_name:
            return saloon_id
            check = True
    
    if check == False:
        print("\n!!! Taj salon ne postoji !!!\n")
        return False

def automobile():
    automobile = {}

    print("__________________________________________")
    automobile['id'] = r.randint(100000,999999)
    number_plate = input("Broj tablice : ")
    automobile['number_plate'] = number_plate
    name = input(">> Ime automobila : ")
    automobile['name'] = name
    seats = input(">> Broj sedista : ")
    automobile['seats'] = seats
    aircond = input(">> Da li klima postoji (da/ne) : ")
    automobile['aircond'] = aircond
    motor = input(">> Tip Motora (dizel, benzin, elektricni) : ")
    automobile['motor'] = motor
    color = input(">> Boja automobila : ")
    automobile['color'] = color
    kilometres = input(">> Predjena kilometraza : ")
    automobile['kilometres'] = kilometres
    price_per_day = input("Cena po danu : ")
    automobile['price_per_day'] = price_per_day
    automobile['availability'] = "dostupan"
    automobile['saloon'] = saloon_id()

    if automobile['saloon'] != False:
        return automobile
    else:
        return 0