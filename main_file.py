import mysql.connector as mysql

try:

#Table Details

    def table():     
         
        
        db=mysql.connect(host="localhost",user="root",password="root",database=b)
        cursor=db.cursor()
        cursor.execute("CREATE TABLE Company_details (Company_ID VARCHAR(100) NOT NULL PRIMARY KEY,Name VARCHAR(100),Email_Address VARCHAR(100),Phone_number VARCHAR(16))")
        cursor.execute("CREATE TABLE Customer (Customer_ID VARCHAR(100) NOT NULL PRIMARY KEY,Name VARCHAR(100),Phone_Number VARCHAR(16),Email_Address VARCHAR(100))")
        cursor.execute("CREATE TABLE Goods (Product_ID VARCHAR(100) NOT NULL PRIMARY KEY,Name VARCHAR(100),Description VARCHAR(255),Type VARCHAR(50))")
        
        cursor.execute("CREATE TABLE Product (Product_ID VARCHAR(100),QTY VARCHAR(10),Purchase_date DATE,Customer_ID VARCHAR(100),CONSTRAINT fk_Customer FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID) ON UPDATE CASCADE ON DELETE CASCADE)")
        cursor.execute("ALTER TABLE Product ADD CONSTRAINT fk_Customer2 FOREIGN KEY (Product_ID) REFERENCES Goods(Product_ID) ON UPDATE CASCADE ON DELETE CASCADE")

        cursor.execute("CREATE TABLE Stocks (Product_ID VARCHAR(100),Initial_Stock VARCHAR(100),Stock_Sold VARCHAR(255),Company_ID VARCHAR(100),CONSTRAINT fk_Company_details FOREIGN KEY (Company_ID) REFERENCES Company_details(Company_ID) ON UPDATE CASCADE ON DELETE CASCADE)")   
        cursor.execute("ALTER TABLE Stocks ADD CONSTRAINT fk_Goods1 FOREIGN KEY (Product_ID) REFERENCES Goods(Product_ID) ON UPDATE CASCADE ON DELETE CASCADE")
        cursor.execute("CREATE TABLE Cus_Payment_ID (Amount VARCHAR(100),Invoice_code VARCHAR(100),Customer_ID VARCHAR(100),CONSTRAINT fk_Customer1 FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID) ON UPDATE CASCADE ON DELETE CASCADE)")
        
        cursor.execute("CREATE TABLE Com_payment_ID (Amount VARCHAR(100),Invoice_code VARCHAR(255),Company_ID VARCHAR(100),CONSTRAINT fk_Company_details1 FOREIGN KEY (Company_ID) REFERENCES Company_details(Company_ID) ON UPDATE CASCADE ON DELETE CASCADE)")
     
        db.commit()
        f()

    def databaseshow():
        import mysql.connector as mysql
        db=mysql.connect(host="localhost",username="root",passwd="root")
        cursor=db.cursor()
        cursor.execute("SHOW DATABASES")
        recset=cursor.fetchall()
        for database in recset:
            print(database)

        z()

