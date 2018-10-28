item_mystery ={"id":"unknown","mass":0 ,"name":"a mysterious item","description":"""You find a mysterious item with no mass. 
Next to which sits a key, presumably to open this item.
On the item is a note which says:
'He who opens this item will either perish or prevail...'
You have been warned!"""}
item_id ={"id":"id","mass":0.2 ,"name":"id card","description":"""Your new shiny student ID card. Expires 1 June 2017.
You wonder why they have printed a suicide hotline number on it?..."""}
item_laptop ={"id":"laptop","mass":2.2 ,"name":"laptop","description":"It has seen better days. At least it has a WiFi card!"}
item_money ={"id":"money","mass":0.3 ,"name":"money","description":"This wad of cash is barely enough to pay your tuition fees."}
item_biscuits ={"id":"biscuits","mass":1.0 ,"name":"a pack of biscuits","description":"A pack of biscuits."}
item_pen ={"id":"pen","mass":0.3 ,"name":"a pen","description":"A basic ballpoint pen."}
item_handbook ={"id":"handbook","mass":0.9 ,"name":"a student handbook","description":"This student handbook explains everything. Seriously."}
import string 
skip_words =['a','about','all','an','another','any','around','at','bad','beautiful','been','better','big','can','every','for','from','good','have','her','here','hers','his','how','i','if','in','into','is','it','its','large','later','like','little','main','me','mine','more','my','now','of','off','oh','on','please','small','some','soon','that','the','then','this','those','through','till','to','towards','until','us','want','we','what','when','why','wish','with','would']
def filter_words (OOO000O00O0OO000O ,OOO0OOOOOOO0OOO0O ):
    ""
    O00O0OO0O0O0O0O00 =[]
    for O0000OOO00O000000 in OOO000O00O0OO000O :
        if O0000OOO00O000000 not in OOO0OOOOOOO0OOO0O :
            O00O0OO0O0O0O0O00 .extend ([O0000OOO00O000000 ])
    return O00O0OO0O0O0O0O00 
def remove_punct (O00OO00000OOOO000 ):
    ""
    O0000O0OOO0OO0OOO =""
    for OO00OOO00OOO0O00O in O00OO00000OOOO000 :
        if not (OO00OOO00OOO0O00O in string .punctuation ):
            O0000O0OOO0OO0OOO =O0000O0OOO0OO0OOO +OO00OOO00OOO0O00O 
    return O0000O0OOO0OO0OOO 
def normalise_input (OOOOO0OO00OOOO00O ):
    ""
    OO00O000OO0OOO00O =remove_punct (OOOOO0OO00OOOO00O ).lower ()
    OO0OOOO0O0O0OO00O =OO00O000OO0OOO00O .strip ().split ()
    OO0OOOO0O0O0OO00O =filter_words (OO0OOOO0O0O0OO00O ,skip_words )
    return OO0OOOO0O0O0OO00O 
room_reception ={"name":"Reception","description":"""You are in a maze of twisty little passages, all alike.
Next to you is the School of Computer Science and
Informatics reception. The receptionist, Matt Strangis,
seems to be playing an old school text-based adventure
game on his computer. There are corridors leading to the
south and east. The exit is to the west.""","exits":{"south":"Admins","east":"Tutor","west":"Parking"},"items":[item_biscuits ,item_handbook ]}
room_admins ={"name":"MJ and Simon's room","description":"""You are leaning agains the door of the systems managers'
room. Inside you notice Matt "MJ" John and Simon Jones. They
ignore you. To the north is the reception.""","exits":{"north":"Reception"},"items":[]}
room_tutor ={"name":"your personal tutor's office","description":"""You are in your personal tutor's office. He intently
stares at his huge monitor, ignoring you completely.
On the desk you notice a cup of coffee and an empty
pack of biscuits. The reception is to the west.""","exits":{"west":"Reception"},"items":[]}
room_parking ={"name":"the parking lot","description":"""You are standing in the Queen's Buildings parking lot.
You can go south to the COMSC reception, or east to the
general office.""","exits":{"east":"Office","south":"Reception"},"items":[item_mystery ]}
room_office ={"name":"the general office","description":"""You are standing next to the cashier's till at
30-36 Newport Road. The cashier looks at you with hope
in their eyes. If you go west you can return to the
Queen's Buildings.""","exits":{"west":"Parking"},"items":[item_pen ]}
rooms ={"Reception":room_reception ,"Admins":room_admins ,"Tutor":room_tutor ,"Parking":room_parking ,"Office":room_office }
winorlose =0 
mysterypickup =False 
inventory =[item_id ,item_laptop ,item_money ]
current_room =rooms ["Reception"]
def list_of_items (OOO00O0O0OO000OO0 ):
    ""
    O0000OO000O000OO0 =""
    for O00OOO000000O000O in OOO00O0O0OO000OO0 :
        O0000OO000O000OO0 +=O00OOO000000O000O ["name"]+", "
    return O0000OO000O000OO0 [:len (O0000OO000O000OO0 )-2 ]
