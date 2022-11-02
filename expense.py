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
    user_option = {
        "type":"checkbox",
        "name":"user_options",
        "message":"Expense Spender",
        "choices": users
    }
    option = []
    option = prompt(user_option)
 #   val = confirm("Do you want to continue?")
 #   while val == True:
 #       option.append(prompt(user_option))
    return option


def new_expense(*args):
    infos = prompt(expense_questions)
    users = []
    users = open_csv()
    with open("expense_report.csv", "a") as file:
        file.write('\n' + infos['amount'] + ',' + infos['label'] + ',' + str(users['user_options']) + ' ')
        file.close()
    print("Expense Added !")
    return True


