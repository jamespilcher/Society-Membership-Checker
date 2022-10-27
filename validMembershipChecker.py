
import csv
import time

with open('society.csv', 'r') as f:
    listOfMembers = [row[1].title() for row in csv.reader(f)][1:]

with open('event.csv', 'r') as f:
    listOfMembersTicketHolders = []
    for row in csv.reader(f):
        if 'Non' not in row[12]:
            listOfMembersTicketHolders.append( (row[0] + " " + row[1]).title() )

listOfLiars = []

for MembersTicketHolder in listOfMembersTicketHolders[1:]:
    if MembersTicketHolder not in listOfMembers:
        listOfLiars.append(MembersTicketHolder)


listOfActualLiars = []

for liar in listOfLiars:
    liarFirstName, liarSecondName = liar.split(" ")

    matchingFirstNames = []
    matchingSecondNames = []
    for member in listOfMembers:
        (memberFirstName, memberSecondName) = member.split(" ",1)
        if liarSecondName == memberSecondName:
            matchingSecondNames.append(member)
        if liarFirstName == memberFirstName:
            matchingFirstNames.append(member)
    
    print()
    print("-----------------------------")
    print()
    print("Current Suspected Liar: ", liar)
    if matchingSecondNames:
        print("Members with matching second names: ")

        for secondNameMatch in matchingSecondNames:
            print("- ", secondNameMatch)

        nameFound = input("Was the correct member found (y/n)? ")
        if nameFound == "y":
            continue

    else: 
        print("No matching second names...")
    time.sleep(.65)
    if matchingFirstNames:
        print("Members with matching first names: ")
        for firstNameMatch in matchingFirstNames:
            print("- ", firstNameMatch)

        nameFound = input("Was the correct member found (y/n)? ")
        if nameFound == "y":
            continue
    else:
        print("No matching first names...")
    print()
    print("LIAR FOUND")
    listOfActualLiars.append(liar)
print("--------------------")
print()
print("LIARS: ")
for liar in listOfActualLiars:
    print("- ", liar)
print()
input('Press ENTER to exit')