# PyBank

# Import the os module
import os
# Import the module for reading CSV files
import csv

# set variables
months = []
profitloss = []

month_count = []
total_profitloss = 0
profitloss_change = []
sum_profitloss_change = 0
greatest_increase = 0
greatest_decrease = 0

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')
# csvpath = "./Resources/budget_data.csv"

# Improved reading using csv module
# open csvpath as csvfile in read mode
# csvfile = open(csvpath, "r")
with open(csvpath, 'r') as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=",")
    # print(csvreader)

    # skip the headers
    header = next(csvreader)

    for row in csvreader:
        # The total number of months included in the dataset
        if row[0] not in months:
            months.append(row[0])
            month_count = len(months)
    print(month_count)

# The net total amount of "Profit/Losses" over the entire period
    profitloss.append(float(row[1]))
    for p in profitloss:
        total_profitloss = total_profitloss + p
    print(total_profitloss)

# # The changes in "Profit/Losses" over the entire period, and then the average of those changes
# for i in range(len(profitloss)-1):
#     profitloss_change.append(profitloss[i + 1] - profitloss[i])
# print(profitloss_change)

# # for p in profloss_ch:
# sum_profitloss_change = sum_profitloss_change + p
# average_profitloss_change = sum_profitloss_change / len(profitloss_change)

# # The greatest increase in profits (date and amount) over the entire period
# for p in profitloss_change:
#     if p > greatest_increase:
#         greatest_increase = p
# print(p)

# # The greatest decrease in profits (date and amount) over the entire period
# for p in profitloss_change:
#     if p > greatest_decrease:
#         greatest_decrease = p
# print(p)

# # print to terminal
# # The 'analysis folder' contains the text file that has the results from the analysis.
# analysis = f'\
# Financial Analysis\n\
# ----------------------------\n\
# Total Months: {month_count} \n\
# Total Amount: ${profitloss} \n\
# Average Change: ${average_profitloss_change} \n\
# Greatest Increase in Profits: ${greatest_increase} \n\
# Greatest Decrease in Profits: ${greatest_decrease} \n'

# print(analysis)

# # In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# output_path = os.path.join(('Analysis', 'PyBank_Analysis.md'), 'w')
# with open(output_path, 'w') as f:
#     f.write((analysis))
# output_path.close()
