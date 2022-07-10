#importing python file
import List
import Borrow
import Return
#creating a function named librarymanagementsystem
def librarymanagementsystem():
    print("      Welcome to the ABC library      ")
    print("--------------------------------------")
    #starting while loop
    while(True):
        print("Enter 1 To Display the available books")
        print("Enter 2 To Borrow books from the library")
        print("Enter 3 To Return the book to the library")
        print("Enter 4 To close the program")
        print("--------------------------------------")
        #exception handeling
        try:
            #taking input from the user
            n = int(input("Enter a number for the respective task: "))
            print("--------------------------------------")
            #starting a if loop with condition
            if( n == 1):
                print("      Available books     ")
                print("--------------------------") 
                file = open("stock.txt","r")
                lines = file.read()
                print(lines)
                print("--------------------------------------")
            
            elif( n == 2):
                List.list_()
                Borrow.borrow()
                
            elif( n == 3):
                List.list_()
                Return.return_()
                
            elif( n == 4):
                print("Thank you for using our library")
                break
            else:
                print("Enter as suggested ")
                print("----------------------------")
                
        except ValueError:
            print("Please input the valid value")
#calling the function
librarymanagementsystem()
                  
