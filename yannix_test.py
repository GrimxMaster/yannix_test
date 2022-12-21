import json

# action 1
def Initialize_data():
    print("initialize data")
    f = open('data.json')

    data = json.load(f)

    f.close()
    return(data)

# Initialize_data()


# action 2
def getRoomByID(data):
    print("get room by id")
    # print(type(data))
    result = {}
    if data != {}:
        target_id = int(input("getRoomById:"))
        # print(target_id)
        for i in data['room']:
            if i['id'] == target_id:
                result = {"id": i['id'],"name": i['name']}

        if result != '':
            print(result)
        else:
            print("No roon with id:",target_id)
    else:
        print("Empty data")
    return(result)   

# getRoomByID()

# action 3
def getAllRoom(data):
    print("get all room")
    if data !={}:
        for i in data['room']:
            print(i)
            return(i)
    else:
        print("Empty data")
        return(data)


# getAllRoom()

# action 4
def getChatById(data):
    print("get chat by id")
    target_chat_id = int(input("getByChatId:"))
    status = {"not found"}
    if data !={}:
        for i in data['room']:
            for j in i['chat']:
                if j['chat_id'] == target_chat_id:
                    status = "found the chat id, in room id :" , i['id'], "\nroom name:", i['name']
                    print(status)
    else:
        print("Empty data")
    return(status)

# getChatById()

# action 5
def getAllChatInRoom(data):
    print("get all chat in room")
    if data !={}:
        res =[]
        target_room_id = int(input("get all chat in room id:"))
        for i in data['room']:
            if i['id'] == target_room_id:
                for j in i['chat']:
                    print(j)
                    res.append(j)
    else:
        print("Empty data")
        return(data)
                

# getAllChatInRoom()

def main():
    action = int(input("Select action (enter 0 for quit) :"))
    res={}
    print(res)
    while(action !=0):
        if action == 1:
            res = Initialize_data()
            if res != None:
                print("data initialized")
            else:
                print("data initialize failed")

        elif action == 2:
            getRoomByID(res)
        elif action == 3:
            getAllRoom(res)
        elif action == 4:
            getChatById(res)
        elif action == 5:
            getAllChatInRoom(res)
        action = int(input("Select action (enter 0 for quit) :"))

if __name__ == "__main__":
    main()