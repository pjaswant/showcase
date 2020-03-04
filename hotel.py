import json

class LoadRooms:
    hotel_dict = {}
    room_record = []
    
    def __init__(self):
        pass

    @classmethod
    def loadRooms(cls):
        hotel_name = input("Add a hotel: ") 
        cls.addRoom()
        while (True):
            add_more_rooms = input("Do you want to add more rooms in hotel "+ str(hotel_name) + " If YES then press Y else N.")     
            if (add_more_rooms == 'Y' or add_more_rooms == 'y'):
                cls.addRoom()
            else:
                break
        cls.hotel_dict["hotel"] = hotel_name  
        cls.hotel_dict["rooms"] = cls.room_record 
        print ("Hotel Name: " + cls.hotel_dict['hotel'])
        print ("Rooms Details: ")
        print ("*************************")
        for i in range(0, len(cls.hotel_dict['rooms'])):
            print ("Amenities: "+ str(cls.hotel_dict['rooms'][i]['amenities']))
            print ("Cost: $"+ str(cls.hotel_dict['rooms'][i]['cost']))
            print ("*************************")
        cls.budgetRooms()
    
    @classmethod
    def addRoom(cls):
        room_desc = input("What amenities provided like AC, Fridge, Couch, TV, Table etc.") 
        room_cost = input("Whats the cost of the room in $?") 
        room_data = {"amenities":room_desc ,"cost":room_cost}
        cls.room_record.append(room_data)
        return cls.room_record

    @classmethod
    def budgetRooms(cls):
        room_budget = input("Whats your budget? Please enter the amount and we will showcase the available rooms in your budget.") 
        print("Rooms availabe in your budget " + str(room_budget))  
        for i in range(0, len(cls.hotel_dict['rooms'])):
            if (cls.hotel_dict['rooms'][i]['cost'] <= room_budget):
                print ("Amenities: "+ str(cls.hotel_dict['rooms'][i]['amenities']))
                print ("Cost: $"+ str(cls.hotel_dict['rooms'][i]['cost']))
                print ("*************************")
        
    
LoadRooms.loadRooms()