## Calculator for Ship Funds

#Global Costs Variables
#*ship_Passage = .5
#messages_Dock_Master = 2
#messages_Addressed = 5
#docking_cost = 10

#Wages for each member
wages = {
    'Sailors' : 0.2,
    'Skilled Sailors' : 0.5,
    'Marines' : 1,
    'Officers' : 2,
    'Wizards' : 2,
}

crew = {
    'Sailors' : 2,
    'Skilled Sailors' : 2,
    'Marines' : 2,
    'Officers' : 2,
    'Wizards' : 2,
}
#Total Money on ship
shipFundTotal = 0
daysOnTrip = 0

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
    costOfSailor = days * wages['Sailors']
    costOfSkilledSailor = days * wages['Skilled Sailors']
    costOfMarine = days * wages['Marines']
    costOfOfficer= days * wages['Officers']
    costOfWizard = days * wages['Wizards']

    print(f"Each Officer gets {costOfOfficer} gold and each Wizard gets {costOfWizard} gold")

    costOfSailors = costOfSailor * crew['Sailors']
    costOfSkillerSailors = costOfSkilledSailor * crew['Skilled Sailors']
    costOfMarines = costOfMarine * crew["Marine"]
    costOfOfficers = costOfOfficer * crew["Officers"]
    costOfWizards = costOfWizard * crew["Wizards"]

    totalCrewWages = costOfSailors + costOfSkillerSailors + costOfMarines + costOfOfficers + costOfWizards
    print(f"The crew cost a total of {totalCrewWages} in wages for this voyage")
    return totalCrewWages
totalCrewWages = calculateCrewWages(1, wages, crew)