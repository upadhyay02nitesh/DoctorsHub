# THIS IS DOCTORS HUB PROJECT USING PYTHON WITH MYSQL DATABASE
# THIS IS MAIN FILE

import mysql.connector as con
class DBhelper:
    def __init__(self):
        self.con=con.connect(host='localhost',     
                  user="root",
                  password="Rewa1234",
                  database='pythontest')
        query='create table if not exists Doctors(Userid int not null primary key,Username varchar(24),Mobile  int,Address text,Specialist varchar(30),Fees int,time TIME)'
        cur=self.con.cursor()
        cur.execute(query)
        print("Table created")
    def insert_user(self,Userid,Username,Mobile ,Address,Specialist,Fees,time):
        query="insert into Doctors(Userid,Username,Mobile ,Address,Specialist,Fees,time) Values('{}','{}','{}','{}','{}','{}','{}')".format(Userid,Username,Mobile ,Address,Specialist,Fees,time)
        # print(query)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("insertion done!!")
    def fetch_all(self):
        query="select * from Doctors"
        cur=self.con.cursor()
        cur.execute(query)
        for i in cur:
            # print(i)
            print("Userid :",i[0])
            print("Name :",i[1])
            print("Mobile Number :",i[2])
            print("Address :",i[3])
            print("Specialist For :",i[4])
            print("Fee :",i[5])
            print("Time :",i[6])
            print()
    def delete_user(self,id):
        query="delete from Doctors where userid={}".format(id)
        cur=self.con.cursor()
        cur.execute(query) 
        print("Deleted")
    def update_user(self,Userid,Username,Mobile,Address,Specialist,Fees):
        query="update Doctors set Username='{}',Mobile ='{}',Address='{}',Specialist='{}', Fees='{}'where Userid={}".format(Username,Mobile ,Address,Specialist,Fees,Userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
d=DBhelper()



