import Attribute
from Attribute import *



"""
    Description: This class represents individual examples to be classified read from the sample file. 
                 Each example has a number for identification, the number of possible attributes it can have, and the attribute assignment values.

                 The attribute assignment values are represented by integers as the index of that value for the attribute.
                 Ex. If an attribute 'color' has possible values [red, blue, green], an example with color=blue would have the value 1 recorded for that attribute.
"""
class Example:

    #A specific number for the example as its order being read from the DataFile
    exampleNum = 0

    #The number of distinct attributes in the example
    numAttributes = 0

    #List of integers that correspond with the example's attribute assignment values
    attributeValues = []

    def __init__(self, exampleNum, exampleAssignments, schemeAttributes):
        self.exampleNum = exampleNum
        self.attributeValues = []

        #Parse all of the attribute assignment values provided for this example
        self.parseAttributeValues(exampleAssignments, schemeAttributes)

        #Initialize the number of attributes in the example
        if (self.attributeValues != None):
            self.numAttributes = len(self.attributeValues)

        else:
            self.numAttributes = 0



    #Getter functions
    def getAttributeValues(self):
        return self.attributeValues

    def getFunctionValue(self):
        return self.attributeValues[self.numAttributes - 1]

    def getSpecificValue(self, index):
        return self.attributeValues[index]



    """ 
        Description: This function parses all of the attribute value assignments for this example from an input string.
                     The list of registed attributes from the SchemeFile are used to validate the attribute values.
     
        Parameter: exampleAssignment                 The string containing the list of attribute assignments
        Parameter: schemeAttributes                  The ArrayList of attributes registered from the SchemeFile
        No return value
    """
    def parseAttributeValues(self, exampleAssignments, schemeAttributes):
        
        #Array of the passed attribute value assignments for this example
        attributeList = exampleAssignments.split()

        #If the number of non-function attribute values doesn't match the number provided in the scheme file, this example is invalid
        if (len(attributeList) != len(schemeAttributes)):
            print("ERROR: The number of attributes in example " + str(self.exampleNum) + " doesn't match the amount required.")
            print("Expected: " + str(len(schemeAttributes)) + "Received: " + str(len(attributeList)))
            self.attributeValues = None
            return

        #Iterate through every passed attribute value assignment
        for i in range(len(attributeList)):

            #Get the corresponding index of the assignment from the order of the values entered when reading the SchemeFile
            #Ex. An attribute with possible values [T, F] would map T:0 and F:1
            index = schemeAttributes[i].getIndexOfValue(attributeList[i])

            #If the index returned is -1, the attribute assignment value passed was invalid
            #Ex. An attribute with possible values [X, Y], and an example that has an assignment of Z
            if (index == -1):
                print("ERROR: One of the attribute values in example: " + str(self.exampleNum) + " is invalid.")
                self.attributeValues = None
                return

            #Else, store the associated index in this class's list of indices
            else:
                self.attributeValues.append(index)