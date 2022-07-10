# creating the function named getDate
def getDate():
    #importing datetime
    import datetime
    now=datetime.datetime.now
    return str(now().date()) # extracting the date from the imported function

# creating the function named getTime
def getTime():
    #importing datetime
    import datetime
    now=datetime.datetime.now
    return str(now().time()) # extracting the time from the imported function
