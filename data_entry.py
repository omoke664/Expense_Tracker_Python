from datetime import datetime
date_format = "%d-%m-%Y" 
CATEGORIES = {"I": 'Income', "E": "Expense"}

def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str: #if nothing is specified, default to current date
        return datetime.today().strftime(date_format)
    try:
        vaild_date = datetime.strptime(date_str, date_format) #converting date to specified format
        return vaild_date.strftime(date_format)
    except ValueError:
        print("Invalid date format, Please Enter the date in dd-mm-yyyy format.")
        return get_date(prompt, allow_default)

def get_amount():
    try:
        amount  = float(input("Enter the amount:"))
        if amount <= 0:
            raise ValueError("Amount must be a non-negative non-zero value.")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter the category ('I' for income or 'E' for Expense):").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    
    print("invalid cateogry, Please enter 'I' for income of 'E' for Expense")
    return get_category()

def get_description():
    return input("Enter a Description (optional)")

