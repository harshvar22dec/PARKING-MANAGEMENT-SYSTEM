from funcdefin import *
while True:
    print('''\nWELCOME IN DHOLERA PARKING SERVICES
                 Press E to enter the vehicle
                  Press U to out the vehicle
                   Type system for Admin Services''')
    response=input('\t').upper()
    if response=='E':entry()
    elif response=='U':outing()
    elif response=='SYSTEM':enquiry()
    else:print('Wrong Entry\n')
