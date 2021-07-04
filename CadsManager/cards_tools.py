card_list = []

def show_menu():
    """shou menu"""
    print("*" * 50)
    print("welcome to use [cards manager system] V 1.0")
    print("")
    print("1. add card")
    print("2. show all card")
    print("3. search card")
    print("")
    print("0. exit system")
    print("*" * 50)

def new_card():
    """add new card"""
    print("-" * 50)
    print("add new card")

    name_str = input("please input name:")
    phone_str = input("please input phone:")
    qq_str = input("please input QQ:")
    email_str = input("please input email:")
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "email": email_str}
    card_list.append(card_dict)
    print(card_list)
    print("add %s's card ok" % name_str)

def show_all():
    """show card"""
    print("-" * 50)
    print("show all card")
    print("=" * 50)
    for name in ["name","phone","qq","email"]:
        print(name, end="\t\t")
    print("")
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" % (card_dict["name"],
                                            card_dict["phone"],
                                            card_dict["qq"],
                                            card_dict["email"]))
    print("=" * 50)
def search_card():
    """search card"""
    print("-" * 50)
    print("search card")
