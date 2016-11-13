import sys
import csv
from collections import Counter

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}        #Step 1: display_inventory() definition

def display_inventory(inv):                                                     #display_inventory function with
        print('Invetory:')                                                      #import_invertory
        item_total = 0
        c = Counter(inv)
        for i, j in inv.items():
            item_total = item_total +j
        for k, v in c.most_common():
            print('\t',     str(v) + '\t' +k)

def add_to_inventory(inventory, added_items):                                   #Step 2: add_to_inventory definition
    for k in added_items:
        pass
        if k in inventory.keys():
            inventory[k]+=1
        else:
            inventory[k]=1

def print_table(inventory):                                                     #Step 3: print_table definition
    print('\nInventory:\n\tcount\titem_name')
    print('------------------------')
    item_total = 0
    c = Counter(inv)
    for i, j in inv.items():                                                    #filling invertory
        item_total = item_total +j
    for k, v in c.most_common():                                                #printing in
        print('\t',     str(v) + '\t' +k)
    print('------------------------',)
    print('Total number of items: '+ str(item_total)+'\n')

def import_inventory(filename="import_inventory.csv"):                          #Step 4: import_inventory() definition
    file_list = []
    with open(filename, "r") as file:
        for line in file:                                                       #data import
            row = line.split(",")
            first = row[0]
            second = row[1]
            minus_line = len(second)-1
            second = second[0:minus_line]
            file_list.extend([[first, second]])
    for listed in range(1, len(file_list)):
        if file_list[listed][0] in inv:
            inv[file_list[listed][0]] += int(file_list[listed][1])
        else:
            inv[file_list[listed][0]] = int(file_list[listed][1])

def export_inventory(filename="export_inventory.csv"):                          #Step 5: export_inventory definition
    global inv
    f = open('export_inventory.csv', 'w')                                       #data exporting
    f.write("count,item_name\n")
    item_export = 0
    c = Counter(inv)
    for i, j in inv.items():
        item_export = item_export +j
    for k, v in c.most_common():
        f.write(str(v) + "," + k + "\n")
    f.close()

dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
import_inventory("import_inventory.csv")                                        #import extension file in import_inventory() function
import_inventory("extension.csv")
display_inventory(inv)
add_to_inventory(inv,dragon_loot)
print_table(inv)
export_inventory(inv)
