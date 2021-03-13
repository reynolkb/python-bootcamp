# ---------------------------------------- Warmup ----------------------------------------
# # card
# # suit, rank, value
# import random

# suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
# ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
# values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
#          'Queen':10, 'King':10, 'Ace':11}

# class Card:
    
#     def __init__(self,suit,rank):
#         self.suit = suit
#         self.rank = rank
#         self.value = values[rank]
        
#     def __str__(self):
#         return self.rank + ' of ' + self.suit

# # deck
# class Deck:
    
#     def __init__(self):
#         # Note this only happens once upon creation of a new Deck
#         self.all_cards = [] 
#         for suit in suits:
#             for rank in ranks:
#                 # This assumes the Card class has already been defined!
#                 self.all_cards.append(Card(suit,rank))
                
#     def shuffle(self):
#         # Note this doesn't return anything
#         random.shuffle(self.all_cards)
        
#     def deal_one(self):
#         # Note we remove one card from the list of all_cards
#         return self.all_cards.pop()

# # player
# class Player:
    
#     def __init__(self,name):
#         self.name = name
#         # A new player has no cards
#         self.all_cards = [] 
        
#     def remove_one(self):
#         # Note we remove one card from the list of all_cards
#         # We state 0 to remove from the "top" of the deck
#         # We'll imagine index -1 as the bottom of the deck
#         return self.all_cards.pop(0)
    
#     def add_cards(self,new_cards):
#         if type(new_cards) == type([]):
#             self.all_cards.extend(new_cards)
#         else:
#             self.all_cards.append(new_cards)
    
    
#     def __str__(self):
#         return f'Player {self.name} has {len(self.all_cards)} cards.'

# # game setup
# player_one = Player("One")
# player_two = Player("Two")
# new_deck = Deck()
# new_deck.shuffle()

# for x in range(26):
#     player_one.add_cards(new_deck.deal_one())
#     player_two.add_cards(new_deck.deal_one())

# import pdb
# game_on = True

# round_num = 0
# while game_on:
    
#     round_num += 1
#     print(f"Round {round_num}")
    
#     # Check to see if a player is out of cards:
#     if len(player_one.all_cards) == 0:
#         print("Player One out of cards! Game Over")
#         print("Player Two Wins!")
#         game_on = False
#         break
        
#     if len(player_two.all_cards) == 0:
#         print("Player Two out of cards! Game Over")
#         print("Player One Wins!")
#         game_on = False
#         break
    
#     # Otherwise, the game is still on!
    
#     # Start a new round and reset current cards "on the table"
#     player_one_cards = []
#     player_one_cards.append(player_one.remove_one())
    
#     player_two_cards = []
#     player_two_cards.append(player_two.remove_one())
    
#     at_war = True

#     while at_war:


#         if player_one_cards[-1].value > player_two_cards[-1].value:

#             # Player One gets the cards
#             player_one.add_cards(player_one_cards)
#             player_one.add_cards(player_two_cards)
            
            
#             # No Longer at "war" , time for next round
#             at_war = False
        
#         # Player Two Has higher Card
#         elif player_one_cards[-1].value < player_two_cards[-1].value:

#             # Player Two gets the cards
#             player_two.add_cards(player_one_cards)
#             player_two.add_cards(player_two_cards)
            
#             # No Longer at "war" , time for next round
#             at_war = False

#         else:
#             print('WAR!')
#             # This occurs when the cards are equal.
#             # We'll grab another card each and continue the current war.
            
#             # First check to see if player has enough cards
            
#             # Check to see if a player is out of cards:
#             if len(player_one.all_cards) < 5:
#                 print("Player One unable to play war! Game Over at War")
#                 print("Player Two Wins! Player One Loses!")
#                 game_on = False
#                 break

#             elif len(player_two.all_cards) < 5:
#                 print("Player Two unable to play war! Game Over at War")
#                 print("Player One Wins! Player One Loses!")
#                 game_on = False
#                 break
#             # Otherwise, we're still at war, so we'll add the next cards
#             else:
#                 for num in range(5):
#                     player_one_cards.append(player_one.remove_one())
#                     player_two_cards.append(player_two.remove_one())

# ---------------------------------------- Milestone Project 2 ----------------------------------------

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

test_deck = Deck()
print(test_deck)