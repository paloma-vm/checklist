
checklist = list()
# colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
#CREATE
def create(item):
    checklist.append(item)


#READ
def read(index):
   # item = checklist[index]
   # return item
    return checklist[index]

#UPDATE
def update(index, item):
    checklist[index] = item

#DESTROY
def destroy(index):
    checklist.pop(index)

def list_all_items():
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        index += 1

def mark_completed(index, item):
    #add code here that marks an item as completed
    read(index)
    ask_completed = user_input("Mark this item complete? y/n")
    if ask_completed == "y":
        update(index, index +" √")
        print(item)
    elif ask_completed == "n":
        "item not marked complete"
    else:
        print("please enter y for yes or n for no")

def user_input(prompt):
    #get user input here
    user_input = input(prompt)
    return user_input

def select(function_code):
    #user selection code here
    function_code = function_code.upper()

    if function_code == "A":
        # "C"
        input_item = user_input("Name an item of clothing to add:")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("Index number of item you wish to remove?:")
        read(item_index)
        destroy()

    elif function_code == "C":
        item_index = user_input("Index number of item you wish to complete?:")
        mark_completed(index, item)

    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False
 
    else:
        print("Unknown Option")
    return True

# def list_all_items():
#     for i in range(len(colors)):
#         color = colors[i]
#         print(color + checklist[i])





def test():
    #Add testing code here

    user_value = user_input("Please enter a value:")
    print(user_value)

    create("purple socks")
    create("red cape")
    create("green tights")
    create("gold mask")
    

    print(read(0))
    print(read(1))

    update(0, "purple socks")
    destroy(1)

    print(read(0))
    # print(read(1))
    # ^the line above was throwing the error
    select("C")
    list_all_items()
    select("R")
    list_all_items()

# test()
#Run tests

running = True
while running: 
    selection = user_input("Press A to add to list, R to remove from list, C to add checkmark, P to display list, and Q to quit")
    running = select(selection)

