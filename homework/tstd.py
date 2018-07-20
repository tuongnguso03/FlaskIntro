Users = {
        'huy' :         {
                'name' : 'Nguyen Quang Huy',
                'age' : 29
        },
        'don' : {
                "name" : 'Don zoombie',
                'age' : 23
        },
        'tuong' : {
                'name' : "Đào Cí Cươ",
                'age' : 15
        }
    }
def user_info(username,Users):
    
    return_string_of_informations= ""
    for info in Users[username]:
        return_string_of_informations += str(info)
        return_string_of_informations += ":"
        return_string_of_informations += str(Users[username][info])
        return_string_of_informations += "<br/>"
    return return_string_of_informations    
print(user_info('tuong',Users))    

print()