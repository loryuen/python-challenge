import os
import csv

poll_csv = os.path.join('PyPoll_election_data.csv')

# create empty lists
number_votes = []
candidates = []
all_candidates = []
counter = []

# open and read csv
with open(poll_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)

    # start loop
    for row in csvreader:
        # append number of votes to number of votes list to count votes
        number_votes.append(row[0])
        total_number_votes = len(number_votes) 

        # append unique candidates to candidates list
        if row[2] not in candidates:
            candidates.append(row[2])
        
        # put row[2] in its own list
        all_candidates.append(row[2])

    for x in range(len(candidates)):
        count = all_candidates.count(candidates[x])
        counter.append(count)
        average = round((count / total_number_votes)*100,3)
        
        print(f'{candidates[x]}: {average}% ({count})')
        
    winner = max(counter)

    print(f'Winner: {candidates[counter.index(winner)]}')
            
    # print results
    print(f'Election Results')
    print(f'-----------------------------------')
    print(f'Total Votes: {total_number_votes}')
    print(f'-----------------------------------')
    print(f'{candidates[x]}:') #khan
    print(f'{candidates[x]}:') #correy
    print(f'{candidates[x]}:') #li
    print(f'{candidates[x]}:') #o tooley
    print(f'-----------------------------------')
