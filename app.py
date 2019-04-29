print("                         WELCOME TO JUW SUPERMART                ")
print("                      BEST ONLINE SHOPPING WEBSITE               ")

# For Collecting User Information;
user_info = {

}
shopping_cart = {

}

details = ["name", "address", "mobile_number"]


def collect_user_info():
    for i in details:
        user_info[i] = input("Your " + i + ": ")


collect_user_info()


print("Please Select Category In Which You Want To Buy \n")


categories = {
    1: {
        "category_name": "WOMEN'S COLLECTION",
        "product": {
            'Kurti': {
                "price": 1000,
                "stock": 100
            },
            'Lawnsuit': {
                "price": 2000,
                "stock": 200
            },
            'Dupatta': {
                "price": 500,
                "stock": 150
            },
            'Trouser': {
                "price": 500,
                "stock": 500
            },
            'Shirts': {
                "price": 800,
                "stock": 200
            },
        }

    },
    2: {
        "category_name": "MEN'S COLLECTION",
        "product": {
            'Kurta': {
                'price': 1000,
                "stock": 60
            },
            'Cottonsuit': {
                "price": 2000,
                "stock": 140
            },
            'T-shirts': {
                "price": 500,
                "stock": 120
            },
            'Trouser': {
                "price": 500,
                "stock": 70
            },
            'Shirts': {
                "price": 800,
                "stock": 90
            },
        }

    },
    3: {
        "category_name": "HEALTH & BEAUTY",
        "product": {
            'Sun Block': {
                "price": 500,
                "stock": 60
            },
            'Menicure And Pedicure': {
                "price": 2000,
                "stock": 600
            },
            'Loreal': {
                "price": 500,
                "stock": 60
            },
            'Slim Fcae Massarger': {
                "price": 1500,
                "stock": 50
            },
            'Fair And Lovely': {
                "price": 200,
                "stock": 500
            },
        }
    },
    4: {
        "category_name": "HOME & LIFESTYLE",
        "product": {
            'Corner Tabal': {
                "price": 1500,
                "stock": 500
            },
            'Dinner Set': {
                "price": 2000,
                "stock": 500
            },
            'Fancy Lights': {
                "price": 1500,
                "stock": 100
            },
            '3D Wallpapers': {
                "price": 1500,
                "stock": 190
            },
            'Drawing Rooms Set': {
                "price": 2500,
                "stock": 30
            },
        }

    },
    5: {
        "category_name": "WATCHES & ACCESSORIES",
        "product": {
            'Rolex': {
                "price": 5000,
                "stock": 420
            },
            'Designer Braclets': {
                "price": 2000,
                "stock": 40
            },
            'Earing Set': {
                "price": 500,
                "stock": 200
            },
            'Rings': {
                "price": 1500,
                "stock": 300
            },
            'Zara ': {
                "price": 200,
                "stock": 600
            },
        }

    }
}

current_category = {

}
cart = {

}


def select_categories():
    print("CATEGORIES \n")
    print("Press The Specified Number To Select The Category In Which You Want To Buy \n")
    for category_number in categories:
        print("Press " + str(category_number)+" For : " +
              categories[category_number]["category_name"])

    current_category_number = input()
    if current_category_number.isdigit():
        current_category_number = int(current_category_number)

    while (current_category_number in categories) is False:
        print("Please Input a Valid Option \n")
        current_category_number = input()
        if str(current_category_number).isdigit():
            current_category_number = int(current_category_number)

    current_category = categories[current_category_number]

    print(current_category["category_name"])

    select_sub_category(current_category)


def select_sub_category(category):
    print(" SUB CATEGORIES \n")
    print("Type The Name Of Sub Category To Buy \n")
    products = category["product"]
    for product in products:
        print(product + ": \n")
        print("price: "+str(products[product]["price"])+"            " +
              "available stock: "+str(products[product]["stock"])+"\n")

    sub_category = input()

    while (sub_category in products) is False:
        print("Please Input a Valid Option \n")
        sub_category = input()

    print("How Many "+sub_category+" In " +
          category["category_name"]+" You Want To Buy")

    quantity = input()
    if quantity.isdigit():
        quantity = int(quantity)

    while str(quantity).isdigit() is False:
        print("Please Input a Valid Option \n")
        quantity = input()
    quantity = int(quantity)
    while (quantity <= products[sub_category]["stock"]) is False:
        print("Out Of Stock")
        quantity = input()
        while quantity.isdigit() is False:
            print("Please Input a Valid Option \n")
            quantity = input()
        quantity = int(quantity)

    add_to_cart(category, sub_category, quantity)


def add_to_cart(current_category, sub_category, quantity):
    if (current_category["category_name"] in cart) is False:
        cart[current_category["category_name"]] = {

        }

    cart[current_category["category_name"]][sub_category] = {
        "quantity": quantity,
        "price": current_category["product"][sub_category]["price"]*quantity
    }
    print("Press B to buy more in this category \n")
    print("Press C to Change the category \n")
    print("Press P to Pay the bill \n")

    wtd = input()
   #  while (wtd != "B") or (wtd != "C") or (wtd != "P"):
   #     print("Please Give A Valid Option \n")
   #     wtd = input()
    print("\n\n\n\n\n\n")
    if wtd == "B":
        select_sub_category(current_category)
    elif wtd == "C":
        select_categories()
    elif wtd == "P":
        pay_bill()


def pay_bill():
    total_bill = 0
    for category in cart:
        print(category+": \n")
        for sub_category in cart[category]:
            print(sub_category+": ")
            print("      Quantity "+str(cart[category][sub_category]["quantity"]
                                        )+" Total "+str(cart[category][sub_category]["price"]))
            total_bill += cart[category][sub_category]["price"]
        print("\n")

    print("\n \n Your Total Bill Is " + str(total_bill))
    print("Pay Charges")
    charges = input()
    if charges.isdigit():
        charges = int()

    while str(charges).isdigit() is False:
        print("Please Input a Valid Option \n")
        charges = input()
    charges = int(charges)
    while charges < total_bill:
        print("Given Price Is Low As Compare To Total Bill \n")
        charges = input()   
        charges = int(charges)
    print("Balance: "+str(charges-total_bill))
    print("\n \n Thanks "+user_info["name"] + " For Coming Our Mart \n \n ")


select_categories()
