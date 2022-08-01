# from replit import clear

from os import system, name
# Modify Run Configuration -> Execution -> Emulate terminal in output console


def clear():
    """Clear Run window"""
    # https://stackoverflow.com/questions/27241268/clear-pycharm-run-window

    # # for windows
    if name == "nt":
        _ = system("cls")

    # # for mac and linux
    # else:
    #     _ = system('clear')


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")


bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bid? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type yes or no.\n")
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear()
