import os
import csv

budget_csv = os.path.join('PyBank_budget_data.csv')

# create empty lists
months = []
profits_losses = []    
differences_list = []

# open and read csv
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    print(header)

    for row in csvreader:
        months.append(row[0]) 
        profits_losses.append(int(row[1])) 
        
    for x in range(len(months)-1):
        difference = profits_losses[x+1] - profits_losses[x]
        differences_list.append(difference)

    total_months = len(months) 
    total_profits_losses = sum(profits_losses) 
    average_change = round(sum(differences_list)/(total_months-1),2)
    max_increase = max(differences_list) 
    max_decrease = min(differences_list) 
    max_increase_date = months[differences_list.index(max_increase)]
    max_decrease_date = months[differences_list.index(max_decrease)]

    print(f'Financial Analysis')
    print(f'------------------------------------------------')
    print(f'Total Months: {total_months}') 
    print(f'Total: ${total_profits_losses}') 
    print(f'Average Change: ${average_change}') 
    print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})') 
    print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})')

# write textfile
with open("PyBank_Output.txt","w") as text_file:
    print(f'Financial Analysis',file=text_file)
    print(f'------------------------------------------------',file=text_file)
    print(f'Total Months: {total_months}',file=text_file) 
    print(f'Total: ${total_profits_losses}',file=text_file) 
    print(f'Average Change: ${average_change}',file=text_file) 
    print(f'Greatest Increase in Profits: {max_increase_date} (${max_increase})',file=text_file) 
    print(f'Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})',file=text_file)
