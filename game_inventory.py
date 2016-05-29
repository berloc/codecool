

inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def Inventory(inv):
    print("Inventory:")
    item_total = 0
    for k, v in inv.items():
        print(str(v) + ' ' + k)


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


def print_table(inv):
    print("Inventory:")
    print('count'.center(10)+ ' '*5 +'item name')
    print('-'*24)
    item_total =0
    
    for k, v in inv.items():
        print(str(v).rjust(7) + ' '*8 + k.rjust(9))
        item_total += v
    print 'Total number of items:', item_total



Inventory(inv)
addToInventory(inv,dragonLoot)
print_table(inv)
