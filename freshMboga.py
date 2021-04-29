fruits = ["pumkin","mango","orange","passion","watermelon","pineapple"]
item = input("Enter the item you want to purchase: ")
mango = 30
orange = 20
pumkin = 40
passion = 10
watermelon = 50
pineapple = 80



if item in fruits:

    
    quantity =int(input("Enter the quantity: ")) 
    if item== "mango" :
        cost = mango * quantity
        print(f"The total amount is {cost}")
    elif item == "orange":
        cost = orange * quantity
        print(f"The total amount is {cost}")
    elif item == "pineapple":
        cost = pineapple * quantity
        print(f"The total amount is {cost}")
    elif item == "watermelon":
        cost = watermelon * quantity
        print(f"The total amount is {cost}")
    elif item == "pumkin":
        cost = pumkin * quantity
        print(f"The total amount is {cost}")
    elif item == "passion":
        cost = passion * quantity
        print(f"The total amount is {cost}")
else:
    print("Item does not exist")

