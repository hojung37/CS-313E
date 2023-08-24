#  File: Poker.py

#  Description: Creating poker games

#  Student Name: Ho jung Kim 

#  Student UT EID: hk25322

#  Partner Name: n/a

#  Partner UT EID: n/a

#  Course Name: CS 313E

#  Unique Number: 52530

#  Date Created: 9/19

#  Date Last Modified: 9/20

import sys 
import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  # constructor
  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  # string representation of a Card object
  #set value/rank for each card 
  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  # equality tests
  #equal 
  def __eq__ (self, other):
    return self.rank == other.rank
  
  # not equal 
  def __ne__ (self, other):
    return self.rank != other.rank
  
  #lower than 
  def __lt__ (self, other):
    return self.rank < other.rank
  
  #lower and equal 
  def __le__ (self, other):
    return self.rank <= other.rank
  
  #greater than 
  def __gt__ (self, other):
    return self.rank > other.rank

  #greater and equal 
  def __ge__ (self, other):
    return self.rank >= other.rank

class Deck (object):
  # constructor
  def __init__ (self, num_decks = 1):
    self.deck = []
    for i in range (num_decks):
      for suit in Card.SUITS:
        for rank in Card.RANKS:
          card = Card (rank, suit)
          self.deck.append (card)

  # shuffle the deck
  def shuffle (self):
    random.shuffle (self.deck)

  # deal a card
  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  # constructor
  def __init__ (self, num_players = 2, num_cards = 5):
    self.deck = Deck()
    self.deck.shuffle()
    self.players_hands = []
    self.numCards_in_Hand = num_cards

    # deal the cards to the players
    for i in range (num_players):
      hand = []
      for j in range (self.numCards_in_Hand):
        hand.append (self.deck.deal())
      self.players_hands.append (hand)

  # simulate the play of poker
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players_hands)):
      sorted_hand = sorted (self.players_hands[i], reverse = True)
      self.players_hands[i] = sorted_hand
      hand_str = ''
      for card in sorted_hand:
        hand_str = hand_str + str (card) + ' '
      print ('Player ' + str(i + 1) + ' : ' + hand_str)

    # determine the type of each hand and print
    hand_type = []	# create a list to store type of hand
    hand_points = []	# create a list to store points for hand

    # determine winner and print


  # determine if a hand is a royal flush
  # takes as argument a list of 5 Card objects
  # returns a number (points) for that hand
  #[A,K,Q,J,10] = 14,13,12,11,10
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
    #for i in range 0,1,2,3
    #hand 0's suit = hand 1's suit
    #hand 1's suit = hand 2's suit
    #hand 2's suit = hand 3's suit
    #hand 3's suit = hand 4's suit
    #basically saying all cards have same suit
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    rank_order = True
    for i in range (len(hand)):
      #for i in range 0,1,2,3,4
      #hand 0's rank = 14
      #hand 1's rank = 13
      rank_order = rank_order and (hand[i].rank == 14 - i)

    if (not rank_order):
      return 0, ''
    
    #calculate points
    points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Royal Flush'
  
  #10,9,8,7,6
  def is_straight_flush (self, hand):
    same_suit = True 
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''
    
    rank_order = True
    for i in range (len(hand)):
      #for i in range 0,1,2,3
      #hand 0's rank = hand 1's rank + 0
      #hand 1's rank = hand 2's rank + 1 
      rank_order = rank_order and (hand[i].rank == hand[0].rank - i)
      #rank_order = rank_order and (hand[i].rank == hand[i+1].rank - i)

    if (not rank_order):
      return 0, ''

    points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight Flush'
    
    ...
  #4 of same rank,last one different rank 
  def is_four_kind (self, hand):
    #is_four_kind = False
    #point = 0
    #if hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank:
    #  if hand[3].rank != hand[4].rank: 
    #    diff_rank = hand[4].rank 
    #    #is_four_kind = True
    #0,1,2,3 same and 4 different
    #1,2,3,4 same and 0 different

    
    if hand[0].rank == hand[1].rank == hand[2].rank == hand[3].rank:
      if hand[3].rank != hand[4].rank: 
        return 8 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'Four of a Kind'

      
    elif hand[1].rank == hand[2].rank == hand[3].rank == hand[4].rank:
      if hand[4].rank != hand[0].rank: 
        return 8 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3 +  (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1 + (hand[0].rank), 'Four of a Kind'

    return 0, ''
    #    diff_rank = hand[0].rank
    #    is_four_kind = True
  

    
  
  
  #3 of same rank, 2 of different rank that are same
  #0,1,2 same and 3,4 same and 2,3 are different
  #2,3,4 same and 0,1 same and 0,4 are different 
  def is_full_house (self, hand):
    if hand[0].rank == hand[1].rank == hand[2].rank:
      if hand[3].rank == hand[4].rank: 
        if hand[2].rank != hand[3].rank: 
          return 7 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'Full House' 

    elif hand[2].rank == hand[3].rank == hand[4].rank:
      if hand[0].rank == hand[1].rank: 
        if hand[4].rank != hand[0].rank: 
          return 7 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3 + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1 + (hand[1].rank), 'Full House'
    
    return 0, ''  



  #5 of same suit 
  def is_flush (self, hand):
    same_suit = True 
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return 0, ''

    points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)
  
    return points, 'Flush'
    
    
  #5 cards of sequential rank [7,6,5,4,3] 
  def is_straight (self, hand):
    rank_order = True
    for i in range (len(hand)):
      #for i in range 0,1,2,3
      #hand 0's rank = hand 1's rank + 0
      #hand 1's rank = hand 2's rank + 1 
      rank_order = rank_order and (hand[i].rank == hand[0].rank - i)
      #rank_order = rank_order and (hand[i].rank == hand[i+1].rank - i)

    if (not rank_order):
      return 0, ''

    points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    points = points + (hand[4].rank)

    return points, 'Straight'
  
  #3 of same rank, 2 of other rank that are different from each other
  #0,1,2 same and 3,4 different
  #1,2,3 same and 0,4 different
  #2,3,4 same and 0,1 different 
  def is_three_kind (self, hand):
    if hand[0].rank == hand[1].rank == hand[2].rank:
      if hand[2].rank != hand[3].rank: 
        if hand[3].rank != hand[4].rank: 
          return 4 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'Three of a Kind'

    elif hand[1].rank == hand[2].rank == hand[3].rank:
      if hand[3].rank!= hand[4].rank: 
        if hand[0].rank != hand[4].rank: 
          return 4 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3 + (hand[3].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1 + (hand[4].rank), 'Three of a Kind'

    elif hand[2].rank == hand[3].rank == hand[4].rank:
      if hand[4].rank!= hand[0].rank: 
        if hand[0].rank != hand[1].rank: 
          return 4 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3 + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1 + (hand[1].rank), 'Three of a Kind'
    return 0, '' 
 


  #2 of same rank, 2 of different rank that are same, 1 of other rank 
  #when 0,1 same 2,3 same, 4 different
  #when 0,1 same 3,4 same, 2 different
  #when 1,2 same 3,4 same, 0 different 
  def is_two_pair (self, hand):
    if (hand[0].rank == hand[1].rank):
      if (hand[2].rank == hand[3].rank):
        if (hand[0].rank != hand[4].rank) and (hand[2].rank != hand[4].rank):
          return 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'Two Pair'
    
    if (hand[1].rank == hand[2].rank):
        if (hand[3].rank == hand[4].rank):
          if (hand[1].rank != hand[0].rank) and (hand[3].rank != hand[0].rank):
            return 3 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3 + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1 + (hand[0].rank), 'Two Pair'

    if (hand[0].rank == hand[1].rank):
        if (hand[3].rank == hand[4].rank):
          if (hand[1].rank != hand[2].rank) and (hand[3].rank != hand[2].rank):
            return 3 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1 + (hand[2].rank), 'Two Pair'

    return 0, ''




  # determine if a hand is one pair
  # takes as argument a list of 5 Card objects
  # returns the number of points for that hand
  #2 of same rank, 3 of other rank that are different from each other
  def is_one_pair (self, hand):
    for i in range (len(hand)):
      if (hand[0].rank == hand[1].rank):
        return 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'One Pair'
    
      if (hand[1].rank == hand[2].rank):
        return 2 * 15 ** 5 + (hand[1].rank) * 15 ** 4 + (hand[2].rank) * 15 ** 3 + (hand[3].rank) * 15 ** 2 + (hand[4].rank) * 15 ** 1 + (hand[0].rank), 'One Pair' 

      if (hand[2].rank == hand[3].rank):
        return 2 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3 + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1 + (hand[1].rank), 'One Pair' 
    
      if (hand[3].rank == hand[4].rank):
        return 2 * 15 ** 5 + (hand[3].rank) * 15 ** 4 + (hand[4].rank) * 15 ** 3 + (hand[0].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1 + (hand[2].rank), 'One Pair'  
    
    return 0,''


    #one_pair = False
    #for i in range (len(hand) - 1):
    #  if (hand[i].rank == hand[i + 1].rank):
    #    one_pair = True
    #    break
    #if (not one_pair):
    #  return 0, ''

    #points = 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
    #points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
    #points = points + (hand[4].rank)

    #return points, 'One Pair'

  
    #if (hand[0].rank == hand[1].rank):
    #  if (hand[1].rank != hand[2].rank) and (hand[2].rank != hand[3].rank) and (hand[3].rank != hand[4].rank):
    #          return 2 * 15 ** 5 + (hand[2].rank) * 15 ** 4 + (hand[3].rank) * 15 ** 3 + (hand[4].rank) * 15 ** 2 + (hand[0].rank) * 15 ** 1 + (hand[1].rank), 'One Pair'
    
    #if (hand[1].rank == hand[2].rank):
    #  if (hand[2].rank != hand[3].rank):
    #    if (hand[3].rank != hand[4].rank) and (hand[4].rank != hand[0].rank):
    #      return 2 * 15 ** 5 + (hand[3].rank) * 15 ** 4 + (hand[4].rank) * 15 ** 3 + (hand[0].rank) * 15 ** 2 + (hand[1].rank) * 15 ** 1 + (hand[2].rank)

    #if (hand[2].rank == hand[3].rank):
    #  if (hand[3].rank != hand[4].rank):
    #    if (hand[4].rank != hand[1].rank) and (hand[1].rank != hand[0].rank):
    #      return 2 * 15 ** 5 + (hand[4].rank) * 15 ** 4 + (hand[0].rank) * 15 ** 3 + (hand[1].rank) * 15 ** 2 + (hand[2].rank) * 15 ** 1 + (hand[3].rank)
    
    #if (hand[3].rank == hand[4].rank):
    #  if (hand[3].rank != hand[2].rank):
    #    if (hand[0].rank != hand[1].rank) and (hand[1].rank != hand[2].rank):
    #      return 2 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank)
    
    #return 0,''



  #all different rank and suit 
  def is_high_card (self,hand):
    #return hand[0].rank 
    #for i in range (len(hand)):
    #  if hand[0].rank: 
    #    return True
    card_rank = hand[0].rank 
    return 1 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3 + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1 + (hand[4].rank), 'High Card'

    ...
def main():
  # read number of players from stdin
  line = sys.stdin.readline()
  line = line.strip()
  num_players = int(line)

  
  if (num_players < 2) or (num_players > 6):
    return
  print()
  

  # create the Poker object
  game = Poker (num_players)

  # play the game
  game.play()
  

if __name__ == "__main__":
  main() 

