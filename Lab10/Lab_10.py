import random
__author__ = "Anthony Peloso and Daniel Williamson"

# created the class Card with lists for the suit, value, and name.
# we used mod and floored division to associate the card with its suit


class Card:
    def __init__(self, card_num):
        suit = ["Hearts", "Spades", "Clubs", "Diamonds"]
        self.suit = suit[card_num//13]
        value = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
        self.value = value[card_num % 13]
        name = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack',
                'Queen', 'King', 'Ace']
        self.name = name[card_num % 13]
        self.is_face_up = True

# here is where we set the default to face up
# below, we created methods and had it print the name and suit

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.name

    def get_value(self):
        return self.value

    def face_down(self):
        self.is_face_up = False

    def face_up(self):
        self.is_face_up = True

    def __str__(self):
        if self.is_face_up is True:
            return self.name + ' of ' + self.suit
        else:
            return '<facedown>'

# above, we created a conditional statement to whether it printed the card
# number and suit or kept that information hidden
# below, we created the ChipBank and used the conditional so that the bank
# would not go negative


class ChipBank:
    def __init__(self, value):
        self.value = value

    def withdraw(self, w_d):
        if self.value - w_d >= 0:
            self.value = self.value - w_d
            return w_d
        elif self.value - w_d < 0:
            amount_before_w_d = self.value
            self.value = self.value - self.value
            return amount_before_w_d

    def deposit(self, deposit):
        self.value = self.value + deposit

    def __str__(self):
        black_chip = self.value//100
        green_chip = self.value % 100//25
        red_chip = self.value % 100 % 25//5
        blue_chip = self.value % 100 % 25 % 5//1
        str_black_chip = str(black_chip)
        str_green_chip = str(green_chip)
        str_red_chip = str(red_chip)
        str_blue_chip = str(blue_chip)
        str_self_value = str(self.value)
        return str_black_chip + " blacks, " + str_green_chip + " greens, "\
            + str_red_chip + " reds, " + str_blue_chip + " blues -" + \
            " Totaling - $" + str_self_value

# above, we associated the value to its chip color
# we also had it return the number of chips available in each color.

if __name__ == "__main__":
    deck = []
    for i in range(52):
        my_card = Card(i)
        deck.append(my_card)
        print(my_card)
    print(random.choice(deck))

    card = Card(37)
    print(card)
    print(card.get_value())
    print(card.get_suit())
    print(card.get_rank())
    card.face_down()
    print(card)
    card.face_up()
    print(card)

    cs = ChipBank(149)
    print(cs)
    cs.deposit(7)
    print(cs.value)
    print(cs)
    print(cs.withdraw(84))
    print(cs)
    cs.deposit(120)
    print(cs)
    print(cs.withdraw(300))

# above, we took the test from the lab
