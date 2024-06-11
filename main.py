import random
from person import Person

def raffle(p1, p2, p3):
    raffle = random.random()
    if raffle < 0.33:
        return p1
    elif raffle < 0.66:
        return p2
    else:
        return p3

def add_prize_to_raffle_winner(p):
    p.set_net_worth(p.get_net_worth() + 10000.0)

def main():
    p1 = Person("Pedro", 20, 123456, 10000.0)
    p2 = Person("Juan", 25, 123457, 20000.0)
    p3 = Person("Maria", 30, 123458, 30000.0)
    winner = raffle(p1, p2, p3)
    print("The winner is:", winner.get_name())
    add_prize_to_raffle_winner(winner)
    print("The winner's net worth is now:", winner.get_net_worth())

if __name__ == "__main__":
    main()
