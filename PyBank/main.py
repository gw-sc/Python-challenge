# PyBank

# Import the os module
import os
# Import the module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
# csvpath = "./Resources/budget_data.csv"

    # Improved reading using csv module
    # open csvpath as csvfile in read mode
#csvfile = open(csvpath, "r")
with open(csvpath, newline = '') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter = ",")
    # print(csvreader)
    
    # skip the headers
    header = next(csvreader)

    # set variables
months = []
profloss = []

month_count = []
net_profloss = []
profloss_ch = []
sum_profloss_ch = 0
incr = 0
decr = 0

for row in csvreader:

# The total number of months included in the dataset
    if row [0] not in months:
        months.append(row[0])
    month_count = len(months)

# The net total amount of "Profit/Losses" over the entire period
    profloss.append(float(row[1]))
    for p in profloss:
        net_profloss = net_profloss + p

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
for i in range(len(profloss)-1):
    profloss_ch.append(profloss[i + 1] - profloss[i])
print(profloss_ch)

for p in profloss_ch:
    sum_profloss_ch = sum_profloss_ch + p
average_profloss_ch = sum_profloss_ch / len(profloss_ch)

# The greatest increase in profits (date and amount) over the entire period
for p in profloss_ch:
    if p > incr:
        incr = p
print(p)

# The greatest decrease in profits (date and amount) over the entire period
for p in profloss_ch:
    if p > decr:
        decr = p
print(p)

# print to terminal
# The 'analysis folder' contains your text file that has the results from your analysis.
analysis = f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {month_count} \n\
Total Amount: ${profloss} \n\
Average Change: ${average_profloss_ch} \n\
Greatest Increase in Profits: ${incr} \n\
Greatest Decrease in Profits: ${decr} \n'

print(analysis)

output_path = os.path.join(('Analysis', 'PyBank_Analysis.md'), w)
with open (output_path, w) as f:
    f.write((analysis))
output_path.close()