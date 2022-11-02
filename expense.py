from PyInquirer import prompt
import csv


expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
]




def open_csv(): 
    file = open('users.csv')
    csvreader = csv.reader(file)
    users = []
    for row in csvreader:
        users.append({"name" : row[0]})
    user = {
        "type":"checkbox",
        "name":"user",
        "message":"Expense Spender",
        "choices": users
    }
    option = []
    option = prompt(user)
    return option

def open_csv_spender(): 
    file = open('users.csv')
    csvreader = csv.reader(file)
    users = []
    for row in csvreader:
        users.append(row[0])
    user_options = {
        "type":"list",
        "name":"user_options",
        "message":"Expense Spender",
        "choices": users
    }
    option = []
    option = prompt(user_options)
    return option


def new_expense(*args):
    infos = prompt(expense_questions)
    users = []
    spender = open_csv_spender()
    users = open_csv()
    with open("expense_report.csv", "a") as file:
        file.write('\n' + infos['amount'] + ',' + infos['label'] + ',' + spender['user_options'] + str(users['user']) + ' ')
        file.close()
    print("Expense Added !")
    return True