def print_room_items (OOO000OOO0O0O0O0O ):
    ""
    if OOO000OOO0O0O0O0O ["items"]==[]:
        return None 
    else :
        print ("There is "+list_of_items (OOO000OOO0O0O0O0O ["items"])+' here.')
        print ("")
def print_inventory_items (OOO0OOO0OOOOOO00O ):
    ""
    print ("You have "+list_of_items (OOO0OOO0OOOOOO00O )+".\n")
def print_room (O000O0O00OOO0O00O ):
    ""
    print ("")
    print (O000O0O00OOO0O00O ["name"].upper ())
    print ("")
    print (O000O0O00OOO0O00O ["description"])
    print ("")
    print_room_items (O000O0O00OOO0O00O )
def exit_leads_to (O0OO00O0000000000 ,O000O00O0O0000OOO ):
    ""
    return rooms [O0OO00O0000000000 [O000O00O0O0000OOO ]]["name"]
def print_exit (OO0000000OO0O0OOO ,OO00O00OO00O000OO ):
    ""
    print ("GO "+OO0000000OO0O0OOO .upper ()+" to "+OO00O00OO00O000OO +".")
def print_menu (OOOOO0OOOOOO000O0 ,OO0OO00O0OO000O0O ,OOOOO000OO0000OOO ):
    ""
    print ("You can:")
    for OOOOO0OOOOOO0OOOO in OOOOO0OOOOOO000O0 :
        print_exit (OOOOO0OOOOOO0OOOO ,exit_leads_to (OOOOO0OOOOOO000O0 ,OOOOO0OOOOOO0OOOO ))
    for O000OO000OOO0O000 in OO0OO00O0OO000O0O :
        print ("TAKE "+O000OO000OOO0O000 ["id"].upper ()+" to take "+O000OO000OOO0O000 ["name"]+".")
    for O000OO000OOO0O000 in OOOOO000OO0000OOO :
        print ("DROP "+O000OO000OOO0O000 ["id"].upper ()+" to drop "+O000OO000OOO0O000 ["name"]+".")
    print ("What do you want to do?")
def is_valid_exit (OOO0O00O000OOOOO0 ,O0O00O0O0OOOO000O ):
    ""
    return O0O00O0O0OOOO000O in OOO0O00O000OOOOO0 
def total_weight (O000OO0OO0O0OOOOO ):
    OOOOOO0O0O0OOO000 =0 
    for OO0O0OO0O00O0OOO0 in O000OO0OO0O0OOOOO :
        OOOOOO0O0O0OOO000 +=OO0O0OO0O00O0OOO0 ["mass"]
    return OOOOOO0O0O0OOO000 
def execute_go (O0O00OO000O00OO00 ):
    ""
    global current_room 
    if is_valid_exit (current_room ["exits"],O0O00OO000O00OO00 )==True :
         current_room =move (current_room ["exits"],O0O00OO000O00OO00 )
         print ("You are now in "+current_room ["name"]+".")
    else :
        print ("You cannot go there.")
