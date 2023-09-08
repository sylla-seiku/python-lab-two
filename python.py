#learning about Comparison Operators
temperature = 35

if temperature > 30:
    print("It's a hot day.")
else:
    print("It's not a hot day.")

#practice 
name = "Seiku Sillah"

if len(name) < 3:
    print("Name must be at least 3 characters.")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters.")
else:
    print("Name looks good!")



'''
# Learning About Logical Operators
has_high_income = False
has_good_credit = True

if has_high_income and has_good_credit: # with the "and" operator bth conditions have to be true to run the message. but not with "or"
    print("Eligible for loan")

has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record: #"and not" operator 
    print("Eligible for loan")



# practice is based on if one has good credit they pay one price if not they pay another using "if statments"
price = 1000000
has_good_credit = True

if has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down payment: ${down_payment}')


#Learning if statments
is_hot = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
print("Enjoy your day")


is_hot = False
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
    
print("Enjoy your day")
'''