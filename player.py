import random

# Players have ids 0 through 3. 
# Cards are of the form (rank:1-12 or 'x' for unknown, suit:1-2)
# Passes are of the form (passer-id:0-3, card-passed:0-5, rank:'x' or 1-12)
# Guesses are of the form (guesser-id:0-3, target-id:0-3, target-card:0-5, rank-guess, 
#                          correct?, revealed-card:0-5, rank:1-12)
class Player:

    def __init__(self, player_id, cards):
        self.id = player_id
        self.cards = cards
        self.pass_log = []
        self.guess_log = []

    def claim(self):
        '''
            Return False if no wish to claim. 
            Else, return self.cards
        '''
        return NotImplementedError

    def make_pass(self):
        '''
            Return number indicating which card to pass
        '''
        return random.randint(0,5)
        raise NotImplementedError

    def make_guess(self):
        '''
            Return tuple (target-id, target-card, rank-guess, flipped-card-if-wrong)
        '''
        return (random.randint(0,3), random.randint(0,5), random.randint(1,12), random.randint(0, 5))
        raise NotImplementedError

    def record_pass(self, player_pass):
        if player_pass[2] != 'x':
            flipped_card = self.cards[player_pass[0]][player_pass[1]]
            self.cards[player_pass[0]][player_pass[1]] = (player_pass[2], flipped_card[1])

        self.pass_log.append(player_pass)

    def record_guess(self, guess):
        cardholder_id = guess[1] if guess[4] else guess[0]

        flipped_card = self.cards[cardholder_id][guess[5]]
        self.cards[cardholder_id][guess[5]] = (guess[6], flipped_card[1])
        
        self.guess_log.append(guess)
        
