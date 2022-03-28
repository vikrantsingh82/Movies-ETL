import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = "../Resources/WWE-Data-2016.csv"


# Define the function and have it accept the 'wrestlerData' as its sole parameter
def wrestling(wrestlerData):
    return wrestlerData[0]

# Find the total number of matches wrestled
def wrestling_total_matches(wrestlerData):
    return int(wrestlerData[1]) + int(wrestlerData[2]) + int(wrestlerData[3])
# Find the percentage of matches won
def percentage_win(wrestlerData):
    return round(float((int(wrestlerData[1])/wrestling_total_matches(wrestlerData))*100 ),2)
# Find the percentage of matches lost
def percentage_loses(wrestlerData):
    return round(float((int(wrestlerData[2])/wrestling_total_matches(wrestlerData))*100 ),2)
# Find the percentage of matches drawn
def percentage_draw(wrestlerData):
    return round(float((int(wrestlerData[3])/wrestling_total_matches(wrestlerData))*100 ),2)

# Print out the wrestler's name and their percentage stats
def print_percentages(wrestlerData):
    print (f"Name: { wrestling(wrestlerData)}")
    print (f"Total # of matches: { wrestling_total_matches(wrestlerData)}")
    print (f"% of Wins:  { percentage_win(wrestlerData)}")
    print (f"% of Loses:  { percentage_loses(wrestlerData)}")
    print (f"% of Draws:  { percentage_draw(wrestlerData)}")


with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")
    # Loop through the data
    for row in csvreader:
        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
        # else:
        #     print(name_to_check +" not found" + row[0])

