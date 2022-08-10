import datetime
import csv
import os
import re
"""This function is print the report
	userinput :kitchen,Water Leakage, etc..  
	rpttype =  ['Location, Type , Risk']"""


def values_get_data(userinput, rpttype):
    # Read the out file to print the report.
    files = open("output.csv")
    csvreaders = csv.reader(files)
    header = next(csvreaders)
    rows = []
    print("\t**************" + rpttype + " : " + userinput + " Report **************")
    print("\t--------------------------------------------------------------")
    print("\t Location    | \t Type     | \t Risk | \t Demographic")
    print("\t--------------------------------------------------------------")
    for row in csvreaders:
        if row:
            if rpttype == 'Location':
                if row[0] == userinput:
                    print("\t {} | \t {} | \t {} | \t {}".format(*row))
            if rpttype == 'Type':
                if row[1] == userinput:
                    print("\t {} | \t {} | \t {} | \t {}".format(*row))
            if rpttype == 'Risk':
                if row[2] == userinput:
                    print("\t {} | \t {} | \t {} | \t {}".format(*row))
    files.close()

def file_input(writer):
    file = open("data.csv")
    csvreader = csv.reader(file)  # read a data from data file
    header = next(csvreader)  # Read headers
    if len(header) != 4:  # Check input csv file is correct columns or not
        print("CSV file is not correct please add only four fields")

    for row in csvreader:
        # check all the columns are in correct format or not.
        if row[0].upper() not in ['LIVING ROOM', 'DINING ROOM', 'KITCHEN', 'BEDROOM', 'BATHROOM']:
            print("Location data is not entered properly.")
            break
        if row[1].upper() not in ['WATER LEAKAGE', 'FIRE HAZARD', 'ELECTRICITY OUTAGE', 'PHYSICAL']:
            print("Type data is not entered properly.")
            break

        if row[2].upper() not in ['HIGH', 'MEDIUM', 'LOW', 'NONE']:
            print("Risk data is not entered properly.")
            break

        # Check the date format.
        date_format = "%d/%m/%Y"
        pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')
        match = pattern.match(row[3])
        if not match:
            try:
                res = bool(datetime.datetime.strptime(row[3], date_format))
            except ValueError:
                print("Date is not in correct format")
                break
        writer.writerow(row)  # Write a data into a output file
    print("Data are successfully added.")

def manual_input(writer):
    print("\n Press 5 to go back main menu.")
    print("['Living Room', 'Dining Room','kitchen','bedroom', 'bathroom']")
    location = input("Please Enter Location:")  # user inputs for Location
    # check the location is correct or not.
    if location == '5':
        main()
    while location.upper() not in ['LIVING ROOM', 'DINING ROOM', 'KITCHEN', 'BEDROOM', 'BATHROOM']:
        print("\t Location is not entered properly\n \t Please enter from below:")
        print("\t ['Living Room', 'Dining Room','kitchen','bedroom', 'bathroom']")
        location = input("\nPlease Enter Location:")
        if location == '5':
            main()
    print("\n Press 5 to go back main menu.")
    print(" ['Water Leakage', 'Fire Hazard', 'Electricity Outage','Physical']")
    hivtype = input("Please Enter Type:")
    # check the type is correct or not.
    if hivtype == '5':
        main()
    while hivtype.upper() not in ['WATER LEAKAGE', 'FIRE HAZARD', 'ELECTRICITY OUTAGE', 'PHYSICAL']:
        print("\t Type is not entered properly\n \t Please enter from below:")
        print("\t ['Water Leakage', 'Fire Hazard', 'Electricity Outage','Physical']")
        hivtype = input("\nPlease Enter Type:")
        if hivtype == '5':
            main()
    print("\n Press 5 to go back main menu.")
    print(" ['High', 'Medium', 'Low', 'None']")
    risk = input("Please Enter Risk:")
    # check the risk is correct or not.
    if risk == '5':
        main()
    while risk.upper() not in ['HIGH', 'MEDIUM', 'LOW', 'NONE']:
        print("\t Risk is not entered properly\n \t Please enter from below:")
        print("\t ['High', 'Medium', 'Low', 'None']")
        risk = input("\nPlease Enter Risk:")
        if risk == '5':
            main()
    print("\n Press 5 to go back main menu.")
    demogramphic = input("Please Enter date(DD/MM/YYYY) or time(HH:MM):")
    if demogramphic == '5':
        main()
    date_format = "%d/%m/%Y"
    res = True
    # check weather date is correct or not.
    pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')
    match = pattern.match(demogramphic)
    if not match:
        try:
            res = bool(datetime.datetime.strptime(demogramphic, date_format))
        except ValueError:
            res = False
    # if date is not in correct format it will ask again for the entry
    while not res:
        demogramphic = input("\nPlease Enter date(DD/MM/YYYY) or time(HH:MM:SS):")
        if demogramphic == '5':
            main()
        date_format = "%d/%m/%Y"
        res = True
        try:
            res = bool(datetime.datetime.strptime(demogramphic, date_format))
        except ValueError:
            res = False
    row = [location, hivtype, risk, demogramphic]
    # if all data are correct then it will store in the output file
    writer.writerow(row)

