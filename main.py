from crud_employee import create_employee,read_employee,update_employee,delete_employee
#from data_science import
count=3
while(count!=0):
    userName=input("Enter the user name=")
    password=input("Enter the password=")
    if(userName=="aa" and password=="123"):
        print("---------EMPLOYEE LOGIN SUCCESSFULLY----------")
        #count=1
        cnt=1
        while(cnt!=0):
            print("Employee Management system")
            print("1.create")
            print("2.read")
            print("3.update")
            print("4.delete")
            print("5.exit")
            ch=input("Enter your choice:")
            if ch=='1':
                id=input("enter the employee ID:")
                name=input("Enter the employee name:")
                salary=input("Enter the employee salary:")
                city=input("Enter the employee city:")
                designation=input("Enter the employee designation:")
                create_employee(id,name,salary,city,designation)

            if ch=='2':
                read_employee()
            if ch=='3':
                id=input("enter the employee ID:")
                name=input("Enter the employee name:")
                salary=input("Enter the employee salary:")
                city=input("Enter the employee city:")
                designation=input("Enter the employee designation:")
                update_employee(id,name or None,salary or None,city or None,designation or None)
            if ch=='4':
                id=input("Enter the employee ID:")
                delete_employee(id)
            if ch=='5':
                cnt=0
            else:
                print("Invalid Choice...please try again")
    elif(userName!="arya" and password!="arya123"):
        count-=1
        print("userName and password are incorrect")
    elif(userName!="arya"):
        count-=1
        print("userName is incorrect")
    elif(password!="arya123"):
        count-=1
        print("password is incorrect")
    if(count==0):
        print("Remaining attempt to login employee=",count)    



                        