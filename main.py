
from datetime import datetime



def check_validation(data):
    details = data.split(",")
    t_type = details[0].strip()
    amount = int(details[1].strip())
    category = details[2].strip()
    date = details[3].strip()
        
    print(data)
    if not (t_type == "Expense" or t_type == "Income"):
        print("Transaction type is not valid")
        return False
    if amount < 0:
        print("Please enter a positive amount")
        return False
    try:
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Please input a correct date format")
        return False
    
    return True
    
print("Welcome to budget tracker!\nPlease select an option")
print("1. Add expense or income")
print("2. View transcation")
print("3. Delete transcation")
print("4. generate summary")
print("5. exit")
user_input = int(input("Enter your choice:\n"))

transactions = []
if(user_input == 1):

    # while not valid_transaction(data):
    user_input = input("Enter the transaction details in below format:\n type(Expense/Income), amount, category, date(DD-MM-YYYY)\n")
 
    while not check_validation(user_input) == True:
        user_input = input("Enter the transaction details in below format:\n type(Expense/Income), amount, category, date(DD-MM-YYYY)\n")
        
    

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
    


   
