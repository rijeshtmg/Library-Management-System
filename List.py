# creating a function named list_
def list_():
    # decleraing global variable
    global bookname
    global authorname
    global quantity
    global cost
    global lines
    # making list of the respective varibale
    bookname = []
    authorname = []
    quantity = []
    cost = []

    # opening the stock file and reading the data
    with open("stock.txt","r") as file: 
        lines = file.readlines()
        lines=[x.strip('\n') for x in lines] # striping the \n from the lines

        # starting nested for loop
        for i in range(len(lines)):
            index=0
            for j in lines[i].split(','):
                if(index == 0):
                    bookname.append(j) # appending data of the bookname in its respective list
                elif(index == 1):
                    authorname.append(j) # appending data of the authorname in its respective list
                elif(index == 2):
                    quantity.append(j) # appending data of the quantity in its respective list
                elif(index == 3):
                    cost.append(j.strip("$")) #  striping the $ from the cost and appending data of the cost in its respective list
                index = index + 1

