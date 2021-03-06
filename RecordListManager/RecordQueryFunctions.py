"""
    Name: listRecordsByArtist
    Description: This function lists all of the records for a given artist.

    Parameter: records          The list of records
    Return: No return value
"""
def listRecordsByArtist(records, artist):

    #The number of records for the given artist
    numRecords = 0

    print("The list of records by " + artist+ " are listed below.")

    #Iterate through the list of records to search for the ones matching the artist
    for rec in records:

        #Print each matching record
        if (rec.artist == artist):
            print("Title: " + rec.title)
            print("Quantity: " + str(rec.quantity))
            print("")
            numRecords = numRecords + 1

    #If no records were found for the given artist, inform the user
    if (numRecords == 0):
        print("There are no records by " + artist + " in the list of records.")



"""
    Name: listRecordsByYear
    Description: This function lists any records for a given release year.

    Parameter: records          The list of records
    Parameter: year             The year to search for
    No return value
"""
def listRecordsByYear(records, year):

    #Counter of the number of records that matched the query
    recordCount = 0

    print("The list of records released in the year " + str(year) + " are below:")

    #Iterate through the list of records
    for rec in records:

        #If the record's release year matches the year we're looking for, print the record info
        if (rec.releaseYear == str(year)):
            print("Artist: " + rec.artist)
            print("Title: " + rec.title)
            print("")
            recordCount = recordCount + 1

    #If no records were released for the given year, inform the user
    if (recordCount == 0):
        print("There were no records in the list for the given year.")

    

"""
    Name: listRecordsWithDuplicates
    Description: This function lists any records in the given list that have duplicates.

    Parameter: records          The list of records
    No return value
"""
def listRecordsWithDuplicates(records):

    #Counter of the number of records that matched the query
    recordCount = 0

    print("The list of records with duplicate copies are listed below:")

    #Iterate through the list of records
    for rec in records:

        #If a record with more than one copy is found, print its information
        if (rec.quantity > 1):
            print("Artist: " + rec.artist)
            print("Title: " + rec.title)
            print("Quantity: " + str(rec.quantity))
            print("")
            recordCount = recordCount + 1

    #If no records had duplicates, inform the user
    if (recordCount == 0):
        print("There were no records in the list with duplicate copies.")



"""
    Name: printTotalRecordCount
    Description: This function returns the number of records in the given list of records.

    Parameter: records          The list of records
    No return value
"""
def printTotalRecordCount(records):
    
    #The number of records in the list total
    recordCount = 0

    #Increment the record count with the quantity of every record
    for rec in records:
        recordCount = recordCount + rec.quantity

    print("There are " + str(recordCount) + " records total in the list.")



"""
    Name: printUniqueRecordCount
    Description: This function returns the number of unique records in the given list of records.

    Parameter: records          The list of records
    No return value
"""
def printUniqueRecordCount(records):
    print("There are " + str(len(records)) + " unique records in the list.")