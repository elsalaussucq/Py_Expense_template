from PyInquirer import prompt
import csv

user_questions = [
    {
    "type":"input",
    "name":"Name",
    "message":"New User - Name : "
    }
]

def add_user(*args):
    infos = prompt(user_questions)
    your_name = infos['Name']
    while your_name == " " or your_name == "":
        print("You should enter a correct name")
        infos = prompt(user_questions)
        your_name = infos['Name']
    with open("users.csv", "a") as file:
        file.write('\n' + infos['Name'])
        file.close()
    print("User Added !")
    return True