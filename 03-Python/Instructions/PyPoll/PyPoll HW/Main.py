import os
import csv

election_data_csv = os.path.join('..', 'Resources', 'election_data.csv')

with open(election_data_csv, 'r') as csvfile:
    
    csv_reader = csv.reader(csvfile, delimiter=',')

    header = next(csv_reader)    
#sum number of votes
    num_votes = 0
    for row in open(election_data_csv):
        num_votes += 1
 #list candidates receiving votes       
    candidates = set()
    for row in csv_reader:
       candidates.add(row[2])

#print results
print("Election Results")
print(f"Total Votes: {num_votes}")
print(list(candidates))