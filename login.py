def login(choice):
    f_in = open("korisnici.txt","r")
    f_in1 = open("zaposleni.txt","r")
    
    user = {}
    members = f_in.readlines()
    employes = f_in1.readlines()

    check = False

    username = input("Unesi korisnicko ime : ")
    password = input("Unesi sifru : ")

    if choice == "1": #administrator
        for member in members:      
            member = member.split("|")
            
            member_username = member[0]     # hvata username,password i poziciju svakog korisnika             
            member_password = member[1]
            member_position = member[6].strip("\n")
            
            if username == member_username and password == member_password and member_position == "3":     # proverava da li postoje
                print("__________________________________________")
                print(member)
                print(">> Uspesno ulogovani")                                   # dati korisnici 
                
                user['role'] = str(member_position) 
                user['name'] = member_username 
                check = True
                return user

    if choice == "2": # ZAPOSLENI
        for member in employes:      
            member = member.split("|")
            
            member_username = member[0]     # hvata username,password i poziciju svakog korisnika             
            member_password = member[1]
            member_position = member[6]
            print(member)
            
            if username == member_username and password == member_password and member_position == "2":     # proverava da li postoje
                print("__________________________________________")
                print(member)
                print(">> Uspesno ulogovani")                                   # dati korisnici 
                
                user['role'] = str(member_position) 
                user['name'] = member_username 
                check = True
                return user

    if choice == "3": # REGISTROVANI
        for member in members:      
            member = member.split("|")
            
            member_username = member[0]     # hvata username,password i poziciju svakog korisnika             
            member_password = member[1]
            member_position = member[6].strip("\n")
            print(member)
            if username == member_username and password == member_password and member_position == "1":     # proverava da li postoje
                print("__________________________________________")
                print(member)
                print(">> Uspesno ulogovani")                                   # dati korisnici 
                
                user['role'] = str(member_position) 
                user['name'] = member_username 
                check = True
                return user

    if check == False:
        user['role'] = "" 
        user['name'] = ""
        print("\n!!! Ne postoji takav korisnik !!!\n")
        return user
            