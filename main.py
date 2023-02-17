menu = {"1": 2.00, "2": 1.00, "3": 3.00}
cart = []
total = 0

print("Welcome to the GC Fruit Market!")
name = input("What is your name? ")

fruit_selection = input(f"Welcome {name}. Which Fruit would you like to buy? "
f"1. Apple $2 "
f"2. Grape $1 "
f"3. Orange $3 " )
if fruit_selection == "1":
    print("You bought 1 apple at $2")
    cart.append(fruit_selection)
if fruit_selection == "2":
    print("You bought 1 grape at $1")
    cart.append(fruit_selection)
if fruit_selection == "3":
    print("You bought 1 orange at $3")
    cart.append(fruit_selection)
while True:
    more = input("Would you like to buy another piece of fruit? y/n ")
    if more == "y":
        fruit_selection = input(f"Welcome {name}. Which Fruit would you like to buy? "
                                f"1. Apple $2 "
                                f"2. Grape $1 "
                                f"3. Orange $3 ")
        if fruit_selection == "1":
            print("You bought 1 apple at $2")
            cart.append(fruit_selection)
        if fruit_selection == "2":
            print("You bought 1 grape at $1")
            cart.append(fruit_selection)
        if fruit_selection == "3":
            print("You bought 1 orange at $3")
            cart.append(fruit_selection)
    if more == "n":
        break

for fruit_selection in cart:
    total += menu.get(fruit_selection)

print()
print(f"Receipt for {name}")
print("1 apple(s) at $2 a piece")
print("1 grape(s) at $1 a piece")
print("1 orange(s) at $3 a piece")
print(f"Sub Total: ${total:.2f}")
tax = total * 0.05
print(f"5% tax: ${tax}")
final_total = total + tax
print(f"Total: ${final_total}")










