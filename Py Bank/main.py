import os
import csv
csvpath = "/Users/asaddadabhoy/Desktop/Python Hw/Py Bank/Resources/budget_data.csv"

total_month = 0
month_change= []
revenue_change_list=[]
greatest_increase = ["", 0]
greatest_decrease = ["", 999999999999]
total_revenue = 0

with open (csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    first_row = next(csvreader)
    total_month = total_month + 1
    total_revenue + int (first_row[1])
    previous_revenue = int(first_row[1])

    for row in csvreader:
        total_month = total_month + 1
        total_revenue = total_revenue + int(first_row[1])
        revenue_change = int(row[1]) - previous_revenue
        previous_revenue = int(row[1])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_change = month_change + [row[0]]
        if revenue_change > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = revenue_change
        if revenue_change < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = revenue_change

revenue_average = sum(revenue_change_list)/len(revenue_change_list)

print("Financial Analysis")
print("----------------------------------------------")
print(f"Total Months: {total_month}")
print(f"Total: ${total_revenue}")
print(f"Average Change: ${revenue_average}")
print(f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")


output = (
   f"\nFinancial Analysis\n"
   f"----------------------------\n"
   f"Total Months: {total_month}\n"
   f"Total: ${total_revenue}\n"
   f"Average  Change: ${revenue_average}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
with open("output.txt", 'w') as txt_file:
    txt_file.write(output)




        



    









    


















 