#Main Function

    #Table Selection
    
    def f():
       
        print("\nPlease Select the Table to be edited")
        print("1.Customer")
        print("2.Company details")
        print("3.Main Product Information")
        print("4.Sales")
        print("5.Payment Information")
        print("6.Exit")
        
        pd1=int(input("Enter  a choice: "))
        
        while pd1>=1 and pd1<=5:

            #Customer Table
            
            if(pd1==1):
                print("\n1.Add New Customer")
                print("2.Delete a Customer")
                print("3.Display a Customer")
                print("4.Edit a Customer")
                print("5.Move to main")
                pd11=int(input("Enter  a choice: "))

                #Adding Data
                
                if pd11==1:
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",user="root",password="root",database=b)
                    cursor=db.cursor()
                    a=int(input("enter the no of Records you want to add: "))
                    for i in range(a):
                        ax=input("enter the customer ID: ")
                        
                        az=input("enter the customer name: ")
                        bx=int(input("enter the phone number: "))
                        by=input("enter the email address: ")
                        A="INSERT INTO customer VALUES(%s,%s,%s,%s)"
                        B=(ax,az,bx,by)
                        cursor.execute(A,B)
                        db.commit()
                        print(cursor.rowcount,"RECORD INSERTED")

                #Deleting Data
                        
                elif pd11==2:
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                    cursor=db.cursor()
                    ax=input("Enter the Customer ID to be deleted: ")
                    A="DELETE FROM Customer WHERE Customer_ID=%s"
                    B=(ax,)
                    cursor.execute(A,B)
                    db.commit()
                    print(cursor.rowcount,"Record Deleted")

                #Displaying Data    

                elif pd11==3:
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                    cursor=db.cursor()
                    cursor.execute("select * from customer")
                    recset=cursor.fetchall()
                    for table in recset:
                        print(table)
                
                #Editing Data
                        
                elif (pd11==4):
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",user="root",password="root",database=b)
                    cursor=db.cursor()
                    print('edit customer info')
                    print('1. edit name')
                    print('2. edit phone number')
                    print('3. edit email address')
                    xc=int(input("enter a choice: "))

                    #Editing Name
                    
                    if xc==1:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",user="root",password="root",database=b)
                        cursor=db.cursor()
                        pl3=input("enter the customer id: ")
                        pl2=input("enter the new name: ")
                        
                        ok2="update customer set Name =%s WHERE Customer_ID =%s"
                        ij2=(pl2,pl3)
                        cursor.execute(ok2,ij2)
                        db.commit()
                    
                    #Editing Phone

                    elif xc==2:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",user="root",password="root",database=b)
                        cursor=db.cursor()
                        pl3=input("enter the customer id: ")
                        pl2=input("enter the phone number: ")
                        ok2="update customer set Phone_Number =%s WHERE Customer_ID =%s"
                        ij2=(pl2,pl3)
                        cursor.execute(ok2,ij2)
                        db.commit()

                    #Editing Mail
                        
                    elif xc==3:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",user="root",password="root",database=b)
                        cursor=db.cursor()
                        pl3=input("enter the customer id: ")
                        pl2=input("enter the email address: ")
                        ok2="update customer set Email_Address =%s WHERE Customer_ID =%s"
                        ij2=(pl2,pl3)
                        cursor.execute(ok2,ij2)
                        db.commit()

                #Going Back
                        
                elif pd11==5:
                    
                    f()
                    
            #Payment Info.
                    
            elif(pd1==5):
              print("\n1.See Customer Payment")
              print("2.See Company Payment")
              print("3.Move to Main")
              
              aa=int(input("Enter Your Choice: "))

              #Customer Payment Table
              
              if(aa==1):
                  print("\n1.Add a Payment") 
                  print("2.Remove a Payment")
                  print("3.Modify a Payment")
                  print("4.Display a Payment")
                  print("5.Move to main")
                  pd11=int(input("Enter  a choice: "))

                  #Adding Data
                  
                  if pd11==1:
                      import mysql.connector as mysql
                      db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                      cursor=db.cursor()
                      a=int(input("enter the no of fields you want to add: "))
                      for i in range(a):
                          gx=input("enter the customer ID: ")
                          gy=input("enter the amount: ")
                          hx=input("enter the Invoice code: ")
                          G="INSERT INTO cus_payment_id VALUES(%s,%s,%s)"
                          H=(gy,hx,gx)
                          cursor.execute(G,H)
                          db.commit()
                          print(cursor.rowcount,"RECORD INSERTED")
                      
                  #Removing Data
                          
                  elif pd11==2:
                      import mysql.connector as mysql
                      db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                      cursor=db.cursor()
                      ax=input("Enter the Customer ID to be deleted: ")
                      A="DELETE FROM Cus_Payment_ID WHERE Customer_ID=%s"
                      B=(ax,)
                      cursor.execute(A,B)
                      db.commit()
                      print(cursor.rowcount,"Record Deleted")

                  #Editing Data
                      
                  elif pd11==3:
                      print('edit customer payment id')
                      print('1. edit amount')
                      print('2. edit invoice code')
                      nm=int(input("enter a choice: "))

                      #Editing Amount
                      
                      if nm==1:
                          import mysql.connector as mysql
                          db=mysql.connect(host="localhost",username="root",password="root",database=b)
                          cursor=db.cursor()
                          
                          
                          pl6=input("enter the customer id: ")
                          pl5=input("enter the amount to be changed: ")
                          
                          ok5="update cus_payment_id set Amount =%s WHERE Customer_ID =%s"
                          ij5=(pl5,pl6)
                          cursor.execute(ok5,ij5)
                          db.commit()

                      #Editing Invoice Id
                          
                      elif nm==2:
                          import mysql.connector as mysql
                          db=mysql.connect(host="localhost",username="root",password="root",database=b)
                          cursor=db.cursor()
                          pl6=input("enter the customer id: ")
                          pl5=input("enter the invoice code: ")
                          
                          ok5="update cus_payment_id set Invoice_code =%s WHERE Customer_ID =%s"
                          ij5=(pl5,pl6)
                          cursor.execute(ok5,ij5)
                          db.commit()

                  #Displaying Data    

                  elif pd11==4:
                                                          
                      import mysql.connector as mysql
                      db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                      cursor=db.cursor()
                      cursor.execute("select * from cus_payment_id")
                      recset=cursor.fetchall()
                      for table in recset:
                          print(table)           

                  #Going Back
                          
                  elif pd11==5:
                      
                      f()

              #Company Payment Table
                      
              elif(aa==2):
                  print("\n1.Add Payment")
                  print("2.Delete Payment")
                  print("3.Edit Payment")
                  print("4.Display Payment")
                  print("5.Move to main")
                  pd11=int(input("Enter  a choice: "))

                  #Adding Data
                  
                  if pd11==1:
                      import mysql.connector as mysql
                      db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                      cursor=db.cursor()
                      a=int(input("enter the no of fields you want to add: "))
                      for i in range(a):
                          ix=input("enter the company ID: ")
                          iy=input("enter the amount: ")
                          jx=input("enter the Invoice code: ")
                          I="INSERT INTO com_payment_id VALUES(%s,%s,%s)"
                          J=(iy,jx,ix)
                          cursor.execute(I,J)
                          db.commit()
                          print(cursor.rowcount,"RECORD INSERTED")

                  #Removing Data
                          
                  elif pd11==2:
                      import mysql.connector as mysql
                      db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                      cursor=db.cursor()
                      ax=input("Enter the Company ID to be deleted: ")
                      A="DELETE FROM Com_Payment_ID WHERE Company_ID=%s"
                      B=(ax,)
                      cursor.execute(A,B)
                      db.commit()
                      print(cursor.rowcount,"Record Deleted")

                  #Editing Data
                      
                  elif pd11==3:
                      
                      print('edit company payment id')
                      print('1. edit amount')
                      print('2. edit invoice code')
                      vb=int(input("enter a choice: "))

                      #Editing Amount
                      
                      if vb==1:
                          import mysql.connector as mysql
                          db=mysql.connect(host="localhost",user="root",password="root",database=b)
                          cursor=db.cursor()
                          
                          pl5=input("enter the company id: ")
                          pl4=input("enter the amount: ")
                          
                          ok4="update com_payment_id set Amount =%s WHERE Company_ID =%s"
                          ij4=(pl4,pl5)
                          cursor.execute(ok4,ij4)
                          db.commit()

                      #Editing Invoice code
                          
                      elif vb==2:
                          import mysql.connector as mysql
                          db=mysql.connect(host="localhost",user="root",password="root",database=b)
                          cursor=db.cursor()
                          pl5=input("enter the company id: ")
                          pl4=input("enter the invoice code: ")
                          
                          ok4="update com_payment_id set Invoice_code =%s WHERE Company_ID =%s"
                          ij4=(pl4,pl5)
                          cursor.execute(ok4,ij4)
                          db.commit()

                  #Display Data
                          
                  elif pd11==4:
                      import mysql.connector as mysql
                      db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                      cursor=db.cursor()
                      cursor.execute("select * from Com_Payment_ID")
                      recset=cursor.fetchall()
                      for table in recset:
                          print(table)

                  #Going Back
                          
                  elif pd11==5:    
                      f()        
              elif(aa==3):
                  f()



              
            #Company Details Table
                      
            elif(pd1==2):
                print("\n1.Add company details") 
                print("2.Edit company details")
                print("3.Display company details")
                print("4.Delete Company Details")
                print("5.Move to main")
                pd11=int(input("Enter  a choice: "))

                #Adding Data
                
                if pd11==1:
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                    cursor=db.cursor()
                    a=int(input("enter the no of Records you want to add: "))
                    for i in range(a):
                        
                        kx=input("enter the company ID: ")
                        ky=input("enter the company name: ")
                        kz=input("enter the email address: ")
                        lx=input("enter the phone number: ")
                        K="INSERT INTO Company_Details VALUES(%s,%s,%s,%s)"
                        L=(kx,ky,kz,lx)
                        cursor.execute(K,L)
                        db.commit()
                        print(cursor.rowcount,"RECORD INSERTED")

                #Editing Data
                        
                elif pd11==2:
                    
                    print('edit company details')
                    print('1. edit name')
                    print('2. edit email address')
                    print('3. edit phone number')
                    bn=int(input("enter a choice: "))

                    #Edit Name
                    
                    if bn==1:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",user="root",password="root",database=b)
                        cursor=db.cursor()
                        
                        pl5=input("enter the company id: ")
                        pl6=input("enter the name: ")
                        
                        ok6="update Company_Details set Name =%s WHERE Company_ID =%s"
                        ij6=(pl6,pl5)
                        cursor.execute(ok6,ij6)
                        db.commit()

                    #Edit mail
                        
                    elif bn==2:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",user="root",password="root",database=b)
                        cursor=db.cursor()
                        pl5=input("enter the company id: ")
                        pl6=input("enter the email address: ")
                        
                        ok6="update Company_Details set Email_Address =%s WHERE Company_ID =%s"
                        ij6=(pl6,pl5)
                        cursor.execute(ok6,ij6)
                        db.commit()

                    #Edit Phone
                        
                    elif bn==3:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",user="root",password="root",database=b)
                        cursor=db.cursor()
                        pl5=input("enter the company id: ")
                        pl6=input("enter the phone number: ")
                        
                        ok6="update Company_Details set Phone_number =%s WHERE Company_ID =%s"
                        ij6=(pl6,pl5)
                        cursor.execute(ok6,ij6)
                        db.commit()

                #Display Data
                        
                elif pd11==3:
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                    cursor=db.cursor()
                    cursor.execute("select * from Company_Details")
                    recset=cursor.fetchall()
                    for table in recset:

                        print(table)

                #Removing Data
                        
                elif pd11==4:
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                    cursor=db.cursor()
                    ax=input("Enter the Company ID to be deleted: ")
                    A="DELETE FROM Company_Details WHERE Company_ID=%s"
                    B=(ax,)
                    cursor.execute(A,B)
                    db.commit()
                    print(cursor.rowcount,"Record Deleted")
                    
                #Going Back
                    
                elif pd11==5:
                    f()

            #Sales
                    
            elif(pd1==4):
                print("\n1. See Customer Payment: ")
                print("2. See Company Payment: ")
                aa=int(input("Enter Your Choice: "))

                #Customer Payment Table
                
                if(aa==1):
                    
                  print("\n1.Add an item") 
                  print("2.Remove an item")
                  print("3.Modify an item")
                  print("4.Display an item")
                  print("5.Move to main")
                  pd11=int(input("Enter  a choice: "))

                  #Adding Data
                  
                  if pd11==1:
                      import mysql.connector as mysql
                      db=mysql.connect(host="localhost",username="root",password="root",database=b)
                      cursor=db.cursor()
                      a=int(input("enter the no of fields you want to add: "))
                      for i in range(a):
                          cx=input("enter the product ID: ")
                          
                          cz=input("enter the Quantity: ")
                          dx=input("enter the Purchase Date: ")
                          dy=input("enter the Customer ID: ")
                          C="INSERT INTO Product VALUES(%s,%s,%s,%s)"
                          D=(cx,cz,dx,dy)
                          cursor.execute(C,D)
                          db.commit()
                          print(cursor.rowcount,"RECORD INSERTED")

                  #Removong Data
                          
                  elif pd11==2:
                      import mysql.connector as mysql
                      db=mysql.connect(host="localhost",username="root",password="root",database=b)
                      cursor=db.cursor()
                      ax=input("Enter the PRODUCT ID to be deleted: ")
                      A="DELETE FROM Product WHERE Product_ID=%s"
                      B=(ax,)
                      cursor.execute(A,B)
                      db.commit()
                      print(cursor.rowcount,"Record Deleted")

                  #Editing Data
                      
                  elif (pd11==3):
                      
                      print('edit product info')
                      print('1. edit Quantity')
                      print('2. edit Purchase Date')
                      
                      cv=int(input("enter a choice: "))
                     
                      #Edit Quantity
                      
                      if cv==1:
                          import mysql.connector as mysql
                          db=mysql.connect(host="localhost",username="root",password="root",database=b)
                          cursor=db.cursor()
                          cursor.execute("ALTER TABLE product drop foreign key fk_customer2")
                          cursor.execute("ALTER TABLE product drop foreign key fk_customer")
                          cursor.execute("ALTER TABLE product drop key fk_customer")
                          cursor.execute("ALTER TABLE product drop key fk_customer2")
                          pl6=input("enter the product id: ")
                          pl3=input("enter the New Quantity: ")
                          ok3="update product set QTY =%s WHERE Product_ID =%s"
                          ij3=(pl3,pl6)
                          cursor.execute(ok3,ij3)
                          db.commit()
                          cursor.execute("ALTER TABLE Product ADD CONSTRAINT fk_Customer2 FOREIGN KEY (Product_ID) REFERENCES Goods(Product_ID) ON UPDATE CASCADE ON DELETE CASCADE")
                          cursor.execute("ALTER TABLE Product ADD CONSTRAINT fk_Customer FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID) ON UPDATE CASCADE ON DELETE CASCADE")
                          db.commit()
                          print("Record Updated")
                          

                      #Edit Purchase Date
                          
                      elif cv==2:
                          import mysql.connector as mysql
                          db=mysql.connect(host="localhost",user="root",password="root",database=b)
                          cursor=db.cursor()
                          cursor.execute("ALTER TABLE product drop foreign key fk_customer2")
                          cursor.execute("ALTER TABLE product drop foreign key fk_customer")
                          cursor.execute("ALTER TABLE product drop key fk_customer")
                          cursor.execute("ALTER TABLE product drop key fk_customer2")
                          pl6=input("enter the product id: ")
                          pl3=input("enter the New Purchase Date: ")
                          ok3="update product set Purchase_date =%s WHERE Product_ID =%s"
                          ij3=(pl3,pl6)
                          cursor.execute(ok3,ij3)
                          db.commit()
                          cursor.execute("ALTER TABLE Product ADD CONSTRAINT fk_Customer2 FOREIGN KEY (Product_ID) REFERENCES Goods(Product_ID) ON UPDATE CASCADE ON DELETE CASCADE")
                          cursor.execute("ALTER TABLE Product ADD CONSTRAINT fk_Customer FOREIGN KEY (Customer_ID) REFERENCES Customer(Customer_ID) ON UPDATE CASCADE ON DELETE CASCADE")
                          db.commit()
                          print("Record Updated")
                  #Display Data
                          
                  elif pd11==4:
                      import mysql.connector as mysql
                      db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                      cursor=db.cursor()
                      cursor.execute("select * from Product")
                      recset=cursor.fetchall()
                      for table in recset:
                          print(table)

                  #Going Back
                          
                  elif pd11==5:
                      f()

                #Company Payment Table
                      
                elif(aa==2):
                    print("\n1.Add Product ID")
                    print("2.Delete Product ID")
                    print("3.Edit Product ID")
                    print("4.Display Product ID")
                    print("5.Move to main")
                    pd11=int(input("Enter  a choice: "))

                    #Adding Data
                    
                    if pd11==1:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                        cursor=db.cursor()
                        a=int(input("enter the no of fields you want to add: "))
                        for i in range(a):      
                            ex=input("enter the company ID: ")
                            ey=input("enter the Product ID: ")
                            ez=input("enter the Initial Stock: ")
                            fx=input("enter the stocks sold: ")
                            
                            E="INSERT INTO stocks VALUES(%s,%s,%s,%s)"
                            F=(ey,ez,fx,ex)
                            cursor.execute(E,F)
                            db.commit()
                            print(cursor.rowcount,"RECORD INSERTED")

                    #Removing Data
                            
                    elif pd11==2:                       
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                        cursor=db.cursor()
                        ax=input("Enter the PRODUCT ID to be deleted: ")
                        A="DELETE FROM Stocks WHERE Company_ID=%s"
                        B=(ax,)
                        cursor.execute(A,B)
                        db.commit()
                        print(cursor.rowcount,"Record Deleted")

                    #Editing Data
                        
                    elif pd11==3:
                        print('edit stock info')
                        print('1. edit initial stock')
                        print('2. edit stock sold')
                        
                        zx=int(input("enter a choice: "))

                        #Edit Initial Stock
                            
                        if zx==1:
                            import mysql.connector as mysql
                            db=mysql.connect(host="localhost",user="root",password="root",database=b)
                            cursor=db.cursor()
                            cursor.execute("ALTER TABLE stocks drop foreign key fk_Company_details")
                            cursor.execute("ALTER TABLE stocks drop foreign key fk_Goods1")
                            cursor.execute("ALTER TABLE stocks drop key fk_Goods1")
                            cursor.execute("ALTER TABLE stocks drop key fk_Company_details")
                            
                            pl5=input("enter the company id: ")
                            pl=input("enter the inital stock: ")
                            ok="update stocks set Initial_Stock =%s WHERE Company_ID =%s"
                            ij=(pl,pl5)
                            cursor.execute(ok,ij)
                            db.commit()
                            cursor.execute("ALTER TABLE Stocks ADD CONSTRAINT fk_Goods1 FOREIGN KEY (Product_ID) REFERENCES Goods(Product_ID) ON UPDATE CASCADE ON DELETE CASCADE")
                            cursor.execute("ALTER TABLE stocks ADD CONSTRAINT fk_Company_details FOREIGN KEY (Company_ID) REFERENCES Company_details(Company_ID) ON UPDATE CASCADE ON DELETE CASCADE")
                            db.commit()
                            print("Record Updated")

                        #Edit Stock Sold
                            
                        elif zx==2:
                            import mysql.connector as mysql
                            db=mysql.connect(host="localhost",user="root",password="root",database=b)
                            cursor=db.cursor()
                            cursor.execute("ALTER TABLE stocks drop foreign key fk_Company_details")
                            cursor.execute("ALTER TABLE stocks drop foreign key fk_Goods1")
                            cursor.execute("ALTER TABLE stocks drop key fk_Goods1")
                            cursor.execute("ALTER TABLE stocks drop key fk_Company_details")
                            pl5=input("enter the company id: ")
                            pl=input("enter the stock sold: ")
                            ok="update stocks set Stock_Sold =%s WHERE Company_ID =%s"
                            ij=(pl,pl5)
                            cursor.execute(ok,ij)
                            db.commit()
                            cursor.execute("ALTER TABLE Stocks ADD CONSTRAINT fk_Goods1 FOREIGN KEY (Product_ID) REFERENCES Goods(Product_ID) ON UPDATE CASCADE ON DELETE CASCADE")
                            cursor.execute("ALTER TABLE stocks ADD CONSTRAINT fk_Company_details FOREIGN KEY (Company_ID) REFERENCES Company_details(Company_ID) ON UPDATE CASCADE ON DELETE CASCADE")
                            db.commit()
                            print("Record Updated")

                        

                    #Display Data
                            
                    elif pd11==4:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                        cursor=db.cursor()
                        cursor.execute("select *,Initial_Stock - Stock_Sold as Stock_Left from stocks")
                        recset=cursor.fetchall()
                        for table in recset:
                            print(table)

                    #Going Back
                            
                    elif pd11==5:
                        f()

            #Main Product Info. Table
                        
            if(pd1==3):
                
                print("\n1.Add New Product")
                print("2.Delete a Product")
                print("3.Display a Product")
                print("4.Edit a Product")
                print("5.Move to main")
                pd11=int(input("Enter  a choice: "))

                #Adding Data
                
                if pd11==1:
                    
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",user="root",password="root",database=b)
                    cursor=db.cursor()
                    a=int(input("enter the no of Records you want to add: "))
                    for i in range(a):
                        
                        ty=input("enter the Product ID: ")
                        tg=input("enter the Product Name: ")
                        th=input("enter the Product Description: ")
                        tu=(input("enter the Product Type: "))
                        
                        A="INSERT INTO Goods VALUES(%s,%s,%s,%s)"
                        B=(ty,tg,th,tu)
                        cursor.execute(A,B)
                        db.commit()
                        print(cursor.rowcount,"RECORD INSERTED")

                #Removing Data
                        
                elif pd11==2:
                    
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                    cursor=db.cursor()
                    ax=input("Enter the Product ID to be deleted: ")
                    A="DELETE FROM Goods WHERE Product_ID=%s"
                    B=(ax,)
                    cursor.execute(A,B)
                    db.commit()

                    print(cursor.rowcount,"Record Deleted")
                    
                #Display Data
                    
                elif pd11==3:
                    
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",username="root",passwd="root",database=b)
                    cursor=db.cursor()
                    cursor.execute("select * from Goods")
                    recset=cursor.fetchall()
                    for table in recset:
                        
                        print(table)

                #Edit Data
                        
                elif (pd11==4):
                    
                    import mysql.connector as mysql
                    db=mysql.connect(host="localhost",user="root",password="root",database=b)
                    cursor=db.cursor()
                    print('Edit Product info')
                    print('1. edit name')
                    print('2. edit Description')
                    print('3. edit Type')
                    xc=int(input("enter a choice: "))

                    #Edit Name
                    
                    if xc==1:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",user="root",password="root",database=b)
                        cursor=db.cursor()
                        pl3=input("enter the Product id: ")
                        pl2=input("enter the new name: ")
                        
                        ok2="update Goods set Name =%s WHERE Product_ID =%s"
                        ij2=(pl2,pl3)
                        cursor.execute(ok2,ij2)
                        db.commit()

                    #Edit Desc.
                        
                    elif xc==2:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",user="root",password="root",database=b)
                        cursor=db.cursor()
                        pl3=input("enter the Product id: ")
                        pl2=input("enter the Description: ")
                        ok2="update Goods set Description =%s WHERE Product_ID =%s"
                        ij2=(pl2,pl3)
                        cursor.execute(ok2,ij2)
                        db.commit()

                    #Edit Type
                        
                    elif xc==3:
                        import mysql.connector as mysql
                        db=mysql.connect(host="localhost",user="root",password="root",database=b)
                        cursor=db.cursor()
                        pl3=input("enter the Product id: ")
                        pl2=input("enter the Type: ")
                        ok2="update Goods set Type =%s WHERE Product_ID =%s"
                        ij2=(pl2,pl3)
                        cursor.execute(ok2,ij2)
                        db.commit()

                #Going Back
                        
                elif pd11==5:
                    f()

        #Exit Code
                    
        while(pd1==6):
                
                print('Finished')
                exit()
        else:
            print("Please enter a number between 1 and 5")
            f()
    
    #Initial Code
            
    def z():
        global b
        ab=input("Do you want to create a New Database?(Y/N): ")
        if ab=="N" or ab=="n":
            import mysql.connector as mysql
            db=mysql.connect(host="localhost",username="root",passwd="root")
            cursor=db.cursor()
            b=input("Enter your database name: ")
            db=mysql.connect(host="localhost",user="root",passwd="root")
            f()
            
        elif ab=="Y" or ab=="y":
            import mysql.connector as mysql
            db=mysql.connect(host="localhost",user="root",passwd="root")
            cursor=db.cursor()       
            b=input("Enter the database name: ")
            cursor.execute("CREATE DATABASE "+ b)
            table()

    #Password Protection
            
    def a():
        i=1
        password=""
        while password!="**":
            if i<4:
                password=input("Enter the password: ")
                if password=="**":
                    databaseshow()
                elif(i<=2):
                    print("Please try again")
                    i=i+1
                elif i==3:
                    print("No more tries available")
                    break
                else:
                    break

    #Calling Code            
    a()

except:
    
    print("Please enter a NUMBER between 1 and  5")   
    f()  
