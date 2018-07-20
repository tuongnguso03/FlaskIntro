from flask import Flask

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
    
app=Flask(__name__)
def user_info(username,Users):
    
    return_string_of_informations=""
    if username in Users:
        for info in Users[username]:
            return_string_of_informations += info
            return_string_of_informations += ":"
            return_string_of_informations += str(Users[username][info])
            return_string_of_informations += "<br/>"
        return return_string_of_informations    
    else: return None
 
@app.route("/user/<user>")
def info(user):
    printing=user_info(user,Users)
    if printing is not None:
        return printing
    else:return "User not found"    

if __name__ == "__main__":
    app.run()    