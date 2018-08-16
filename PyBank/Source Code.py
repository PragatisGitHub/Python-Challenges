#Importing the required libraries
import csv
import os

#Filename and path
csvpath = os.path.join('raw_data', 'budget_data_2.csv')
txt_output = os.path.join('Output', 'PyBank_Summary2.txt')

#Decalaration of the variables
head = True
firstmonth = True
Totalmonths = 0
Totalrevenue = 0
prevrev = 0
currrev = 0
SumRevDiff = 0
RevChgD = {}

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
                SumRevDiff =SumRevDiff+(currrev - prevrev)
                RevChgD[row[0]] = currrev - prevrev
                prevrev = int(row[1])

#Printing the results
print(f'Financial Analysis')
print(f'---------------------------')
print(f'Total Months: {Totalmonths}')
print(f'Total Revenue: ${Totalrevenue}')
print(f'Average Revenue Change: ${round(SumRevDiff/(Totalmonths-1))}')
print(f'Greatest Increase in Revenue and the month: {max(RevChgD.items(), key=lambda k: k[1])[0]} (${max(RevChgD.items(), key=lambda k: k[1])[1]})')
print(f'Greatest Decrease in Revenue and the month: {min(RevChgD.items(), key=lambda k: k[1])[0]} (${min(RevChgD.items(), key=lambda k: k[1])[1]})')

#Writing to a text file
with open(txt_output,'w') as texthandler:
    texthandler.write(f'Financial Analysis\n')
    texthandler.write(f'---------------------------\n')
    texthandler.write(f'Total Months: {Totalmonths}\n')
    texthandler.write(f'Total Revenue: ${Totalrevenue}\n')
    texthandler.write(f'Average Revenue Change: ${round(SumRevDiff/(Totalmonths-1))}\n')
    texthandler.write(f'Greatest Increase in Revenue and the month: {max(RevChgD.items(), key=lambda k: k[1])[0]} (${max(RevChgD.items(), key=lambda k: k[1])[1]})\n')
    texthandler.write(f'Greatest Decrease in Revenue and the month: {min(RevChgD.items(), key=lambda k: k[1])[0]} (${min(RevChgD.items(), key=lambda k: k[1])[1]})')