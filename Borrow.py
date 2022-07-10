# importing python file
import List
import Date_Time
# creating a function named borrow
def borrow():
    bBorrowed = False
    
    # starting while loop
    while(True):
        firstname = input("Enter the first name of the borrower: ")
        # checking whether the given input is in alphabet or not
        if firstname.isalpha():
            break
        print("----------------------------------")
        print("Please input valid character from A-Z")

    # starting while loop  
    while(True):
        lastname = input("Enter the last name of the borrower: ")
        # checking whether the given input is in alphabet or not
        if lastname.isalpha():
            break
        print("----------------------------------")
        print("Please input the alphabet from A-Z")
        
    # creating a object name bFile for borrower txt file
    bFile = "Borrower-" + firstname + ".txt"
    
    # opening bFile as object(file) to write the data
    with open(bFile,"w+") as file:
        file.write("        \t\t   ABC Library         " + "\n")
        file.write("           Borrowed By: "+ firstname + " " + lastname + "\n")
        file.write("     Date: " + Date_Time.getDate() + "\t Time: " + Date_Time.getTime() + "\n")
        file.write("S.N. \t\t Book Name \t         AuthorName \n")
    # starting while loop
    while bBorrowed == False:
        print("----------------------------------")
        print("Please select the book which you want to borrow: ")
        print("----------------------------------")
        # listing the available book
        for i in range(len(List.bookname)):
            print("Enter",i ,"to borrow book", List.bookname[i])
        print("----------------------------------")
        # exception handeling  
        try:
            a = int(input("Enter the respective number of the book you want to borrow: ")) # taking input from the user
            # starting if else loop and checking if the input value is positive or negative
            if (a < 0):
                print("----------------------------------")
                print("Please enter the positive value.")
                print("----------------------------------")
            else:
                # exception handeling
                try:
                    # starting if loop  
                    if(int(List.quantity[a])>0): # checking if the book is available or not
                        print("----------------------------------")
                        print("The book is available")
                        # Appending data in the bFile
                        with open(bFile,"a") as file:
                            file.write("1. \t\t"+ List.bookname[a] + "\t\t   " + List.authorname[a] + "\n")

                        List.quantity[a] = int(List.quantity[a])-1 # decreasing the quantity of the book
                        # updating the stock file after borrowing book
                        with open("stock.txt","w") as file:
                            for i in range(len(List.lines)):
                                file.write(List.bookname[i] + "," + List.authorname[i] + "," + str(List.quantity[i]) + "," + "$" + List.cost[i]+ "\n")

                        # for borrowing multiple book
                        loop = True
                        c = 1
                        # starting while loop
                        while loop == True:
                            print("-------------------------------------------")
                            borrow_more = input("Do you want to borrow more books? Enter Y for Yes and N for No: ")
                            # starting if else loop and checking the enter value
                            if(borrow_more.upper() == "Y"):
                                c=c+1
                                print("Please select an option below:")
                                # listing the available book
                                for i in range(len(List.bookname)):
                                    print("Enter", i, "to borrow book", List.bookname[i])
                                print("----------------------------------")
                            
                                b = int(input("Enter the respective number of the book you want to borrow: ")) # taking input from the user
                                if( a == b): # comparing the index of the book
                                    print("You cannot borrow same book twice")
                                elif(int(List.quantity[b])>0): # checking if the book is available or not
                                    print("----------------------------------")
                                    print("The book is available")
                                    # opening file named bFile to append data of the book
                                    with open(bFile,"a") as file:
                                        file.write(str(c) +". \t\t"+ List.bookname[b]+"\t\t  "+ List.authorname[b] + "\n")

                                    List.quantity[b] = int(List.quantity[b])-1 # decreasing the quantity of the book
                                    # updating the stock file after borrowing book
                                    with open("Stock.txt","w") as file:
                                        for i in range(len(List.lines)):
                                            file.write(List.bookname[i] + "," + List.authorname[i] + "," + str(List.quantity[i]) + "," + "$" + List.cost[i] + "\n")
                                            bBorrowed = False
                                else:
                                    loop = False
                                    break
                            elif(borrow_more.upper() == "N"):
                                print("----------------------------------")
                                print("Thank you for using our library to borrow books")
                                print("----------------------------------")
                                loop = False
                                bBorrowed = True
                            else:
                                # Error message
                                print("Enter the number as instructed")
                            
                    else:
                        # Error message
                        print("This Book is not available")
                        borrow()
                        bBorrowed = False
                  
                except IndexError:
                    # Error message
                    print("----------------------------------")
                    print("Please choose book according to their number.")
    
        except ValueError:
            # Error message
            print("----------------------------------")
            print("Enter number as instructed.")
                                              
            
                                                
                                          
                    
        
    
    
