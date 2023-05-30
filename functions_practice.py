def hello():
    print("Hello Laura")
hello()

def pack(sunscreen,clothes,shoes):
    return[sunscreen,clothes,shoes]
print(pack("sunscreen", "clothes", "shoes"))

def eat_lunch(my_lunch):
    if len(my_lunch) == 0:
        print("My Lunchbox Is Empty!")
    else:
        for i in range(len(my_lunch)):
            if i == 0:
                print(f"First I eat {my_lunch[0]}")
            else:
                print(f"Next I eat {my_lunch[i]}")
eat_lunch([])
eat_lunch(["pizza", "soda", "cheesecake"])