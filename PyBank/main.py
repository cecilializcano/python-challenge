import csv
#Read csv file
with open ('Resources/budget_data.csv') as file:
    data = csv.reader(file,delimiter=',')
    date=[]
    profit_losses=0
    profit_losses1=[]
    i=0
    #Read text file row by row
    for row in data:
        if i!=0:
            date.append(row[0])
            profit_losses=profit_losses+int(row[1])
            profit_losses1.append(int(row[1]))
        i=i+1

#Results from reading csv file
months=str(len(date))
total_profit=str(profit_losses)
avg_change=str(round((profit_losses1[0]-profit_losses1[i-2])/(len(date)-1),2))

#Find highest value (Greatest Increase in Profits) and lowest value (Greatest Decrease in Profits) and its index
num1=0
num2=0
delta1=0
delta2=0
max_num=0
min_num=0
month1=''
month2=''
z=0
for num in profit_losses1:
    if z!=0:
        delta1=num-num1
        delta2=num-num2
    if delta1>max_num:
        max_num=delta1
        max_month=date[z]
    if delta2<min_num:
        min_num=delta2
        min_month=date[z]
    num1=num
    num2=num
    z=z+1

#Print results in terminal
print('Total months: '+ months + '\n'+'\n')
print('Total: $'+ total_profit + '\n'+'\n')
print('Average Change: $'+ avg_change + '\n'+'\n')
print('Greatest Increase in Profits: '+ max_month +' '+'($'+str(max_num) +')'+'\n'+'\n')
print('Greatest Decrease in Profits: '+ min_month +' '+'($'+str(min_num) +')')

#Write results on text file
with open ('Analysis/Result.txt','w') as result:
    result.write('Total months: '+ months + '\n'+'\n')
    result.write('Total: $'+ total_profit + '\n'+'\n')
    result.write('Average Change: $'+ avg_change + '\n'+'\n')
    result.write('Greatest Increase in Profits: '+ max_month +' '+'($'+str(max_num) +')'+'\n'+'\n')
    result.write('Greatest Decrease in Profits: '+ min_month +' '+'($'+str(min_num) +')')
