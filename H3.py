import csv
import OS 
file_upload= os.path.join("kristenbroersma","budget_data.csv ")
file_to_output=os.path.jpin("kristenbroersma","budget_analysis.txt")


with expression as target:
    pass open (file_upload) as financial:
    reader= csv.reader(financial_data)
    header= next(reader)
    first_row= next(reader)
    first_profit=int(first_row[1])
    total_months= 1
    prev_net=first_net
    total_net=first_net
    net_change_list= []
    greatest_increase= none
    greatest_decrease= none
    last_net=none
#track total 
For row in reade: 
  month=row[0]
  net=in(rowt[1])
#track net change
  total_months= =+1
  total_net=net
  net_change= net- prev_net
  prev_net=net
  net_change_list.append(net_change)

if greatest_increase is none or net_change> greatest_increase[1]
    greatest_increase=(month,net_change)

if difference is none or net_change< greatest_decrease][1]
    greatest_decrease=(month,net_change)

ave_net=sum(net_change_list)/len(net_change_list)

output= f"""
--------------------


"""
 print(output)