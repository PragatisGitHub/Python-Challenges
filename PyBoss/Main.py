#import dependencies
import os
import csv

#Filename & filepath
filepath = os.path.join("raw_data","employee_data1.csv")
csvpath_output = os.path.join("Output","PyBoss_Outputdata1.csv")

#US state dictionary
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

#Variable declaration
head = True
First_Name = []
Last_Name = []
DOB = []
SSN = []
State = []
Reformatted_Line = []

#Main logic to read a file and do the required calculations
with open(filepath) as csvhandlerR:
    InfileData = csv.reader(csvhandlerR)
    for line in InfileData:
        if head == True:
            Reformatted_Line.append(f'Emp_Id,First_Name,Last_Name,DOB,SSN,State')
            head = False
        else:    
            #Split the name into first name & last name
            Split_Name = line[1].split(" ")
            First_Name = Split_Name[0]
            Last_Name = Split_Name[1]
            
            #Reformat date from YYYY-MM-DD to MM/DD/YYYY
            Split_DOB = line[2].split("-")
            Format_DOB = f'{Split_DOB[1]}/{Split_DOB[2]}/{Split_DOB[0]}'
                       
            #Reformat SSN into ***-**-NNNN
            Split_SSN = line[3].split("-")
            Format_SSN = f'{Split_SSN[0].replace(Split_SSN[0],"***")}-{Split_SSN[1].replace(Split_SSN[1],"**")}-{Split_SSN[2]}'
           
            #Reformat state name to its abbreviation
            State_Abbreviation = us_state_abbrev[line[4]]    
                     
            Reformatted_Line.append(f'{line[0]},{First_Name},{Last_Name},{Format_DOB},{Format_SSN},{State_Abbreviation}')

#Writing to a csv file            
with open(csvpath_output,'w',newline='') as csvhandlerW:
    OutfileData = csv.writer(csvhandlerW,delimiter="\t")
    for row in Reformatted_Line:  
        OutfileData.writerow(row)                