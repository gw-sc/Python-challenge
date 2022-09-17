# Pypoll

# Import modules os, csv
import os, csv

csvpath = os.path.join('Resources', 'budget_data.csv')


analysis = f'\
Election Results\n\
-------------------------\n\
Total Votes: {}\n\
-------------------------\n\
'': {}% ({})\n\
'': {}% ({})\n\
'': {}% ({})\n\
-------------------------\n\
Winner: ''\n\
------------------------- \n'
