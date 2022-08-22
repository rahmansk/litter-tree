import sys
import datetime

print("""

                                                                                          
 ,dPYb,        I8      I8                        I8                                        
 IP'`Yb        I8      I8                        I8                                        
 I8  8I  gg 8888888888888888                  88888888                                     
 I8  8'  ""    I8      I8                        I8                                        
 I8 dP   gg    I8      I8    ,ggg,    ,gggggg,   I8    ,gggggg,   ,ggg,    ,ggg,    ,ggg,  
 I8dP    88    I8      I8   i8" "8i   dP""""8I   I8    dP""""8I  i8" "8i  i8" "8i  i8" "8i 
 I8P     88   ,I8,    ,I8,  I8, ,8I  ,8'    8I  ,I8,  ,8'    8I  I8, ,8I  I8, ,8I  I8, ,8I 
,d8b,_ _,88,_,d88b,  ,d88b, `YbadP' ,dP     Y8,,d88b,,dP     Y8, `YbadP'  `YbadP'  `YbadP' 
8P'"Y888P""Y88P""Y8  8P""Y8888P"Y8888P      `Y88P""Y88P      `Y8888P"Y888888P"Y888888P"Y888


""")

now = datetime.datetime.now()

print(now.strftime('Current Date: %d-%m-%y'))
print(now.strftime('Time: %H:%M:%S on %A, %B %dth, %Y\n'))


uni = input("Enter University/College/PU Name : ")
print("Hello " + uni + " " + "Student !!")


srn = input("\nEnter Your SRN / Reg No /Application No : ")
print(f"Entry Allowed to {srn}")


name = input("\nWhat is your First name: ")
surname = input("And your Last name: ")
print("\nHello", name, surname)


def arithmetic():

    while True:
    
        print("""
                   __         __     __  _             
         _______ _/ /_____ __/ /__ _/ /_(_)__  ___  ___
        / __/ _ `/ / __/ // / / _ `/ __/ / _ \/ _ \(_-<
        \__/\_,_/_/\__/\_,_/_/\_,_/\__/_/\___/_//_/___/
        

        """)

        a = int(input("Enter First Number: "))
        b = int(input("Enter Second Number: "))

        print("""

        Choose An Option:
        
        a) ADD
        b) SUB
        c) MUL
        d) DIV
        e) MOD
        f) EXP
        g) FLOOR
        
        """)

        arithmetic = str(input("\nSelect Option: "))

        if arithmetic == "a" or arithmetic == "ADD" or arithmetic == "add" or arithmetic == "1":
            print("\nAddition Operator")
            add = a + b
            print(f"A + B = {add}")

        elif arithmetic == "b" or arithmetic == "SUB" or arithmetic == "sub" or arithmetic == "2":
            print("\nSubraction Operator")
            sub = a - b
            print(f"A - B = {sub}")

        elif arithmetic == "c" or arithmetic == "MUL" or arithmetic == "mul" or arithmetic == "3" :
            print("\nMultiplication Operator")
            mul = a * b
            print(f"A * B = {mul}")

        elif arithmetic == "d" or arithmetic == "DIV" or arithmetic == "div" or arithmetic == "4":
            print("\nDivision Operator")
            div = a / b
            print(f"A / B = {div}")

        elif arithmetic == "e" or arithmetic == "MOD" or arithmetic == "mod" or arithmetic == "5":
            print("\nModulus Operator")
            mod = a % b
            print(f"A % B = {mod}")

        elif arithmetic == "f" or arithmetic == "EXP" or arithmetic == "exp" or arithmetic == "6":
            print("\nExponentation Operator")
            exp = a ** b
            print(f"A ** B = {exp}")

        elif arithmetic == "g" or arithmetic == "FLOOR" or arithmetic == "floor" or arithmetic == "7":
            print("\nFloor Division")
            floor = a / b
            print(f"A / B = {floor}")


        else:
            print("\nError !! Try Again")

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break


   
    print("\nRedirecting to the Dashboard ...............\n")

    

def rectangle():

    while True:
        
        print("""
        
         ____  ____  _____ ____ 
        /  _ \/  __\/  __//  _ \
        | / \||  \/||  \  | / \|
        | |-|||    /|  /_ | |-||
        \_/ \|\_/\_\\____\\_/ \| ????
        
        
        """)


        length = int(input("Length = "))
        width = int(input("Width = "))
        area = length * width
        print(f"\nThe area is {area}")

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

    print("\nRedirecting to the Dashboard ...............\n")


