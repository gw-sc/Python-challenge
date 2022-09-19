# Pypoll

# Import modules os, csv
import os
import csv

# Input path
csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')
# Output path
output_path = os.path.join('PyPoll', 'Analysis', 'PyPoll_Analysis.md')


def func():
    for row in candidate_summary:
        if row[0] == column[2]:
            row[1] = row[1] + 1
            return (0)
    candidate_summary.append([column[2], 1, 0])


def sort(i):
    return (i[1])


candidate_summary = []
candidates = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)  # skip header
    # print(csvreader)

# The total number of votes cast
    for column in csvreader:
        func()
    total_votes = sum(i[1] for i in candidate_summary)
print(total_votes)

# A complete list of candidates who received votes
for row in candidate_summary:
    print('{candidates}'.format(candidates=row[0]))

    # The percentage of votes each candidate won
for i in candidate_summary:
    i[2] = round((i[1] / total_votes) * 100, 3)
candidate_summary.sort(key=sort, reverse=True)
Winner = (candidate_summary[0])
print(Winner)
# The total number of votes each candidate won

# The winner of the election based on popular vote.

analysis = f'\
Election Results\n\
-------------------------\n\
Total Votes: {total_votes}\n\
-------------------------\n\
'': {}% ({})\n\
'': {}% ({})\n\
'': {}% ({})\n\
-------------------------\n\
Winner: ''\n\
------------------------- \n'

# In addition, your final script should both print the analysis to the terminal and export a text file with the results.
# print(analysis)

# with open(output_path, 'w') as f:
#     f.write((analysis))
# output_path.close()
