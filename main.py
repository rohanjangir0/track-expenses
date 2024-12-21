

print("Welcome to budget tracker!\nPlease select an option")
print("1. Add expense or income")
print("2. View transcation")
print("3. Delete transcation")
print("4. generate summary")
print("5. exit")
user_input = int(input("Enter your choice:\n"))

transactions = []
if(user_input == 1):

    data = {
        "type": "",
        "amount": 0,
        "category": "",
        "date": ""
    }
    # while not valid_transaction(data):
    user_input = input("Enter the transaction details in below format:\n type(Expense/Income), amount, category, date(DD-MM-YYYY)\n")

    details = user_input.split(",")

    data['type'] = details[0].strip()
    data['amount'] = details[1].strip()
    data["category"] = details[2].strip()
    data["date"] = details[3].strip()
    print(data)
    
elif(user_input == 2):
    print("you select option 2")
elif(user_input == 3):
    print("you select option 3")
elif(user_input == 4):
    print("you select option 4")
elif(user_input == 5):
    print("you select option 5")
else:
    print("Invalid Option")
    


