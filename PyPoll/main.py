import os
import csv

poll_csv = os.path.join('PyPoll_election_data.csv')

# create empty lists
number_votes = []
candidates = []
all_candidates = []
counter = []
averagelist = []

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

    print(f'Election Results')
    print(f'-----------------------------------')
    print(f'Total Votes: {total_number_votes}')
    print(f'-----------------------------------')

    for x in range(len(candidates)):
        count = all_candidates.count(candidates[x])
        counter.append(count)
        average = str(round((count / total_number_votes)*100,3)) 
        averagelist.append(average)
        print(f'{candidates[x]}: {averagelist[x]}% ({counter[x]})') 
        #print(f'{candidates[x]}: {average}% ({count})') #good
        
    winner = max(counter) 

    print(f'-----------------------------------')
    print(f'Winner: {candidates[counter.index(winner)]}')
    print(f'-----------------------------------')

# write textfile
with open("PyPoll_Output.txt","w") as text_file:
    print(f'Election Results',file=text_file)
    print(f'-----------------------------------',file=text_file)
    print(f'Total Votes: {total_number_votes}',file=text_file)
    print(f'-----------------------------------',file=text_file)
    for x in range(len(candidates)):
        print(f'{candidates[x]}: {averagelist[x]}% ({counter[x]})',file=text_file)
    print(f'-----------------------------------',file=text_file)
    print(f'Winner: {candidates[counter.index(winner)]}',file=text_file)
    print(f'-----------------------------------',file=text_file)