
from datetime import datetime
def check_validation(data):
    print(data)
    if not (data["type"] == "Expense" or data["type"] == "Income"):
        print("Transaction type is not valid")
    if data["amount"] < 0:
        print("Please enter a positive amount")
    
    try:
        datetime.strptime(data["date"], "%d-%m-%Y")
    except ValueError:
        print("Please input a correct date format")




