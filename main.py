import math
import random

# create a list of a deck of cards in poker
suits = ['spades', 'hearts', 'clubs', 'diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# define a deck of cards as a list of tuples, where each tuple is a (suit, rank) pair
deck = [(suit, rank) for suit in suits for rank in ranks]

# define a function that shuffles the deck of cards
def shuffle_deck(deck):
    random.shuffle(deck)

# define a function that deals a number of cards to each player
def deal_cards(deck, num_cards, players):
    for i in range(num_cards):
        for player in players:
            player.append(deck.pop())
            print('Dealt %s to player %d' % (player[-1], players.index(player) + 1))

#define a function that deals a number of cards to the table
def deal_table(deck, num_cards, table):
    for i in range(num_cards):
        table.append(deck.pop())
        print('Dealt %s to the table' % (table))
    return table

# define a function that prints the cards held by each player
def print_cards(players):
    for i, player in enumerate(players):
        print('Player %d: %s' % (i + 1, player))

# define a function that evaluates the strength of a given hand
def evaluate_hand(hand):
    
    # first, check for a straight flush (five cards of the same suit in sequence)
    straight_flush = True
    for i in range(1, len(hand)):
        if hand[i][0] != hand[i-1][0] or ranks.index(hand[i][1]) != ranks.index(hand[i-1][1]) + 1:
            straight_flush = False
            break
    if straight_flush:
        return (8, max([ranks.index(card[1]) for card in hand]))
    
    # then, check for four of a kind (four cards with the same rank)
    four_kind = False
    for rank in ranks:
        if [card for card in hand if card[1] == rank] == 4:
            four_kind = True
            break
    if four_kind:
        return (7, ranks.index(rank))

    three_kind = False
    two_kind = False
    for rank in ranks:
        if [card for card in hand if card[1] == rank] == 3:
            three_kind = True
        elif [card for card in hand if card[1] == rank] == 2:
            two_kind = True
    if three_kind and two_kind:
        return (6, ranks.index(rank))
    # then, check for a full house (three of a kind and a pair)
    full_house = False
    for rank in ranks:
        if [card for card in hand if card[1] == rank] == 3:
            for rank2 in ranks:
                if [card for card in hand if card[1] == rank2] == 2:
                    full_house = True
                    break
            full_house = True
            break
    if full_house:
        return (6, ranks.index(rank))

    # then, check for a flush (five cards of the same suit)
    flush = False
    for suit in suits:
        if [card for card in hand if card[0] == suit] == 5:
            flush = True
            break
    if flush:
        return (5, max([ranks.index(card[1]) for card in hand]))

    # then, check for a straight (five cards in sequence)
    straight = True
    for i in range(1, len(hand)):
        if ranks.index(hand[i][1]) != ranks.index(hand[i-1][1]) + 1:
            straight = False
            break
    if straight:
        return (4, max([ranks.index(card[1]) for card in hand]))
    
    # then, check for three of a kind (three cards with the same rank)
    three_kind = False
    for rank in ranks:
        if [card for card in hand if card[1] == rank] == 3:
            three_kind = True
            break
    if three_kind:
        return (3, ranks.index(rank))

    # then, check for two pairs (two cards with the same rank and two cards with another same rank)
    two_pairs = False
    for rank in ranks:
        if [card for card in hand if card[1] == rank] == 2:
            if two_pairs:
                two_pairs = True
                break
            else:
                two_pairs = True
    if two_pairs:
        return (2, ranks.index(rank))

# Checking if there is a pair in the hand.
    pair = False
    for rank in ranks:
        if [card for card in hand if card[1] == rank] == 2:
            pair = True
            break
    if pair:
        return (1, ranks.index(rank))

# Returning the highest card in the hand.
    return (0, max([ranks.index(card[1]) for card in hand]))

def determine_winner(players, table):
    """
    It determines the winner of the game.
    
    :param players: a list of player objects
    :param table: a list of 5 cards
    """
# Evaluating the hand of each player and the table cards.
    hands = [evaluate_hand(player + table) for player in players]

# Determining the winner.
    winner = 0
    for i in range(1, len(hands)):
        if hands[i][0] > hands[winner][0] or (hands[i][0] == hands[winner][0] and hands[i][1] > hands[winner][1]):
            winner = i
    return winner

def play_poker(players):
    """
    This function shuffles the deck and deals the cards to the players.
    
    :param players: a list of player objects
    """
    shuffle_deck(deck)

# Dealing 2 cards to each player.
    deal_cards(deck, 2, players)
    
# Creating a list called table and then it is dealing 5 cards to the table.
    table = []
    deal_table(deck, 5, table)
    
# Printing the cards of each player.
    print_cards(players)
    
# Printing the cards of each player and the table cards.
    print(" ")
    print("Player 1")
    print(' '.join(players[0][0]).title() + ' ' + ' '.join(players[0][1]).title())
    print(" ")
    print("Player 2")
    print(' '.join(players[1][0]).title() + ' ' + ' '.join(players[1][1]).title())
    print(" ")
    print("Player 3")
    print(' '.join(players[2][0]).title() + ' ' + ' '.join(players[2][1]).title())
    print(" ")
    print("Player 4")
    print(' '.join(players[3][0]).title() + ' ' + ' '.join(players[3][1]).title())
    print(" ")
    print('The Table Cards')
    print(' '.join(table[0]).title() + ' ' + ' '.join(table[1]).title() + ' ' + ' '.join(table[2]).title() + ' ' + ' '.join(table[3]).title() + ' ' + ' '.join(table[4]).title())
    print(" ")

    # determine the winner
    winner = determine_winner(players, table)
    print(" ")
    print('Player %d wins!' % (winner + 1))

play_poker([[], [], [], []])
