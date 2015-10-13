from random import shuffle, randint
from operator import itemgetter
from player import *

class Simulator:
    def generate_cards(self):
        deck = [(x, 1) for x in range(1, 13)] + [(x, 2) for x in range(1, 13)]
        shuffle(deck)

        cards = []
        for player in range(4):
            hand = deck[6*player:6*(player+1)]

            hand.sort(key=itemgetter(0))
            cards.append(hand)

        return cards

    def new_game(self, players):
        shuffle(players)
        self.cards = self.generate_cards()
        self.players = []

        for i, player in enumerate(players):
            player_cards = []
            for j, hand in enumerate(self.cards):
                if i != j:
                    player_cards.append([('x', card[1]) for card in self.cards[j]])
                else:
                    player_cards.append(list(self.cards[j]))
            self.players.append(player(i, player_cards))
    
    def record_pass_all(self, pid, card_passed):
        passed_to = (pid + 2) % 4
        for i in range(4):
            if i == passed_to:
                self.players[i].record_pass((pid, card_passed, self.cards[pid][card_passed][0]))
            else:
                self.players[i].record_pass((pid, card_passed, 'x'))

    def record_guess_all(self, guess):
        for i in range(4):
            self.players[i].record_guess(guess)

    def run(self):
        curr_player = 0
        teammate = (curr_player + 2)%4
        
        for _ in range(24):
            card = self.players[teammate].make_pass()
            #TODO check that pass is legit
            self.record_pass_all(curr_player, card)

            guess = self.players[curr_player].make_guess()

            #TODO check that guess is legit
            if self.cards[guess[0]][guess[1]] == guess[2]:
                self.record_guess_all((curr_player, guess[0], guess[1], guess[2], True, guess[1], guess[2]))
            else:
                self.record_guess_all((curr_player, guess[0], guess[1], guess[2], False, guess[3], self.cards[curr_player][guess[3]][0]))

            curr_player = (curr_player + 1)%4

simulator = Simulator()
simulator.new_game([Player, Player, Player, Player])
simulator.run()
