from test import logo
from replit import clear

print(logo)
ask = 1
b_dict = {}
price = 0
name_win = ""


def bdict(b_name, b_price):
    b_dict[b_name] = b_price


while ask != 2:
    print('Welcome to the secret auction program. What is your name?: ', end="")
    name = str(input())
    bid = int(input("What's your bid?: $"))
    bdict(b_name=name, b_price=bid)
    ask = int(input("Are there any other bidders? Type 'yes'(1) or 'no'(2): "))
    clear()

for key in b_dict:
    price = b_dict[key]
    if price < b_dict[key]:
        price = b_dict[key]
    name_win = key
print(f"The winner is {name_win} with a bid of ${price}!")
