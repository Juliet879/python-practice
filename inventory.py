# stock = {
#     'books' : 3,
#     'pens' : 14,
#     'tissue' : 67,
#     'manila' : 148
# }
# def display(inventory):
#     item_total = 0
#     for k,v in inventory.items():
#         print(k + " " + str(v))
#         item_total += v
#     print("The total number of your inventories is:" + str(item_total))
# display(stock)

# # def addToInventory(inv,addedItems):
# #     item_total = 0
# #     for k,v in inv.items():
# #         print(k + " "+ str(v))
# #         item_total += v
    
# # inv = {'gold coin':42,'rope':1}
# # dragonLoot = ['gold coin','dagger','gold coin','ruby']
# # inv = addToInventory(inv,dragonLoot)

# while True:
#     age = input("Enter you age:")
#     if age.isdecimal():
#         break
#     print("Please enter a number for your age: ")
# while True:
#     password = input("Select a new password (letters and numbers only): ")
#     if password.isalnum:
#         break
#     print("Password can only have letters and numbers.")

def printPicnic(itemsDict,leftWidth,rightWidth):
    print('PICNIC ITEMS'.center(leftWidth + rightWidth, '-'))
    for k,v in itemsDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))
picnicItems = {'sandeitches':4,'apple':12,'cups':5,'coolies':8000}
printPicnic(picnicItems,12,5)
printPicnic(picnicItems,20,6)
