def insert_user(self,Userid,Username,Mobile No,Address,Specialist,Fees,time):
    #     query="insert into Doctors(Userid,Username,Mobile No,Address,Specialist,Fees,time) Values('{}','{}','{}','{}','{}','{}','{}')".format(Userid,Username,Mobile No,Address,Specialist,Fees,time)
    #     # print(query)
    #     cur=self.con.cursor()
    #     cur.execute(query)
    #     self.con.commit()
    #     print("insertion done!!")
    # def fetch_all(self):
    #     query="select * from Doctors"
    #     cur=self.con.cursor()
    #     cur.execute(query)
    #     for i in cur:
    #         # print(i)
    #         print("Userid :",i[0])
    #         print("Name :",i[1])
    #         print("Mobile Number :",i[2])
    #         print("Address :",i[3])
    #         print("Specialist For :",i[4])
    #         print("Fee :",i[5])
    #         print("Time :",i[6])
    #         print()
    # def delete_user(self,id):
    #     query="delete from Doctors where userid={}".format(id)
    #     cur=self.con.cursor()
    #     cur.execute(query) 
    #     print("Deleted")
    # def update_user(self,Userid,Username,Mobile No,Address,Specialist,Fees,time):
    #     query="update Doctors set Username='{}',Mobile no='{}',Address='{}',Specialist='{}',Mobile Fees='{}',Time='{}' where Userid={}".format(Username,Mobile No,Address,Specialist,Fees,time,Userid)
    #     cur=self.con.cursor()
    #     cur.execute(query)
    #     self.con.commit()