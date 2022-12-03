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

    # then, check for a full house (three of a kind and a pair)
    full_house = False
    three_kind = False
    two_kind = False
    for rank in ranks:
        if [card for card in hand if card[1] == rank] == 3:
            three_kind = True
        elif [card for card in hand if card[1] == rank] == 2:
            two_kind = True
    if three_kind and two_kind:
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

    # then, check for a pair (two cards with the same rank)
    pair = False
    for rank in ranks:
        if [card for card in hand if card[1] == rank] == 2:
            pair = True
            break
    if pair:
        return (1, ranks.index(rank))

    # finally, return the highest ranked card
    return (0, max([ranks.index(card[1]) for card in hand]))
# define a function that determines the winner with the table cards
def determine_winner(players, table):
    # first, evaluate the strength of each player's hand 
    hands = [evaluate_hand(player + table) for player in players]

    # then, determine the winner
    winner = 0
    for i in range(1, len(hands)):
        if hands[i][0] > hands[winner][0] or (hands[i][0] == hands[winner][0] and hands[i][1] > hands[winner][1]):
            winner = i
    return winner

# define a function that plays a game of poker
def play_poker(players):
    # shuffle the deck
    shuffle_deck(deck)

    # deal two cards to each player
    deal_cards(deck, 2, players)
    
    # deal five cards to the table
    table = []
    deal_table(deck, 5, table)
    
    # print the cards held by each player
    print_cards(players)
    
    # print all the cards for every player and table cards and print it in a nice way
    print(" ")
    print(f"Player 1: {players[0][0][0]} {players[0][0][1]}")
    print('Player 1: %s %s' % (players[0][0], players[0][1]))
    print('Player 2: %s %s' % (players[1][0], players[1][1]))
    print('Player 3: %s %s' % (players[2][0], players[2][1]))
    print('Player 4: %s %s' % (players[3][0], players[3][1]))
    print('Table: %s %s %s %s %s' % (table[0], table[1], table[2], table[3], table[4]))
    print(" ")


    # determine the winner
    winner = determine_winner(players, table)
    print(" ")
    print('Player %d wins!' % (winner + 1))

play_poker([[], [], [], []])
