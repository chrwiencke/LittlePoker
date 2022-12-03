import random

# Creating a list of suits and ranks.
suits = ['spades', 'hearts', 'clubs', 'diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

# Creating a list of a deck of cards in poker.
deck = [(suit, rank) for suit in suits for rank in ranks]

def shuffle_deck(deck):
    """
    It shuffles the deck.
    
    :param deck: a list of cards
    """
    random.shuffle(deck)

def deal_cards(deck, num_cards, players):
    """
    It takes a deck of cards, a number of cards to deal, and a list of players, and deals the cards to
    the players.
    
    :param deck: a list of cards
    :param num_cards: The number of cards to deal to each player
    :param players: a list of lists, each list representing a player's hand
    """
    for i in range(num_cards):
        for player in players:
            player.append(deck.pop())
            print('Dealt %s to player %d' % (player[-1], players.index(player) + 1))

def deal_table(deck, num_cards, table):
    """
    It deals a card from the deck to the table.
    
    :param deck: a list of cards
    :param num_cards: the number of cards to deal to the table
    :param table: a list of cards
    :return: The table list is being returned.
    """
    for i in range(num_cards):
        table.append(deck.pop())
        print('Dealt %s to the table' % (table))
    return table

def print_cards(players):
    """
    It takes a list of players and prints out each player's name and cards.
    
    :param players: a list of lists of cards
    """
    for i, player in enumerate(players):
        print('Player %d: %s' % (i + 1, player))

def evaluate_hand(hand):
    """
    The above function evaluates the hand of a player.
    
    :param hand: a list of cards in the hand
    :return: a tuple. The first element of the tuple is the rank of the hand and the second element of
    the tuple is the rank of the highest card in the hand.
    """
# Sorting the hand of a player while taking into account the table cards.
    hand = sorted(hand, key=lambda x: ranks.index(x[1]))

# Creating a dictionary called rank_dict and it is setting the value of each key to 0.
    rank_dict = {key: 0 for key in ranks}

# Counting the number of unique ranks in the hand.
    for card in hand:
        rank_dict[card[1]] += 1

# Creating a dictionary called suit_dict and it is setting the value of each key to 0.
    suit_dict = {key: 0 for key in suits}

# Counting the number of unique suits in the hand.
    for card in hand:
        suit_dict[card[0]] += 1

# Counting the number of unique suits in the hand.
    num_unique_suits = len([key for key in suit_dict if suit_dict[key] > 0])

# Checking if there is a straight in the hand.
    num_consecutive_ranks = 1
    for i in range(len(ranks) - 1):
        if ranks[i] in rank_dict and ranks[i + 1] in rank_dict:
            num_consecutive_ranks += 1
        else:
            break

# Checking if there is a straight flush in the hand.
    if num_unique_suits == 1 and num_consecutive_ranks == 5:
        return 8, ranks.index(hand[-1][1])

# Checking if there is a four of a kind in the hand.
    if 4 in rank_dict.values():
        return 7, ranks.index([key for key in rank_dict if rank_dict[key] == 4][0])

# Checking if there is a full house in the hand.
    if 3 in rank_dict.values() and 2 in rank_dict.values():
        return 6, ranks.index([key for key in rank_dict if rank_dict[key] == 3][0])

# Checking if there is a flush in the hand.
    if num_unique_suits == 1:
        return 5, ranks.index(hand[-1][1])

# Checking if there is a straight in the hand.
    if num_consecutive_ranks == 5:
        return 4, ranks.index(hand[-1][1])
    
# Checking if there is a three of a kind in the hand.
    if 3 in rank_dict.values():
        return 3, ranks.index([key for key in rank_dict if rank_dict[key] == 3][0])

# Checking if there is two pairs in the hand.
    if list(rank_dict.values()).count(2) == 2:
        return 2, ranks.index([key for key in rank_dict if rank_dict[key] == 2][-1])

# Checking if there is a pair in the hand.
    if 2 in rank_dict.values():
        return 1, ranks.index([key for key in rank_dict if rank_dict[key] == 2][0])

# Returning the highest card in the hand.
    if 1 in rank_dict.values():
        return 0, ranks.index([key for key in rank_dict if rank_dict[key] == 1][-1])
    
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

# Determining the winner of the game.
    winner = determine_winner(players, table)
    print(" ")
    print('Player %d wins!' % (winner + 1))

# Creating a list of lists. Each list represents a player's hand.
play_poker([[], [], [], []])
