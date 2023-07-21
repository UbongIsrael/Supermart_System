admin_dic= {"master":3302, "test1": 2022} #add or edit the admins and passcodes from here
login_state = 0
name = ""
txn_id = 0
def admin_auth ():
    """
    Funtion handles the admins authentication \n
    in the login system.\n
    Returns the name of the currently logged in user. 
    """
    global login_state
    global name
    while login_state == 0:
        name = input("Whats your name: ")
        password = int(input("Enter Password: "))
        if name in admin_dic and admin_dic[name] == password:
            print(f"\
                  Logged In!, Welcome {name.upper()}")
            login_state = 1
        else: 
            print("Invalid Cred")
    return name


def new_admin(name = admin_auth()):
    """
    This function is for setting a new admin \n
    Can only be used by the master admin\n

    Would work best if admin details are stored on a database
    """
    if name == "master":
        new_ad = input("Input new admin name: ")
        new_ad_pass = int(input("Input new admin pasword: "))
        admin_dic[new_ad] = new_ad_pass
        print("New Admin SET!")
    else:
        print("Current Admin can't use this command!")

def digit(no, error):
    """
    Funtion is used to ensure a digit is passed.\n
    Returns the passed digit.
    Parameters:
        no: number
        error: Error message
    """
    while True:
      if no.isdigit():
         no = int(no)
         break
      else:
         no = input(f"\nInput a valid {error}: ")
    return no

def price_calc():
    """
    Gets the name, unit price and quantity of the product \n
    Then it calculates the total cost and adds it to the
    invoice dictionary. \n
    Total cost of products are generated and printed.
    """
    total = 0
    invoice_dic = {}
    global txn_id
    txn_id+=1
    print("\n        Input Product name, unit price and quantity")
    while True:
        prod= input("\nProduct name: ")
        if prod == "done":
            break
        unit_price = digit(input("Enter unit price: "), "unit price")
        quant = digit(input("Enter quantity: "), "quantity")
        sum = unit_price * quant
        total = total + sum
        invoice_dic[prod] = [f"{unit_price}             {quant}               {sum}"]
        print("Next, Type 'done' when through. ")

    invoice_head = f"""\
                             INVOICE DETAILS
        ADMIN - {admin_auth()}
        TRANSACTION ID - {txn_id}
                ITEMS         PRICE($)    QUANTITY(PCS)   TOTAL($)
    """
    print(invoice_head)
    for id, items in invoice_dic.items():

        print(f"                 {id}-------- {items}") 
    print(f"\n                 TOTAL------------------------------------${total}")
    
    

# BEGINING OF PROGRAM RUN
admin_auth()
print("""\n
                    MY CUSTOM SUPERMARKET DASHBOARD
""")
while True:
    print("\n ENTER 'A' FOR PRICE COLLECTION, 'B' TO ADD NEW ADMIN, 'C' TO END PROGRAM")
    new_input = input("a, b or c: ").lower()
    if new_input == "a" :
        price_calc()
    elif new_input == "b":
        new_admin()
    elif new_input == 'c':
        exit()
    else:
        print("Invalid Response")