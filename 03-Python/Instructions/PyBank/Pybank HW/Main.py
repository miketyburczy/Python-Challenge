import os
import csv

budget_csv = os.path.join('..', 'Resources', 'budget_data.csv')

with open(budget_csv, 'r') as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    header = next(csv_reader)    

#count number of months
    num_months = 0
    for row in open(budget_csv):
        num_months += 1

#sum profit/loss
    P_L_total = 0
    for row in csv.reader(csvfile):
        P_L_total += int(row[1])

    P_L_change = []
        
#print analysis   
print("Financial Analysis")
print(f"Total Months: {num_months}")
print(f"Total Profit/Loss: {P_L_total}")
print(f"Greatest Increase in Profits ")
print(f"Great Decrease in Profits: ")