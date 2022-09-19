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
total_votes = 0

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
# for row in candidate_summary:
#     print('{candidates}'.format(candidates=row[0]))

# The percentage of votes each candidate won
    for i in candidate_summary:
        i[2] = round((i[1] / total_votes) * 100, 3)
    # print('{candidates}: {vote_percentage}%'.format(candidates=row[0], vote_percentage=row[2]))

# The total number of votes each candidate won
    # for row in candidate_summary:
    #     print('{candidate}: {candidate_votes}'.format(candidate=row[0], candidate_votes=row[1]))

# The winner of the election based on popular vote.
    candidate_summary.sort(key=sort, reverse=True)
    winner = (candidate_summary[0])
# print(winner)

print('Election Results')
print('-------------------------')
print('Total Votes: {total_votes}'.format(total_votes=total_votes))
print('-------------------------')
for row in candidate_summary:
    print('{candidate}: {percent}% ({votes})'.format(
        candidate=row[0],
        percent=row[2],
        votes=row[1]
    ))
print('-------------------------')
print('Winner: {winner}'.format(winner=winner[0]))
print('-------------------------')

# In addition, your final script should both print the analysis to the terminal and export a text file with the results. print(analysis) # with open(output_path, 'w') as f:
with open(output_path, 'w', newline='') as f:
    w = csv.writer(f)
    w.writerow(['Election Results'])
    w.writerow(['-------------------------'])
    w.writerow(['Total Votes: {total_votes}'.format(total_votes=total_votes)])
    w.writerow(['-------------------------'])
    for row in candidate_summary:
        w.writerow(['{candidate}: {percent}% ({votes})'.format(
            candidate=row[0],
            percent=row[2],
            votes=row[1]
        )])
    w.writerow(['-------------------------'])
    w.writerow(['Winner: {winner}'.format(winner=winner[0])])
    w.writerow(['-------------------------'])
# output_path.close()
