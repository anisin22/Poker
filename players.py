import itertools
from collections import Counter

class Player(object):
    def __init__(self):
        self.chips = 0
        self.stake = 0
        self.stake_gap = 0
        self.cards =  []
        self.score = []
        self.fold = False
        self.ready = False
        self.all_in = False
        self.list_of_attribites = []
        self.win = False

    def hand_scorer(self, player):
            seven_cards = player.cards + self.cards
            all_hand_combos = list(itertools.combinations(seven_cards, 5))
            list_of_all_score_possibilities = []
            for i in all_hand_combos:
                suit_list = []
                value_list = []
                for j in i:
                    suit_list.append(j.suit)
                    value_list.append(j.value)
                initial_value_check = list(reversed(sorted(value_list)))
                score1 = 0
                score2 = 0
                score3 = 0
                score4 = initial_value_check.pop(0)
                score5 = initial_value_check.pop(0)
                score6 = initial_value_check.pop(0)
                score7 = initial_value_check.pop(0)
                score8 = initial_value_check.pop(0)
                list_of_pair_values = []
                other_cards_not_special = []
                pair_present = False
                pair_value = int
                value_counter = dict(Counter(value_list))
                for value_name, count in value_counter.items():
                    if count == 2:
                        pair_present = True
                        pair_value = value_name
                        list_of_pair_values.append(value_name)
                if pair_present:
                    for value in value_list:
                        if value not in list_of_pair_values:
                            other_cards_not_special.append(value)
                    other_cards_not_special = list(reversed(sorted(other_cards_not_special)))
                    if len(set(list_of_pair_values)) == 1:
                        score1 = 1
                        score2 = max(list_of_pair_values)
                        try:
                            score3 = other_cards_not_special.pop(0)
                            score4 = other_cards_not_special.pop(0)
                            score5 = other_cards_not_special.pop(0)
                            score6 = other_cards_not_special.pop(0)
                            score7 = other_cards_not_special.pop(0)
                            score8 = other_cards_not_special.pop(0)
                        except IndexError:
                            pass
                    if len(set(list_of_pair_values)) == 2:
                        list_of_pair_values = list(reversed(sorted(list_of_pair_values)))
                        score1 = 2
                        score2 = list_of_pair_values.pop(0)
                        score3 = list_of_pair_values.pop(0)
                        try:
                            score4 = other_cards_not_special.pop(0)
                            score5 = other_cards_not_special.pop(0)
                            score6 = other_cards_not_special.pop(0)
                            score7 = other_cards_not_special.pop(0)
                            score8 = other_cards_not_special.pop(0)
                        except IndexError:
                            pass
                three_of_a_kind_value = int
                other_cards_not_special = []
                three_of_a_kind_present = False
                for value_name, count in value_counter.items():
                    if count == 3:
                        three_of_a_kind_present = True
                        three_of_a_kind_value = value_name
                if three_of_a_kind_present:
                    for value in value_list:
                        if value != three_of_a_kind_value:
                            other_cards_not_special.append(value)
                    other_cards_not_special = list(reversed(sorted(other_cards_not_special)))
                    score1 = 3
                    score2 = three_of_a_kind_value
                    try:
                        score3 = other_cards_not_special.pop(0)
                        score4 = other_cards_not_special.pop(0)
                        score5 = other_cards_not_special.pop(0)
                        score6 = other_cards_not_special.pop(0)
                        score7 = other_cards_not_special.pop(0)
                        score8 = other_cards_not_special.pop(0)
                    except IndexError:
                        pass
                if sorted(value_list) == list(range(min(value_list), max(value_list) + 1)):
                    score1 = 4
                    score2 = max(value_list)
                if sorted(value_list) == [0, 1, 2, 3, 12]:
                    score1 = 4
                    score2 = 3
                if len(set(suit_list)) == 1:
                    score1 = 5
                    score2 = max(value_list)
                if three_of_a_kind_present and pair_present:
                    score1 = 6
                    score2 = three_of_a_kind_value
                    score3 = pair_value
                four_of_a_kind_value = int
                other_card_value = int
                four_of_a_kind = False
                for value_name, count in value_counter.items():
                    if count == 4:
                        four_of_a_kind_value = value_name
                        four_of_a_kind: True
                for value in value_list:
                    if value != four_of_a_kind_value:
                        other_card_value = value
                if four_of_a_kind:
                    score1 = 7
                    score2 = four_of_a_kind_value
                    score3 = other_card_value
                if sorted(value_list) == [0, 1, 2, 3, 12] and len(set(suit_list)) == 1:
                    score1 = 8
                    score2 = 3
                if sorted(value_list) == list(range(min(value_list), max(value_list) + 1)) and len(set(suit_list)) == 1:
                    score1 = 8
                    score2 = max(value_list)
                    if max(value_list) == 12:
                        score1 = 9
                list_of_all_score_possibilities.append([score1, score2, score3, score4, score5, score6, score7, score8])
            best_score = max(list_of_all_score_possibilities)
            player.score = best_score

player1 = Player()
player2 = Player()
player3 = Player()
player4 = Player()
player5 = Player()
player6 = Player()
player7 = Player()
player8 = Player()
player9 = Player()
board = Player()
