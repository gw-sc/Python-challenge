# Import the os module
from distutils import text_file
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
incr = []
decr = []

for row in csvreader:

# The total number of months included in the dataset
    months.append(row[0])
    month_count = len(months)

# The net total amount of "Profit/Losses" over the entire period
    net_profloss.append(float(row[1]))

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
    # profloss_ch = 

# The greatest increase in profits (date and amount) over the entire period
    # incr =

# The greatest decrease in profits (date and amount) over the entire period
    # decr =


# The 'analysis folder' contains your text file that has the results from your analysis.
analysis = f'\
Financial Analysis\n\
----------------------------\n\
Total Months: {month_count} \n\
Total Amount: ${} \n\
Average Change: ${} \n\
Greatest Increase in Profits: ${} \n\
Greatest Decrease in Profits: ${} \n'

print(analysis)

output_path = os.path.join(('Analysis', 'PyBank_Analysis.md'), w)
with open (output_path, w) as f:
    f.write((analysis))
output_path.close()