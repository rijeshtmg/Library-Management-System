# importing the python file
import List
import Date_Time

# creating a function named return_
def return_():
    firstname = input("Enter the name of the borrower: ") # taking input for the name of the borrower
    # creating a object of same named as borrower txt file
    bFile = "Borrower-" + firstname + ".txt"

    # exception handeling
    try:
        # opening the file named bFile and reading data in it
        with open(bFile,"r") as file:
            lines = file.readlines()
            lines = [bFile.strip("$") for bFile in lines] # stripping the $ from the lines
        # opening the file named bFile and reading data in it
        with open(bFile,"r") as file:
            info = file.read()
            print(info) # printing the data of the file
    except:
        print("The name of the borrower is incorrect. Please enter the correct name.")
        return_()
    # creating a object named rFile for return txt file
    rFile = "Return-" + firstname + ".txt"
    # opening the file named rFile and write data in it
    with open(rFile,"w") as file:
        file.write("        \t\t   ABC Library         " + "\n")
        file.write("           Borrowed By: "+ firstname + "\n")
        file.write("     Date: " + Date_Time.getDate() + "\t Time: " + Date_Time.getTime() + "\n")
        file.write("S.N. \t\t Book Name \t         Cost \n")
    # declearing the total cost
    total_cost = 0.0
    c = 0
    for i in range(len(List.lines)):
        if List.bookname[i] in info: # checking if the book name is in the borrower txt file or not
           c = c + 1
           # opening file named rFile and appending data in it
           with open(rFile,"a") as file:
                file.write(str(c)+"\t\t"+List.bookname[i]+"\t\t$"+List.cost[i]+"\n")
                List.quantity[i]=int(List.quantity[i])+1 # increasing the quantity of the book
           total_cost = total_cost + float(List.cost[i]) # adding the total cost of the book

    print("\t\t\t\t\t\t\t" + "Total cost: " + "$" + str(total_cost))
    print("----------------------------------")
    print("Does the date of returning is more than 10 days?")
    print("----------------------------------")
    delay = input("Enter y for Yes and n for No: ") # taking input from the user for delay
    # starting a if loop
    if ( delay.upper() == "Y"):
        print("----------------------------------")
        time = int(input("How many days it is delayed: ")) # taking input from the user for how many day it was delayed
        fine = 1 * time
        # opening file named rFile and append fine in the fie
        with open(rFile,"a")as file:
            file.write("\t\t\t\t\t"+"Fine: $"+ str(fine)+"\n")
        total_cost = total_cost + fine
    

    print("----------------------------------")
    print("Final Total: "+ "$"+str(total_cost)) # printing the total cost
    print("----------------------------------")

    # opening the file named rFIle and append the total cost
    with open(rFile,"a")as file:
        file.write("\t\t\t\t\t"+"Total: $"+ str(total_cost))
    print("Thank you for returning our book to the library")

    # updating the stock txt file after returning book
    with open("Stock.txt","w") as file:
            for i in range(len(List.lines)):
                file.write(List.bookname[i]+","+List.authorname[i]+","+str(List.quantity[i])+","+"$"+List.cost[i]+"\n")
            
    
        
    
        
