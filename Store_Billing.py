import sys

input_file = open('price.csv','r')

all_items = input_file.readlines()

price_list = {}

for item in all_items:
    print(item)
    item_name = item.split(",")[0]
    item_price = item.split(",")[1]
    price_list[item_name] = item_price.strip()

print(price_list)

for item in price_list:
    print(item + " = $" + str(price_list[item]))
grand_total_list = []
all_line_item = []

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()

# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("date and time -", dt_string)
#print(now)

dt = now.strftime("%Y%m%d-%H%M%S")
#print(dt)

cart = True
while cart:
    item = input("Enter item name: ")
    if item == "END":
        cart = False
    else:
        quantity = int(input("Enter quantity: "))
        item_price = int(price_list[item]) * int(quantity)
        grand_total_list.append(item_price)
        lineitem = (item + ":" + str(price_list[item]) + "x" + str(quantity) + "=" + str(item_price))
        all_line_item.append(lineitem)
f=open ('bill-'+dt+'.txt', 'w')
f.write("Welcome to Tamil Kadai!\n\n")
f.write(dt_string + "\n\n")

for item in all_line_item:
    print (item)
    f.write(item+"\n")

sum (grand_total_list)
print ("Total Cost = ", str(sum(grand_total_list)))
f.write ("Total Cost = " + str(sum(grand_total_list))+"\n\n")
f.write ("\n Thanks for shopping! Have a great day!")
f.close()
