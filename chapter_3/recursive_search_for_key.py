def search_the_key(caixa):
    for item in caixa:
        is_a_box = isinstance(item, list)

        if is_a_box:
            search_the_key(item)
        elif item == "key":
            print("Finally! I found the key!")
        else:
            print("I found something else: ", item)

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