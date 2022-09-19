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
# increase_month = 0
# decrease_month = 0


# csvpath = "./Resources/budget_data.csv"
# (os.getcwd(),.....)
csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv')

output_path = os.path.join('PyBank', 'Analysis', 'PyBank_Analysis.md')

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
        profitloss.append([row[0], float(row[1])])

        # The total number of months included in the dataset
        if row[0] not in months:
            months.append(row[0])
            month_count = len(months)
    # print(month_count)

# The net total amount of "Profit/Losses" over the entire period
    # for row in csvreader:
    #     profitloss.append(float(row[1]))
    for p in profitloss:
        total_profitloss = total_profitloss + p[1]
    print(total_profitloss)

# The changes in "Profit/Losses" over the entire period, and then the average of those changes
    for i in range(len(profitloss)-1):
        profitloss_change.append(
            [profitloss[i+1][0], profitloss[i + 1][1] - profitloss[i][1]])

    for p in profitloss_change:
        sum_profitloss_change = sum_profitloss_change + p[1]
    average_profitloss_change = sum_profitloss_change / len(profitloss_change)
    average_profitloss_change = round(average_profitloss_change, 2)
    # print(average_profitloss_change)

# The greatest increase in profits (date and amount) over the entire period
    p = 0
    increase_month = 0
    for p in profitloss_change:
        if p[1] > greatest_increase:
            greatest_increase = p[1]
            increase_month = p[0]

    print(greatest_increase)
    print(increase_month)
    # find the month adjacent
    # print(months)

    # The greatest decrease in profits (date and amount) over the entire period
    p = 0
    decrease_month = 0
    for p in profitloss_change:
        if p[1] < greatest_decrease:
            greatest_decrease = p[1]
            decrease_month = p[0]
    print(greatest_decrease)
    print(decrease_month)

# The 'analysis folder' contains the text file that has the results from the analysis.
analysis = f"\
Financial Analysis\n\
    ----------------------------\n\
    Total Months: {month_count} \n\
    Total Amount: ${total_profitloss} \n\
    Average Change: ${average_profitloss_change} \n\
    Greatest Increase in Profits: {increase_month} ${greatest_increase} \n\
    Greatest Decrease in Profits: {decrease_month} ${greatest_decrease} \n"

print(analysis)

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

with open(output_path, 'w') as f:
    f.write((analysis))
output_path.close()