def execute_take (O0OO0000000O0O00O ):
    ""
    global mysterypickup 
    OOOO0OOOO0O0O0O0O =False 
    O0O0OOOOO000000OO =False 
    for O0000000O0OO0O0O0 in current_room ["items"]:
        if O0OO0000000O0O00O ==O0000000O0OO0O0O0 ["id"]and total_weight (inventory )+O0000000O0OO0O0O0 ["mass"]<=3.5 :
            inventory .append (O0000000O0OO0O0O0 )
            current_room ["items"].remove (O0000000O0OO0O0O0 )
            OOOO0OOOO0O0O0O0O =True 
        elif total_weight (inventory )+O0000000O0OO0O0O0 ["mass"]>3.5 :
            print ("You cannot take this as you would be carrying",total_weight (inventory )+O0000000O0OO0O0O0 ["mass"],"kg. This is more than 3.5kg, the max weight you can carry.")
            return 
    for O0000000O0OO0O0O0 in inventory :
        if O0000000O0OO0O0O0 ["id"]=="unknown":
            print (O0000000O0OO0O0O0 ["description"])
            while O0O0OOOOO000000OO ==False :
                 print ("")
                 print ("Are you sure you want to pick this item up? Y for yes, N for No.")
                 OOO0O0OOOO0O00OO0 =input ()
                 if OOO0O0OOOO0O00OO0 .upper ()=="Y":
                     mysterypickup =True 
                     O0O0OOOOO000000OO =True 
                 elif OOO0O0OOOO0O00OO0 .upper ()=="N":
                     mysterypickup =False 
                     inventory .remove (O0000000O0OO0O0O0 )
                     current_room ["items"].append (O0000000O0OO0O0O0 )
                     O0O0OOOOO000000OO =True 
                 else :
                     print ("invalid input")
                     O0O0OOOOO000000OO =False 
    if OOOO0OOOO0O0O0O0O ==False :
        print ("You cannot take that.")
def execute_drop (OOOOO00000OO0O000 ):
    ""
    OO0OO000000000O00 =False 
    for OOOOOOOOO00OOOOOO in inventory :
        if OOOOO00000OO0O000 ==OOOOOOOOO00OOOOOO ["id"]:
            inventory .remove (OOOOOOOOO00OOOOOO )
            current_room ["items"].append (OOOOOOOOO00OOOOOO )
            OO0OO000000000O00 =True 
            return 
    if OO0OO000000000O00 ==False :
        print ("You cannot drop that.")
def execute_command (OOOOOO00000OOO00O ):
    ""
    if 0 ==len (OOOOOO00000OOO00O ):
        return 
    if OOOOOO00000OOO00O [0 ]=="go":
        if len (OOOOOO00000OOO00O )>1 :
            execute_go (OOOOOO00000OOO00O [1 ])
        else :
            print ("Go where?")
    elif OOOOOO00000OOO00O [0 ]=="take":
        if len (OOOOOO00000OOO00O )>1 :
            execute_take (OOOOOO00000OOO00O [1 ])
        else :
            print ("Take what?")
    elif OOOOOO00000OOO00O [0 ]=="drop":
        if len (OOOOOO00000OOO00O )>1 :
            execute_drop (OOOOOO00000OOO00O [1 ])
        else :
            print ("Drop what?")
    else :
        print ("This makes no sense.")
def menu (OOOO0O0OOOOOOO0O0 ,O0O00O0O00O0O0OO0 ,O0OO0OOO0OO0000OO ):
    ""
    print_menu (OOOO0O0OOOOOOO0O0 ,O0O00O0O00O0O0OO0 ,O0OO0OOO0OO0000OO )
    O0O0OOO00OOO0000O =input ("> ")
    OO0OOO0O0OOOOO000 =normalise_input (O0O0OOO00OOO0000O )
    return OO0OOO0O0OOOOO000 
def move (OO000OO0O0O00000O ,O00000O0O0O0OO0O0 ):
    ""
    return rooms [OO000OO0O0O00000O [O00000O0O0O0OO0O0 ]]
def main ():
    global winorlose 
    while True :
        print_room (current_room )
        print_inventory_items (inventory )
        OO0O0OO00O0O00O0O =menu (current_room ["exits"],current_room ["items"],inventory )
        execute_command (OO0O0OO00O0O00O0O )
        if mysterypickup ==True :
            import random
            winorlose +=random .randint (0 ,100 )
            if winorlose <50 :
                print ("Congratulations! You have prevailed and have won the game!")
                break 
            elif winorlose >=50 :
                print ("You have perished and have lost the game!")
                break 
if __name__ =="__main__":
    main ()
