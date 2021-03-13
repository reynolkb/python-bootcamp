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

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        # card passed in
        # from deck.deal() --> single card(suit, rank)
        self.cards.append(card)
        self.value += values[card.rank]

        # track aces
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        # if total value is greater than 21 and I still have an ace
        # then change my ace to be a 1 instead of an 11
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet? '))
        except ValueError:
            print('Sorry, a bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

def hit(deck,hand):
    
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's' ")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  # hit() function defined above

        elif x[0].lower() == 's':
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again.")
            continue
        break

def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)

def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")

while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chips()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break