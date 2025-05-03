# 1 box, with 
def search_the_key(main_box):
    stack = main_box # initialize the stack with the main box
    # the stack is a list of boxes to search in
    # in other words, I opened the main box

    i = 0
    total_steps = 0
        
    while stack: # while my stack of boxes is not empty
        total_steps += 1

        item_to_check = stack[i] # I take the current box in the stack
        is_a_box = isinstance(item_to_check, list)

        if is_a_box:
            print("New box...")
            for item in item_to_check:
                stack.append(item) # I add the new box in the boxes stack

            stack.pop(i) # I remove the current box from the stack
            i = 0 # I reset the index to as I have a new box to open
            
        elif item == "key":
            print("Finally! I found the key!")
            break
        else:
            print("I found something else: ", item)
            i += 1
    
    print("Total steps: ", total_steps)

# a box with many other boxes inside of if
search_the_key(
    [ #1
        [ #1.1
            [ # 1.1.1
                "food"
            ]
        ], 
        [], #1.2
        [ # 1.3
            [ # 1.3.1
                [ # 1.3.1.1
                    "toys",
                    "clothes"
                ], 
                [ # 1.3.1.2
                    "key"
                ]
            ], 
            [] # 1.3.2
        ]
    ]
)