def large():

    while True:
        
        print("""
         _____                               
        |     |_.---.-.----.-----.-----.----.
        |       |  _  |   _|  _  |  -__|   _|
        |_______|___._|__| |___  |_____|__|   ??
                           |_____|           
        """)

        No1 = float(input("Enter No 1: "))
        No2 = float(input("Enter No 2: "))
        No3 = float(input("Enter No 3: "))


        if (No1 >= No2) and (No1 >= No3):
            largest = No1
        elif (No2 >= No1) and (No2 >= No3):
            largest = No1
        else:
            largest = No3

        print(f"\nThe Largest number is {largest}")


        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break


    print("\nRedirecting to the Dashboard ...............\n")



def oddeve():


    while True:
        
        print("""
         ____  ____  ____        _____ _     _____
        /  _ \/  _ \/  _ \      /  __// \ |\/  __/
        | / \|| | \|| | \|_____ |  \  | | //|  \  
        | \_/|| |_/|| |_/|\____\|  /_ | \// |  /_ 
        \____/\____/\____/      \____\\__/  \____\ ??
                                                
        """)

        oddeve = int(input("Enter Number: "))

        if oddeve == 0:
            print(f"\n{oddeve} is an Universal Number")


        elif oddeve % 2 == 0:
            print(f"\n{oddeve} is an Even Number")


        else:
            print(f"\n{oddeve} is an Odd Number")

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

    print("\nRedirecting to the Dashboard ...............\n")




def sqltest():
    while True:

        print("""


         __    ____  __         ___   ___    __    __  __  ___  _____ 
        / _\  /___ \/ /        / __\ /___\/\ \ \/\ \ \/__\/ __\/__   \
        \ \  //  / / /  _____ / /   //  //  \/ /  \/ /_\ / /     / /\/
        _\ \/ \_/ / /__|_____/ /___/ \_// /\  / /\  //__/ /___  / /   
        \__/\___,_\____/     \____/\___/\_\ \/\_\ \/\__/\____/  \/  ----   
                                                                    


        ****************************** CAUTION ******************************

        Before using this program ! Plese try to install the required modules
        and try to start the sql service before using it ...................

        NOTE : IN LINUX, to start the sql service [ service mysql start ]

        Modules : mysql.connector

        Enter the correct details to ignore the error, else Program will be 
        throw an output ...... 

        
        """)
        
        import mysql.connector
        from mysql.connector import Error

        hostname = input("Enter Hostname [Ip/localhost]: ") 
        username = input("Enter Username: ") 
        passwordNo = input("Password: ")
        databaseName = input("Database Name: ")


        if hostname and username and passwordNo and databaseName:

            try:
             connection = mysql.connector.connect(host=hostname,database=databaseName,user=username,password=passwordNo)
             if connection.is_connected():
              db_Info = connection.get_server_info()
              print("connected: ", db_Info)
              cursor = connection.cursor()
              selected = input("Enter Select/Insert: ")
              
              if selected == 'insert':
                q = input('Query: ');
                cursor.execute(q)
                connection.commit()
                print("inserted")
              elif selected == 'select':
                q = input('Type your select sql query : ');
                cursor.execute(q)
                allrecords = cursor.fetchall()
                for x in allrecords:
                  print(x)
              else:
                 print('Terminating, Please Enter insert or select to proceed')
                 
            except Error as e:
                print ("Error while connecting to MySQL", e)
            finally:
                if(connection.is_connected()):
                    cursor.close()
                    connection.close()

        else:
            print("Please enter the correct Input !!")


        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")


def gradings():
    while True:

        print("""

         __  ___  _   __  ___  __ 
        / _|| o \/ \ |  \| __|/ _|
       ( |_n|   / o || o ) _| \_ \
        \__/|_|\\_n_||__/|___||__/ ooooo
                                

        """)

        a = int(input("Enter English: "))
        b = int(input("Enter Chemistry: "))
        c = int(input("Enter Mathematics: "))
        d = int(input("Enter Comp Sci: "))
        e = int(input("Enter Physics: "))


        avg = (a+b+c+d+e) / 5

        print("Average= ", avg)

        if (avg >= 90):
            print("Grade A")

        elif (avg >= 75 ) and (avg >=89):
            print("Grade B")

        elif (avg >= 60) and (avg >=74):
            print("Grade C")

        elif (avg >= 40) and (avg >=64):
            print("Grade E")


        else:
            print("Grade F")

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")


