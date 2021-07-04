import cards_tools

while True:
    #TODO show menu
    cards_tools.show_menu()
    action_str = input("please choice do:")
    print("you choice is [%s]" % action_str)
    #1,2,3
    if action_str in ["1","2","3"]:
        #pass
        if action_str == "1":
            #pass
            cards_tools.new_card()
        elif action_str == "2":
            #pass
            cards_tools.show_all()
        elif action_str == "3":
            #pass
            cards_tools.search_card()
    elif action_str == "0":
        #pass
        print("welcome to use again:[cads manager]")
        break
    else:
        print("you input is error,please choice again")
