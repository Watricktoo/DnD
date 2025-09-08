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

def wagesForCrew(daysOnTrip, wages):
    return 0

test = "test"
print(test)
#Calculating trip wages

    
    