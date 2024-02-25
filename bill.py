import sys

input_file = open('pricelist.csv','r')

all_items = input_file.readlines()

price_list = {}

for item in all_items:
    item_name = item.split(",")[0]
    item_price = item.split(",")[1]

    price_list[item_name] = item_price.strip()

print(price_list)

sys.exit()




print(price_list)

for item in price_list:
    print(item + " = $ " + str(price_list[item]))



grand_total_list = []
all_line_items = []

cart = True

while cart:
    item = input("Enter Item name : ")
    if item == "END":
        cart = False
    else:
        quantity = int(input("Enter Quantity : "))
        
        item_price = int(price_list[item]) * int(quantity)
        grand_total_list.append(item_price)
        
        line_item = ( item ," : " , price_list[item],  " X " ,  quantity , " = ", item_price )
        all_line_items.append(line_item)


print(all_line_items)
print(grand_total_list)



        
        
           



    
