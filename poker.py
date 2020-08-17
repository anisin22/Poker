from cards import deck
from players import player1, board, player2, player3, player4, player5, player6, player7, player8, player9

class PokerScorer(object):

    def __init__(self, cards):
        if not len(cards) == 5:
            return "Error: wrong number of cards"
        self.cards = cards

def score_interpreter(player):
        list_of_hand_types = ["High Card", "One Pair", "Two Pair", "Three of a Kind", "Straight", "Flush",
                              "Full House",
                              "Four of a Kind", "Straight Flush", "Royal Flush"]
        list_of_values_to_interpret = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
                                       "Jack",
                                       "Queen",
                                       "King", "Ace"]
        hand_type = list_of_hand_types[player.score[0]]
        mod1 = list_of_values_to_interpret[player.score[1]]
        mod2 = list_of_values_to_interpret[player.score[2]]
        mod3 = list_of_values_to_interpret[player.score[3]]
        if player.score[0] == 0:
            return hand_type + ": " + mod3
        if player.score[0] == 1:
            return hand_type + ": " + mod1 + "s"
        if player.score[0] == 2:
            return hand_type + ": " + mod1 + "s" + " and " + mod2 + "s"
        if player.score[0] == 3:
            return hand_type + ": " + mod1 + "s"
        if player.score[0] == 4:
            return hand_type + ": " + mod1 + " High"
        if player.score[0] == 5:
            return hand_type + ": " + mod1 + " High"
        if player.score[0] == 6:
            return hand_type + ": " + mod1 + "s" + " and " + mod2 + "s"
        if player.score[0] == 7:
            return hand_type + ": " + mod1 + "s"
        if player.score[0] == 8:
            return hand_type + ": " + mod1 + " High"
        if player.score[0] == 9:
            return hand_type

def winner(player1, player2):
    scoredict = {"Twos": 1, "Threes":2, "Fours": 3, "Fives": 4, "Sixs":5, "Sevens":6, "Eights": 7, "Nines":8,"Tens": 9, "Jacks": 10, "Queens": 11, "Kings": 12, "Aces": 13}
    scoredictrank = {"High Card":1, "One Pair":2, "Two Pair":3, "Three of a Kind":4,"Straight":5,"Flush":6,"Full House":7,"Four of a Kind":8,"Straight Flush":9, "Royal Flush":10}
    colonx = player1.rfind(":")
    colony = player2.rfind(":")
    rank1 = player1[:colonx]
    rank2 = player2[:colony]
    num1 = player1[colonx+2:]
    num2 = player2[colony+2:]
    if player1 == player2:
        return 1 #Tie
    if scoredictrank[rank1] > scoredictrank[rank2]:
        return 0   # "Player 1 wins with " + player1
    elif scoredictrank[rank1] < scoredictrank[rank2]:
        return 2   #  "Player 2 wins with " + player2
    else:
        if rank1 == "Two Pair":
            return "Both have two pairs need to fix XD" #FIX!!!!!
        if rank1 == "Straight":
            return "Both have straight need to fix XD"#FIX!!!
        if scoredict[num1] > scoredict[num2]:
            return 0  #"Player 1 wins with " + player1
        else:
            return 2  #"Player 2 wins with " + player2


num_players = input("Enter number of players(max of 9): ") #add check if input is number
new = int(num_players)
while new > 9:
    num_players = input("Enter number of players(max of 9): ")
    new = int(num_players)

deck.shuffle()

all_players = {"Player1": player1, "Player2": player2, "Player3": player3, "Player4": player4, "Player5": player5, "Player6": player6, "Player7": player7, "Player8": player8, "Player9": player9}

for i in range(new):
    current_player = "Player" + str(i + 1)
    deck.deal(all_players[current_player])
    deck.deal(all_players[current_player])
    print("Player "+ str(i+1) + " hand: ")
    print(all_players[current_player].cards)


deck.burn()
deck.deal(board)
deck.deal(board)
deck.deal(board)
deck.burn()
deck.deal(board)
deck.burn()
deck.deal(board)
print("The Board: ")
print(board.cards)

for j in range(new):
    current_player = "Player" + str(j + 1)
    board.hand_scorer(all_players[current_player])
    print("Player "+ str(j+1) + " has: ")
    print(score_interpreter(all_players[current_player]))

if new == 2:
    if (winner(score_interpreter(player1),score_interpreter(player2))) == 0:
        print( "Player 1 wins with " + score_interpreter(player1))
    elif (winner(score_interpreter(player1),score_interpreter(player2))) == 2:
        print ("Player 2 wins with " + score_interpreter(player2))
    else:
        print( "Tie")
if new == 3:
    if winner(score_interpreter(player1),score_interpreter(player2)) == 1:
        first_win = score_interpreter(player1)
        if winner(first_win, score_interpreter(player3)) == 1:
            print( "Tie")
        elif winner(first_win, score_interpreter(player3)) == 0:
            print( "Player 1 and Player 2 win with " + score_interpreter(player1))
        else:
            print( "Player 3 wins with " + score_interpreter(player3))
    elif winner(score_interpreter(player1),score_interpreter(player2)) == 0:
        first_win = score_interpreter(player1)
        if winner(first_win, score_interpreter(player3)) == 1:
            print( "Player 1 and Player 3 win with " + score_interpreter(player1))
        elif winner(first_win, score_interpreter(player3)) == 0:
            print( "Player 1 wins with " + score_interpreter(player1))
        else:
            print( "Player 3 wins with " + score_interpreter(player3))

    else:
        first_win = score_interpreter(player2)
        if winner(first_win, score_interpreter(player3)) == 1:
            print( "Player 2 and Player 3 win with " + score_interpreter(player2))
        elif winner(first_win, score_interpreter(player3)) == 0:
            print( "Player 2 wins with " + score_interpreter(player2))
        else:
            print( "Player 3 wins with " + score_interpreter(player3))
print(player1.score, player2.score)
#print(winner(score_interpreter(player1),score_interpreter(player2)))
