##### Terminal / Command line (run Python scripts & shell basics) #####

##1. pwd --> prints currect directory

##2. ls *.py --> lists all .py files in current folder

##3. Printing Username In Terminal
#import getpass
#try:
    #username = getpass.getuser()
#except:
    #username = "unknown"
#print(f"Logged in as: {username}")

##4. searching for strings in files
#import re
#def search_string(string, file_name):
    #with open(file_name, 'r') as file:
        #for num, line in enumerate(file, start=1):
            #if string in line: 
                #print(f"{num}: {line.strip()}")



##5. (GO BACK TO 3-5 TMR)
#def snake_case(string):
    #string = string.lower()
    #string = string.replace(" ", "_")
    #print(string)

#snake_case("Report Final.pdf")

##### Strings & variables #####

##6. Personalied Greeting
#name = input("Enter your name: ")
#print(f"Hello, {name}!")

##7. Email Username & Domain
#email = "alex.lee@company.com"
#print(f"uername: {email.split('@')[0]} \ndomian: {email.split('@')[1]}")

##8. Convert a Title to a URL Slu
#import string
#title = "My First Blog Post!!!"
#clean_title = title.translate(str.maketrans('', '', string.punctuation)).lower().replace(" ", "-")
#print(clean_title)

##9. Mask a Credit Card
#def mask_card(card):
    #parts = card.split(" ")
    #for i in range(len(parts) - 1):
        #parts[i] = "****"
    #return " ".join(parts)

#card = "4111 1111 1111 1111" 
#print(mask_card(card))

##10. Safe Template Fill
def fill_template(template, info):
    output_string = template.format(**info)
    return(output_string)
template = "Dear {first} {last}, your order {order_id} ships on {date}."
info = {"first": "Maya", "last": "Patel", "order_id": "A123", "date": "2025-10-23"}
print(fill_template(template,info))

##### Data Types & Math Operators #####
##1. Total Bill Calculator
def Calculate_total(bill,tip):
    total = bill + tip
    return (f"{total:.2f}")
#print(Calculate_total(50,0.18))

##2. BMI Calculator
def Calculate_BMI(weight_kg, height_m):
    BMI = weight_kg/(height_m ** 2)
    return (f"{BMI:.1f}")
print(Calculate_BMI(70, 1.75))