def voting():
    while True:

        print("""
                     __   __                   
        .--.--.-----|  |_|__.-----.-----.-----.
        |  |  |  _  |   _|  |     |  _  |__ --|
         \___/|_____|____|__|__|__|___  |_____| !!!
                                  |_____|      

        """)

        age = int(input("Enter Age: "))

        if age <= 18:
            print("You are in child hood")
        elif age <= 25:
            print("YOu are in the Golden Time")
        elif age <= 50:
            print("You are in age where you have responsibilty")

        else:
            print("Enjoy you're retirement")

        print("Check again if you want")

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")


def multiply_table():
    while True:

        print("""
         ____  __   ____  __    ____ 
        (_  _)/ _\ (  _ \(  )  (  __)
          )( /    \ ) _ (/ (_/\ ) _) 
         (__)\_/\_/(____/\____/(____) !!
        
        """)



        n = int(input("Enter Number: "))
        i = 1
        while i<=10:
            print("\n")
            print(n,"x",i,'=',n*i)
            i=i+1

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")



def factorial():
    while True:

        print("""
         _                                     _  
        | |                          o        | | 
        | |  __,   __ _|_  __   ,_       __,  | | 
        |/  /  |  /    |  /  \_/  |  |  /  |  |/  
        |__/\_/|_/\___/|_/\__/    |_/|_/\_/|_/|__/ !!
        |\                                        
        |/  
        
        """)

        import math
 
        def factorial(n):
            return(math.factorial(n))
         
         
        num = int(input("Enter Number: "))
        print("Factorial of", num, "is", factorial(num))


        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")



def simp_interest():
    while True:


        print("""
         _        .-.                       .-.      
        :_;      .' `.                     .' `.     
        .-.,-.,-.`. .'.--. .--.  .--.  .--.`. .'.--. 
        : :: ,. : : :' '_.': ..'' '_.'`._-.': :`._-.'
        :_;:_;:_; :_;`.__.':_;  `.__.'`.__.':_;`.__.'
        
        
        """)

        p = int(input("Enter Principle: "))
        t = int(input("Enter Time: "))
        r = int(input("Enter Rate of interest: "))



          
        si = (p * t * r)/100
          
        print('\nThe Simple Interest is', si)
        

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")


def comp_interest():
    while True:

        print("""
         _        .-.                       .-.      
        :_;      .' `.                     .' `.     
        .-.,-.,-.`. .'.--. .--.  .--.  .--.`. .'.--. 
        : :: ,. : : :' '_.': ..'' '_.'`._-.': :`._-.'
        :_;:_;:_; :_;`.__.':_;  `.__.'`.__.':_;`.__.'
        
        
        """)


        principle = int(input("Enter Principle: "))
        rate = int(input("Enter Rate: "))
        time = int(input("Enter Time: "))


        Amount = principle * (pow((1 + rate / 100), time))
        CI = Amount - principle
        print("Compound interest is", CI)

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")


def cel_fah():
    while True:


        

        celsius_1 = float(input("Temperature value in degree Celsius: " ))  
    
        Fahrenheit_1 = (celsius_1 * 1.8) + 32  
            
         
        print('The %.2f degree Celsius is equal to: %.2f Fahrenheit' %(celsius_1, Fahrenheit_1))  
  

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")


def fibo():
    while True:

        print("""
                   __         __     __  _             
         _______ _/ /_____ __/ /__ _/ /_(_)__  ___  ___
        / __/ _ `/ / __/ // / / _ `/ __/ / _ \/ _ \(_-<
        \__/\_,_/_/\__/\_,_/_/\_,_/\__/_/\___/_//_/___/
        

        """)
        
        n_terms = int(input ("How many terms the user wants to print: "))

        n_1 = 0  
        n_2 = 1  
        count = 0  
          
          
        if n_terms <= 0:  
            print ("Please enter a positive integer, the given number is not valid")  

        elif n_terms == 1:  
            print ("The Fibonacci sequence of the numbers up to", n_terms, ": ")  
            print(n_1)  


        else:  
            print ("The fibonacci sequence of the numbers is:")  
            while count < n_terms:  
                print(n_1)  
                nth = n_1 + n_2  
                n_1 = n_2  
                n_2 = nth  
                count += 1  


    
        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")



