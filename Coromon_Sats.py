# Add you code here

import random

coromon_dic={}
coromon_list=[]
coromon_types=[]

def info_of_type(types):   #create a nested list of stats for given type and returns it
    types=types.lower()
    pok=[]
    for coro in coromon_list:
        mon=list(coromon_dic[coro])
        leng=len(mon)
        if types == mon[0].lower():
            pok.append(mon[0:leng])
    return pok

def avarge1(dic, user):  #given a dicionary and a type print the avrage of either the type or all types
    avg=[]
    heath=0
    att=0
    satt=0
    de=0
    spde=0
    spee=0
    stam=0
    
    number_count=0
    count=1
    for stat in dic.values():
        if user.lower() == stat[0].lower():  
            heath+=int(stat[1])
            att+=int(stat[2])
            satt+=int(stat[3])
            de+=int(stat[4])
            spde+=int(stat[5])
            spee+=int(stat[6])
            stam+=int(stat[7])
            count+=1
        elif number_count > 0 and user.lower() == "all":
            heath+=int(stat[1])
            att+=int(stat[2])
            satt+=int(stat[3])
            de+=int(stat[4])
            spde+=int(stat[5])
            spee+=int(stat[6])
            stam+=int(stat[7])
            count+=1
        number_count+=1
    heath= heath/count
    att=att/count
    satt=satt/count
    de=de/count
    spde=spde/count
    spee=spee/count
    stam=stam/count
    avg.append(heath)
    avg.append(att)
    avg.append(satt)
    avg.append(de)
    avg.append(spde)
    avg.append(spee)
    avg.append(stam)
    return avg


def highest_stat(i_dex):  ##given a index of the stat returns highest type 
    high_HP=0
    high=""
    for typ in coromon_types:
        if typ in coromon_types[1:len_type]:
            avg=avarge1(coromon_dic, typ)
            if high_HP < avg[i_dex]:
                high_HP=avg[i_dex]
                high=typ
            elif high_HP == avg[i_dex]:
                high=f"{high} and {typ}"
    return high


def lowest_stat(i_dex):   #given index of stat return the type with lowest
    low_HP=0
    low=""
    for typ in coromon_types:
        if typ in coromon_types[1:len_type]:
            avg=avarge1(coromon_dic, typ)
            if low_HP == 0:
                low_HP=avg[i_dex]
                low=typ
            elif low_HP > avg[i_dex]:
                low_HP=avg[i_dex]
                low=typ
            elif low_HP == avg[i_dex]:
                low=f"{low} and {typ}"
    return low

with open("CoromonDataset.csv", "r") as data: #reads file

    coromon_everything = data.readlines()   #get the lines
    header=data.readline()

    for coromon in coromon_everything:
        coromon_clean = coromon.strip().split(",") #turns lines into list
        lenth=len(coromon_clean)

        coromon_dic[coromon_clean[0]]=coromon_clean[1:lenth]  #put coromon in a dictionary wiht the stats and type as varbles
        coromon_list.append(coromon_clean[0])       #adds the coromon name to the list

        if coromon_clean[1] not in coromon_types:
            coromon_types.append(coromon_clean[1])   #stores singlar types


 
total_len=len(coromon_list)
len_type=len(coromon_types)
while True:
    user=input("What would you like to know about Coromons? \n A) How many Coromons exist? \n B) A random Coromon? \n C) the types of Coromons. \n D) the avarge stats of a given   type. \n E) Coromon type(s) with highest avarge HP. \n F) Coromon type(s) with lowest avarge HP.  \n G) The Coromon type(s) with the highest average Attack points. \n H) The Coromon type(s) with the lowest average Attack points. \n I) The Coromon type(s) with the highest average Special Attack points. \n J) The Coromon type(s) with the lowest average Special Attack points. \n K) The Coromon type(s) with the highest average  Defense points. \n L) The Coromon type(s) with the lowest average Defense points.\n M) The Coromon type(s) with the highest average Special Defense points. \n N) The Coromon type(s) with the lowest average Special Defense points. \n O) The Coromon type(s) with the highest average Speed points. \n P) The Coromon type(s) with the lowest average Speed points. \n    press enter to leave program: \n")
    user= user.lower()
    if user == "a":
        print(f"there are {total_len} Coromons. \n")
    elif user == "b":
        random1=random.randrange(1,total_len)
        cormon_ran=coromon_list[random1]
        single=list(coromon_dic[cormon_ran])        #this list a list of the stats
        print(f"Here is a random Coromon: {cormon_ran} \n the type: {single[0]} \n the heath    {single[1]} \n the attack {single[2]} \n the special attack {single[3]} \n the     defense {single[4]} \n the special defense {single[5]} \n thespeed {single[6]} \n  the stamina {single[7]} \n")
    elif user == "c":
        print("the types are:", coromon_types[1:len_type])   #find the types of coromons 
    elif user == "d":
        user_types=input(f"What stats for the types would you like to see the avarge stats: \n  {coromon_types[1:len_type]} \n if you would like to see the avarge of all coromons   type: ALL \n")   #given a type
        avg=avarge1(coromon_dic, user_types)     #finds the avarge
        print(f"{user_types} types have an avarge HP of {avg[0]}, attack of {avg[1]}, special   attack of {avg[2]}, defense of {avg[3]}, sepcial defense of {avg[4]}, speed of {avg   [5]}, and stamina of {avg[6]} \n")
    elif user == "e":                          #the rest use either a high or low funciton to make code look cleaner 
        high= highest_stat(int(0))
        print("The coromon with the highest avarge HP are", high, "types \n")    
    elif user == "f":
        low= lowest_stat(int(0))
        print("The coromon with the lowest avarge HP are", low, "types \n")
    elif user == "g":
        high= highest_stat(int(1))
        print("The coromon with the highest avarge attack are", high, "types \n")
    elif user == "h":
        low= lowest_stat(int(1))
        print("The coromon with the lowest avarge attack are", low, "types \n")
    elif user == "i":
        high= highest_stat(int(2))
        print("The coromon with the highest avarge special attack are", high, "types \n")
    elif user == "j":
        low= lowest_stat(int(2))
        print("The coromon with the lowest avarge special attack are", low, "types \n")
    elif user == "k":
        high= highest_stat(int(3))
        print("The coromon with the highest avarge defense are", high, "types \n")
    elif user == "l":
        low= lowest_stat(int(3))
        print("The coromon with the lowest avarge defense are", low, "types \n")
    elif user == "m":
        high= highest_stat(int(4))
        print("The coromon with the highest avarge special defense are", high, "types \n")
    elif user == "n":
        low= lowest_stat(int(4))
        print("The coromon with the lowest avarge special defense are", low, "types \n")
    elif user == "o":
        high= highest_stat(int(5))
        print("The coromon with the highest avarge speed are", high, "types \n")
    elif user == "p":
        low= lowest_stat(int(5))
        print("The coromon with the lowest avarge speed are", low, "types \n")
    else:
        break