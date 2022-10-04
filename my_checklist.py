
checklist = list()
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
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

# def list_all_items():
#     index = 0
#     for list_item in checklist:
#         # print(str(index) + list_item)
#         # print("{} {}".format(index, list_item))
#         print("{} {}".format(colors[index] + list_item)
#         index += 1

# def mark_completed(index):
    #add code here that marks an item as completed
def select(function_code):
    #user selection code here
    if function_code == "C":
        input_item = user_input("Name an item of clothing:")
        create(input_item)

    elif function_code == "R":
        item_index = user_input("What color?")
        # should index number ask for color choice?
        read(item_index)

    elif function_code == "P":
        list_all_items()

    elif function_code == "Q":
        return False

    
    else:
        print("Unknown Option")
        return True

def list_all_items():
    for i in range(len(colors)):
        color = colors[i]
        print(color + checklist[i])

def user_input(prompt):
    #get user input here
    user_input = input(prompt)
    return user_input

    

running = True
while running: 
    function_code = user_input()

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

test()
#Run tests
    