def display():
    print("Display the output")
    file_path = "output.csv"
    # check weather file is empty or not
    if os.stat(file_path).st_size == 0:
        print('File is empty')
    else:
        # read the file and print the output of it.
        file = open("output.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        if len(header) != 4:
            print("CSV file is not correct please add only four fields")
        rows = []
        print("\t--------------------------------------------------------------")
        print("\t Location    | \t Type     | \t Risk | \t Demographic")
        print("\t--------------------------------------------------------------")
        for row in csvreader:
            if row:
                print("\t {} | \t {} | \t {} | \t {}".format(*row))
        file.close()

def reports():
    reporttype = input("Please enter a number based on you want to print report\
    			 \n \t 1. Location \
    			  \n \t 2. Type \
    			  \n \t 3. Risk \
    			  \n \t 5. Go back to main menu.:")  # Take user input for what reports they wants.
    if reporttype == '1':
        print("\n \t ['Living Room', 'Dining Room','kitchen','bedroom', 'bathroom']")
        locationtype = input("\tEnter the location.:")
        # check location wise report  entered details are correct ot not.
        if locationtype == '5':
            main()
        if locationtype.upper() in ['LIVING ROOM', 'DINING ROOM', 'KITCHEN', 'BEDROOM', 'BATHROOM']:
            values_get_data(locationtype, 'Location')
        # else:
        #     break;
    elif reporttype == '2':
        # check Type wise report  entered details are correct ot not.
        print("\n \t ['Water Leakage', 'Fire Hazard', 'Electricity Outage','Physical']")
        types = input("\tEnter the type.:")
        if types == '5':
            main()
        if types.upper() in ['WATER LEAKAGE', 'FIRE HAZARD', 'ELECTRICITY OUTAGE', 'PHYSICAL']:
            values_get_data(types, 'Type')
        # else:
        #     break;
    elif reporttype == '3':
        print("\n \t ['High', 'Medium', 'Low', 'None']")
        risks = input("\tEnter the Risk.:")
        if risks == '5':
            main()
        # check risk wise report  entered details are correct ot not.
        if risks.upper() in ['HIGH', 'MEDIUM', 'LOW', 'NONE']:
            values_get_data(risks, 'Risk')  # Call the function to print the report data.
        # else:
        #     break;
    else:
        print("Report option is wrong.")


#method is used to delete a record from the output.
def delete_record():
    if os.stat('output.csv').st_size == 0:
        print('File is empty. You cannnot delete anything.')
        main()
    print("\n Press 5 to go back main menu.")
    print("['Living Room', 'Dining Room','kitchen','bedroom', 'bathroom']")
    location = input("Please Enter Location:")  # user inputs for Location
    # check the location is correct or not.
    if location == '5':
        main()
    while location.upper() not in ['LIVING ROOM', 'DINING ROOM', 'KITCHEN', 'BEDROOM', 'BATHROOM']:
        print("\t Location is not entered properly\n \t Please enter from below:")
        print("\t ['Living Room', 'Dining Room','kitchen','bedroom', 'bathroom']")
        location = input("\nPlease Enter Location:")
        if location == '5':
            main()
    print("\n Press 5 to go back main menu.")
    print(" ['Water Leakage', 'Fire Hazard', 'Electricity Outage','Physical']")
    hivtype = input("Please Enter Type:")
    # check the type is correct or not.
    if hivtype == '5':
        main()
    while hivtype.upper() not in ['WATER LEAKAGE', 'FIRE HAZARD', 'ELECTRICITY OUTAGE', 'PHYSICAL']:
        print("\t Type is not entered properly\n \t Please enter from below:")
        print("\t ['Water Leakage', 'Fire Hazard', 'Electricity Outage','Physical']")
        hivtype = input("\nPlease Enter Type:")
        if hivtype == '5':
            main()
    print("\n Press 5 to go back main menu.")
    print(" ['High', 'Medium', 'Low', 'None']")
    risk = input("Please Enter Risk:")
    # check the risk is correct or not.
    if risk == '5':
        main()
    while risk.upper() not in ['HIGH', 'MEDIUM', 'LOW', 'NONE']:
        print("\t Risk is not entered properly\n \t Please enter from below:")
        print("\t ['High', 'Medium', 'Low', 'None']")
        risk = input("\nPlease Enter Risk:")
        if risk == '5':
            main()
    print("\n Press 5 to go back main menu.")
    demogramphic = input("Please Enter date(DD/MM/YYYY) or time(HH:MM):")
    if demogramphic == '5':
        main()
    date_format = "%d/%m/%Y"
    res = True
    # check weather date is correct or not.
    pattern = re.compile(r'^([0-1]?[0-9]|2[0-3]):[0-5][0-9]$')
    match = pattern.match(demogramphic)
    if not match:
        try:
            res = bool(datetime.datetime.strptime(demogramphic, date_format))
        except ValueError:
            res = False
    # if date is not in correct format it will ask again for the entry
    while not res:
        demogramphic = input("\nPlease Enter date(DD/MM/YYYY) or time(HH:MM:SS):")
        if demogramphic == '5':
            main()
        date_format = "%d/%m/%Y"
        res = True
        try:
            res = bool(datetime.datetime.strptime(demogramphic, date_format))
        except ValueError:
            res = False
    delete_row = [location, hivtype, risk, demogramphic]
    file = open("output.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    if len(header) != 4:
        print("CSV file is not correct please add only four fields")
    rows = []
    print("\t--------------------------------------------------------------")
    print("\t Location    | \t Type     | \t Risk | \t Demographic")
    print("\t--------------------------------------------------------------")
    count = 0
    not_deleted = []
    for row in csvreader:
        if row:
            if row == delete_row:
                count +=1
                print("\t {} | \t {} | \t {} | \t {}".format(*row))
            else:
                not_deleted.append(row)

    if count > 0:
        print ("\n \t Total %s records are deleted." % count)
    else:
        print ("\n \t No records found for | {} | {} | {} | {}".format(*delete_row))

    #delete a records and create a new file for the updated records.

    f = open('output.csv', 'w')  # create a csv file object to store the data.
    writer = csv.writer(f)
    if not headerwrite:
        if os.stat('output.csv').st_size == 0:
            header_row = ['Location', 'Type', 'Risk', 'Date']  # Add the header of the output file
            writer.writerow(header_row)
            writer.writerows(not_deleted)
# This program will execute untill user will get userinpu=quit
filePath = 'output.csv'
if os.path.exists(filePath):
    os.remove(filePath)
headerwrite=False

def main():
    while True:
        f = open('output.csv', 'a')  # create a csv file object to store the data.
        writer = csv.writer(f)
        if not headerwrite:
            if os.stat('output.csv').st_size == 0:
                header_row = ['Location', 'Type', 'Risk', 'Date']  # Add the header of the output file
                writer.writerow(header_row)
        print ("\n\n-----Main Menu-----")
        print("1. Enter data from file.")
        print("2. Manual Entry")
        print("3. Check the output")
        print("4. Reports")
        print("5. quit")
        print("6. Delete a record\n")

        userinput = input("\tEnter user input:")  # User inputs for the process.
        print("User input is: " + userinput)

        # Read the data from csv file and add into the output file for.
        if userinput == '1':
            file_input(writer)

        # take user manual inputs
        elif userinput == '2':
            manual_input(writer)

        elif userinput == '3':
            display()

        # It's print report based on Location, Type, Risk
        elif userinput == '4':
            reports()
        # Quit program
        elif userinput == '6':
            f.close()
            print ("FILE CLOSE")
            delete_record()

        else:
            exit(0)

    f.close()
main()