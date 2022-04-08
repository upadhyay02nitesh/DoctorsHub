from main import DBhelper

def main():
    
    while True:
        db=DBhelper()
        print("****************WELCOME TO DOCTORS HUB****************")
        print("PRESS 1 TO INSERT NEW USER")
        print("PRESS 2 TO DISPLAY USER USER")
        print("PRESS 3 TO DELETE USER")
        print("PRESS 4 TO UPDATE USER")
        print("EXIT THE PROGRAM")
        print()
        
        try:
            choice=int(input("Enter your key->"))
            if (choice==1):
                userid=int(input("Enter id"))
                Username=input("Enter your Name :->")
                Mobile=int(input("Enter Mobile Number:"))
                Address=input("Enter the Address -:")
                Specialist=input("Enter the Speciality of Doctors -:")
                Fees=int(input("Enter the Fees :"))
                time=int(input("Enter the Doctor's Time :"))
                
                db.insert_user(userid,Username,Mobile ,Address,Specialist,Fees,time)
            elif (choice==2):
                # display user
                db.fetch_all()
            elif (choice==3):
                id=int(input("Enter your userid :"))
                db.delete_user(id)
            elif (choice==4):
                Userid=int(input("Enter the id :"))
                Username=input("Enter name :")
                Mobile=int(input("Enter Mobile Number:"))
                Address=input("Enter the Address -:")
                Specialist=input("Enter the Speciality of Doctors -:")
                Fees=int(input("Enter the Fees :"))
                db.update_user(Userid,Username,Mobile ,Address,Specialist,Fees)
            elif (choice==5):
                # quit program
                break
            else:
                print("INVALID INPUT !!!!")
        except Exception as e:
            print(e)
            print("INVALID INPUT !!!")
if __name__=="__main__":
    main()
            