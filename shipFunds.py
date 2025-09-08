## Calculator for Ship Funds 
#Imports
import tkinter as tk

#TK information
master = tk.Tk()
#Title of Page
master.title('Ship Funds Calculator')

#Creating enterbox for Shipfunds
#label = Label(master, text='Ship Funds Total').grid(row=0)
#Wages for each member
wages = {
    'Sailors' : 0.2,
    'Skilled Sailors' : 0.5,
    'Marines' : 1,
    'Officers' : 2,
    'Wizards' : 2,
}

#Number of staffing for each crew type
crew = {
    'Sailors' : 2,
    'Skilled Sailors' : 2,
    'Marines' : 2,
    'Officers' : 2,
    'Wizards' : 2,
}
#Total Money on ship
shipFundTotal = 0
daysOnTrip = 1

#Adding money to the ship total
def addMoneyToShip(money):
    shipFundTotal += money
    return shipFundTotal

#Adding days to journey, for wages
def addDaysOnTrip(days):
    daysOnTrip += days
    return daysOnTrip



#Calculating trip wages
def calculateCrewWages(days, wages, crew):
    #Calc the cost of a single crew member of each type
    costOfSailor = days * wages['Sailors']
    costOfSkilledSailor = days * wages['Skilled Sailors']
    costOfMarine = days * wages['Marines']
    costOfOfficer= days * wages['Officers']
    costOfWizard = days * wages['Wizards']

    #Each player is a officer or wizard so mention amount of gold to players
    print(f"Each Officer gets {costOfOfficer} gold and each Wizard gets {costOfWizard} gold")

    #Calc the total cost of each crew member type for the total number of crew
    costOfSailors = costOfSailor * crew['Sailors']
    costOfSkillerSailors = costOfSkilledSailor * crew['Skilled Sailors']
    costOfMarines = costOfMarine * crew["Marines"]
    costOfOfficers = costOfOfficer * crew["Officers"]
    costOfWizards = costOfWizard * crew["Wizards"]

    #Sum the total of cost & print/return total
    totalCrewWages = costOfSailors + costOfSkillerSailors + costOfMarines + costOfOfficers + costOfWizards
    print(f"The crew cost a total of {totalCrewWages} gold in wages for this voyage")
    return totalCrewWages

#Collecting value of Crew Wages
totalCrewWages = calculateCrewWages(daysOnTrip, wages, crew)

#Subtracting Crew wages from Funds and print out remain Funds
shipFundTotal -= totalCrewWages
print(f"There is {shipFundTotal} gold in Ship Funds remaining after wages")