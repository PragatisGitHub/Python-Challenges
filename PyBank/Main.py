#Importing the required libraries
import csv
import os

#Filename and path
csvpath = os.path.join('raw_data', 'budget_data_1.csv')
csvpath_output = os.path.join('Output', 'PyBank_Summary1.csv')

#Decalaration of the variables
head = True
firstmonth = True
Totalmonths = 0
Totalrevenue = 0
prevrev = 0
currrev = 0
SumRevDiff = 0
RevChg = {}

#Main Logic to read the data and do the required calculations
with open(csvpath, "r") as PyBank:
    csvread = csv.reader(PyBank)
    for row in csvread:
        if (head == True): 
            head = False
        else:   
            if firstmonth == True:
                firstmonth = False
                Totalmonths +=1
                Totalrevenue +=int(row[1])
                prevrev = int(row[1])
            else: 
                Totalmonths +=1
                Totalrevenue +=int(row[1])
                currrev = int(row[1])
                SumRevDiff = currrev - prevrev
                RevChg[row[0]] = int(SumRevDiff)
                prevrev = int(row[1])

#Printing the results
print(f'Financial Analysis')
print(f'---------------------------')
print(f'Total Months: {Totalmonths}')
print(f'Total Revenue: ${Totalrevenue}')
print(f'Average Revenue Change: {SumRevDiff/Totalmonths-1}')
print(f'Greatest Increase in Revenue: {max(RevChg.items(), key=lambda k: k[1])[0]} (${max(RevChg.items(), key=lambda k: k[1])[1]})')
print(f'Greatest Decrease in Revenue: {min(RevChg.items(), key=lambda k: k[1])[0]} (${min(RevChg.items(), key=lambda k: k[1])[1]})')

#Writing to a csv file
with open(csvpath_output,'w',newline='') as csvhandlerW:
      csvwriter = csv.writer(csvhandlerW,delimiter="\t")
      csvwriter.writerow(f'Financial Analysis')
      csvwriter.writerow(f'---------------------------')
      csvwriter.writerow(f'Total Months: {Totalmonths}')
      csvwriter.writerow(f'Total Revenue: ${Totalrevenue}')
      csvwriter.writerow(f'Average Revenue Change: {SumRevDiff/Totalmonths-1}')
      csvwriter.writerow(f'Greatest Increase in Revenue: {max(RevChg.items(), key=lambda k: k[1])[0]} (${max(RevChg.items(), key=lambda k: k[1])[1]})')
      csvwriter.writerow(f'Greatest Decrease in Revenue: {min(RevChg.items(), key=lambda k: k[1])[0]} (${min(RevChg.items(), key=lambda k: k[1])[1]})')
