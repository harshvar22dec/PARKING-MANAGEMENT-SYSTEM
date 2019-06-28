from datetime import datetime as time
def security_password():#this function is built for security
    obj=open('encryption.txt','r')
    curr_pass=obj.read()
    obj.close()
    if input('Enter Desktop Password\t')==curr_pass:return True
    else:print('Wrong Password, Process Failed');return False

def confirmation_passw():
    '''this function is built for confirmation:if user made any mistake,that mistake could be cleared
    before consideration'''
    obj = open('encryption.txt', 'r')
    curr_pass = obj.read()
    obj.close()
    if input('Confirm Desktop Password\t') == curr_pass:
        return True
    else:
        print('Wrong Password, Process Failed');return False

def change_password():#this function is access when you type "access":if yo forgot password, it handles
    obj=open('encryption.txt','r')
    curr_pwd=obj.read();obj.close()
    if input('Enter Current Password\t')==curr_pwd and obj.closed and confirmation_passw():
        new_pwd=input('Enter New Password\t')
        obj=open('encryption.txt','w')
        obj.write(new_pwd)
        return print('Successfully Done!')
    else:print('Wrong Password,Try Again!')

def entry():
    if security_password():
        obj=open('data.txt','a')
        veh_no=input('Enter Vehicle No.\t').replace(' ','').upper()
        owner=input('Enter Owner Name as mentioned on any Id or Aadhar Card\t').title()
        veh_name=input('Enter Vehicle Full Name\t').upper()
        veh_type=input('Enter type of vehicle\t').upper()
        if confirmation_passw():
            obj.write(veh_no+'%*'+owner+"%*"+veh_name+'%*'+veh_type+'%*'+'Entered'+'%*'+str(time.now())[:-7]+'\n')
            print('Successfully Entered\n')

def outing():
    if security_password():
        obj=open('data.txt','a')
        veh_no=input('Enter Vehicle No.\t').replace(' ','').upper()
        owner=input('Enter Owner Name as mentioned on any Id or Aadhar Card\t').title()
        veh_name=input('Enter Vehicle Full Name\t').upper()
        veh_type=input('Enter type of vehicle\t').upper()
        if confirmation_passw():
            obj.write(veh_no+'%*'+owner+"%*"+veh_name+'%*'+veh_type+'%*'+'Outed'+'%*'+str(time.now())[:-7]+'\n')
            print('Successfully Outed\n')
def enquiry():
    print("\tWelcome in enquiry\n\t\tverify it's you")
    if security_password():
        activity=input('press C to change your password\npress E to enquire a vehicle\t').upper()
        if activity=='C':change_password()
        elif activity=='E' and confirmation_passw():
            veh_no=input('Enter vehicle No.\t').replace(' ','').upper()
            obj=open('data.txt','r')
            veh_data=obj.readlines();found=0
            print('=_='*30)
            for i in veh_data:
                if i.startswith(veh_no) and i.split('%*')[0]==veh_no:print('[~'+i.replace('%*',' ->')[:-1]);found=1
            obj.close()
            print('=_=' *30)
            print('Done!') if found==1 else print('\n[There is not any activity of this vehicle]\n')
        else:print('Wrong Entry\t')