def leap_year():
    while True:

        print("""
        
         _                                     
        | |___ __ _ _ __ ___ _  _ ___ __ _ _ _ 
        | / -_) _` | '_ \___| || / -_) _` | '_|
        |_\___\__,_| .__/    \_, \___\__,_|_|   !!
                   |_|       |__/              
        
        """)
        
        def CheckLeap(Year):
            
          if((Year % 400 == 0) or  
             (Year % 100 != 0) and  
             (Year % 4 == 0)):   
            print("Given Year is a leap Year");  

          else:  
            print ("Given Year is not a leap Year")  
         
        Year = int(input("Enter Year: "))  

        CheckLeap(Year)

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")



def sumNum():
    while True:

        print("""

         ____  _     _     
        / ___\/ \ /\/ \__/|
        |    \| | ||| |\/||
        \___ || \_/|| |  ||
        \____/\____/\_/  \| + + +

        """)

        num = int(input("Enter a number: "))  
  
        if num < 0:  
           print("Enter a positive number")  
        else:  
           sum = 0   
           while(num > 0):  
               sum += num  
               num -= 1  
           print("The sum is",sum)  

        con = input("\nDo You want to try again? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

        print("\nRedirecting to the Dashboard ...............\n")



def man():
    while True:

        print("""                         

       '||    ||'     |     '|.   '|' '||'  '|'     |     '||'      
        |||  |||     |||     |'|   |   ||    |     |||     ||       
        |'|..'||    |  ||    | '|. |   ||    |    |  ||    ||       
        | '|' ||   .''''|.   |   |||   ||    |   .''''|.   ||       
       .|. | .||. .|.  .||. .|.   '|    '|..'   .|.  .||. .||.....| 
        


        Modules Needed: mysql.connector, sys, datetime, termcolor
        
        TIP: Use SQL Connection only in Linux which has installed all the requirements

        NOTE : 
        
        * Enter the correct commands to ignore the error's
        * Enter the correct Options [ 00, 01, ... , 99]
        * Install preffered Modules [ pip install <module_name> ]
        * Enter Y or N Correctly to Proceed Further

        """)


        con = input("\nPress D - [DASHBOARD] & Enter : ")

        if (con[0] == "d" or con[0] == "D"):
            break

        print("\nRedirecting to the Dashboard ...............\n")



        
def exy():
    sys.exit()


try:
    while True:


        print("""
        
        d8888b.  .d8b.  .d8888. db   db d8888b.  .d88b.   .d8b.  d8888b. d8888b. 
        88  `8D d8' `8b 88'  YP 88   88 88  `8D .8P  Y8. d8' `8b 88  `8D 88  `8D 
        88   88 88ooo88 `8bo.   88ooo88 88oooY' 88    88 88ooo88 88oobY' 88   88 
        88   88 88~~~88   `Y8b. 88~~~88 88~~~b. 88    88 88~~~88 88`8b   88   88 
        88  .8D 88   88 db   8D 88   88 88   8D `8b  d8' 88   88 88 `88. 88  .8D 
        Y8888D' YP   YP `8888Y' YP   YP Y8888P'  `Y88P'  YP   YP 88   YD Y8888D'  .......
                                                                                   
        """)


        print("""
        Choose an Option [1,2,3,4,.....,15]

        00. User Manual
        01. Arithmetic Operations
        02. Calculate the Area of rectangle
        03. Checking Larger of 3 Numbers
        04. Check Odd - Even
        05. Grading System
        06. Check voting Eligibility
        07. Multiplication
        08. Factorial
        09. Simple Interest
        10. Compound Interest
        11. Celcius to Fahrenheit
        12. Fibonacci Sequence
        13. Check Leap Year
        14. Sum of Numbers
        15. Connect to MySQL Database
        99. Exit

        """)


        option = int(input("Select an Option: "))

        if option == 1:
            arithmetic()

        elif option == 2:
            rectangle()

        elif option == 3:
            large()

        elif option == 4:
            oddeve()

        elif option == 5:
            gradings()

        elif option == 6:
            voting()

        elif option == 7:
            multiply_table()

        elif option == 8:
            factorial()

        elif option == 9:
            simp_interest()

        elif option == 10:
            comp_interest()

        elif option == 11:
            cel_fah()

        elif option == 12:
            fibo()

        elif option == 13:
            leap_year()

        elif option == 14:
            sumNum()

        elif option == 15:
            sqltest()

        elif option == 00:
            man()

        elif option == 99:
            exy()

        else:
            print("Invalid Option !! Try Again .......")

        con = input("\nContinue to Dashboard? [Y/N] : ")

        if not (con[0] == "Y" or con[0] == "y"):
            break

    

finally:
    print("\n............... Version : litter-treee 0.0.4 .............\n")