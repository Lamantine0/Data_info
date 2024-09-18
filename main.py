
import json



class Info_people:

    def __init__(self, file_path):

        self.file_path = file_path
        self.file_data = self.get_users()
        self.last_name = [user["last_name"] for user in self.file_data]
    

    
    def get_users(self):

        with open (self.file_path, "r") as info_people:

            return json.load(info_people)
            

    

    def get_first_name(self):
        
        

        for user in self.file_data:
            print(user["first_name"])     
    

    def get_date_of_birth(self):

        for user in self.file_data:

            print(user["date_of_birth"])


    

data_people = Info_people('data\data_info.json')



print(data_people.get_users())


print(data_people.get_first_name())        

print(data_people.last_name)       



print(data_people.get_date_of_birth())




class New_User(Info_people):

    def save_users(self):
        with open(self.file_path, "w") as info_people:
            json.dump(self.file_data, info_people, indent=4)

    def add_new_user(self, new_user):
            
            for user in self.file_data:
                if user["first_name"] == new_user["first_name"] and new_user["last_name"] == new_user["last_name"]:
            
                    print("Данный пользователь существует")

                    return
       
            self.file_data.append(new_user)
            self.save_users()
            print("Новый пользователь добавлен.")

            
                   


if __name__ == "__main__":
    new_user_data = {
        "first_name": "Frida",
        "last_name": "Smit",
        "date_of_birth": "1994-02-23"
    }


create_user = New_User('data/data_info.json')


create_user.add_new_user(new_user_data)

            



            



