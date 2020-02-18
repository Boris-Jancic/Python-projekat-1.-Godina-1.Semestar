import new

def reservation_to_str(res):
    res_str = str(str(res['res_id']) + "|" + str(res['res_auto']) + "|" + res['day_of_res'] + "|" + res['date_start_res'] + "|" + res['date_end_res'] + \
                  "|" + res['res_state'] + "|" + res['username'])
    return res_str

def save_reservation(reservation):
    f_in = open("rezervacije.txt","a")
    f_in.write(reservation + "\n")

def member_to_stri(mem):     
    member_str = str(str(mem['username']) + "|" + str(mem['password']) + "|" + str(mem['name']) + \
                "|" + str(mem['last_name']) + "|" + str(mem['phone']) + "|" + str(mem['email'])  + "|" +  str(mem['position']))
    return member_str

def employe_to_stri(mem):     
    member_str = "\n" + str(mem['username']) + "|" + str(mem['password']) + "|" + str(mem['name']) + \
                "|" + str(mem['last_name']) + "|" + str(mem['phone']) + "|" + str(mem['email'])  + \
                "|" +  str(mem['position']) + "|" + str(mem['saloon']) + "|" + str(mem['job'])
    return member_str

def save_member(mem):     
    f_in = open("korisnici.txt","a")
    f_in.write(mem)

def auto_to_str(auto):
    auto_str =  str(str(auto['id']) + "|" + str(auto['number_plate']) + "|" + \
                str(auto['name']) + "|" + str(auto['seats']) + "|" + \
                str(auto['aircond']) + "|" + str(auto['motor']) + "|" + \
                str(auto['color']) + "|" + str(auto['kilometres']) + "|" + \
                str(auto['price_per_day']) + "|" + str(auto['availability']) + "|" + \
                str(auto['saloon']))
    return auto_str

def save_auto(auto):
    f_in = open("automobili.txt","a")
    f_in.write(auto + "\n")