from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import itertools
import random
import time

doc = """
"""


class Constants(BaseConstants):

    name_in_url = 'experiment6543_2nd'
    players_per_group = 2
    num_rounds = 1
    
    timeout_decision = 45
    timeout_results = 30

    prize = 100
    ratio_costprod = 4

    bonus = 50

class Subsession(BaseSubsession):

    def creating_session(self):
        for p in self.get_players():
            p.treatment = p.participant.vars['treatment']
            if p.treatment == 'budget':
                p.endowment1 = 25
            else:
                p.endowment1 = 100

    def group_by_arrival_time_method(self, waiting_players):
        baseline = [p for p in waiting_players 
                    if p.participant.vars['treatment'] == 'baseline']
        productive = [p for p in waiting_players 
                      if p.participant.vars['treatment'] == 'productive']
        cost = [p for p in waiting_players 
                if p.participant.vars['treatment'] == 'cost']
        budget = [p for p in waiting_players 
                  if p.participant.vars['treatment'] == 'budget']

        if len(baseline) >= 2:
            return baseline[:2]
        if len(productive) >= 2:
            return productive[:2]
        if len(cost) >= 2:
            return cost[:2]
        if len(budget) >= 2:
            return budget[:2]
        for player in waiting_players:
            if player.waiting_too_long():
                # make a single-player group.
                player.participant.vars['group_formed'] = False
                player.no_group = True
                return [player]

class Group(BaseGroup):

    winner1 = models.IntegerField(initial=0)
    winner2 = models.IntegerField(initial=0)
    expiry_group = models.BooleanField(initial=False)
    total_tickets1 = models.IntegerField()
    total_tickets2 = models.IntegerField()

    def set_earnings1(self):
        if self.expiry_group is False:
            self.total_tickets1 = sum([p.tokens1 for p in self.get_players()])
            if self.total_tickets1 != 0:
                self.winner1 = random.choices([p.id_in_group for p in
                                               self.get_players()],
                                              weights=[p.tokens1 for p in
                                                       self.get_players()])[0]
                for p in self.get_players():
                    p.earnings1 = p.endowment1 - p.tokens1 + Constants.prize if \
                    p.id_in_group is self.winner1 else p.endowment1 - \
                    p.tokens1
            else:
                for p in self.get_players():
                    p.earnings1 = p.endowment1 - p.tokens1

    def set_earnings2(self):
        if self.expiry_group is False:
            for p in self.get_players():
                if p.treatment in ['baseline', 'budget']:
                    p.tickets2 = p.tokens2
                elif p.treatment == 'productive':
                    p.tickets2 = p.tokens2*Constants.ratio_costprod if \
                                    p.id_in_group is self.winner1 else p.tokens2
                elif p.treatment == 'cost':
                    p.tickets2 = p.tokens2 if p.id_in_group is self.winner1 else \
                                    p.tokens2/Constants.ratio_costprod
            self.total_tickets2 = sum([p.tickets2 for p in self.get_players()])
            if self.total_tickets2 != 0:
                self.winner2 = random.choices([p.id_in_group for p in
                                               self.get_players()],
                                              weights=[p.tickets2 for p in
                                                       self.get_players()])[0]
                for p in self.get_players():
                    p.earnings2 = p.earnings1 - p.tokens2 + Constants.prize if \
                                    p.id_in_group is self.winner2 else \
                                    p.earnings1 - p.tokens2
            else:
                for p in self.get_players():
                    p.earnings2 = p.earnings1 - p.tokens2

    def set_expiry(self):
        self.expiry_group = True 
        for p in self.get_players():
            p.expiry_passive = True if p.expiry is False else False
            p.participant.vars['expiry_group'] = self.expiry_group
            p.participant.vars['expiry'] = p.expiry
            p.participant.vars['expiry_passive'] = p.expiry_passive


class Player(BasePlayer):

    # treatment
    treatment = models.StringField()

    # maximum waiting time
    no_group = models.BooleanField(initial=False)

    def waiting_too_long(self):
        return time.time() - self.participant.vars['wait_page_arrival'] > 3*60


    # variables for the game
    endowment1 = models.IntegerField()
    tokens1 = models.IntegerField(label="How many tokens would you like to use \
                                  to buy lottery tickets in Stage 1?", min=0)
    tokens2 = models.IntegerField(label="How many tokens would you like to use \
                                  to buy lottery tickets in Stage 2?", min=0)
    tickets2 = models.IntegerField()
    other_tokens2 = models.IntegerField()
    earnings1 = models.IntegerField()
    other_earnings1 = models.IntegerField()
    earnings2 = models.IntegerField()
    bonus1 = models.IntegerField()
    bonus2 = models.IntegerField()

    def tokens1_max(self):
        return self.endowment1

    def tokens2_max(self):
        return self.earnings1

    def tokens2_error_message(self, value):
        if self.treatment == 'cost' and \
            self.tokens2%Constants.ratio_costprod != 0 and \
            self.id_in_group is not self.group.winner1:
            return "The number of tokens must be a multiple of 4, i.e. \
                the price of each ticket"

    # dropouts
    expiry = models.BooleanField(initial=False) 
    expiry_passive = models.BooleanField(initial=False)
        
    # forms for belief elicitation
    belief2 = models.IntegerField(label=
                                  "In your estimate, how many tokens will your"
                                  " co-participant use to buy lottery tickets in"
                                  " Stage 2?", min=0)

    def belief2_max(self):
        self.other_earnings1 = [p.earnings1 for p in 
                                    self.get_others_in_group()][0]
        return self.other_earnings1

    def set_earnings_beliefs(self):
        self.other_tokens2 = [p.tokens2 for p in self.get_others_in_group()][0]
        if self.participant.vars['belief1'] in \
                range(self.group.total_tickets1 - self.tokens1 - 1,
                      self.group.total_tickets1 - self.tokens1 + 2):
            self.bonus1 = Constants.bonus
        else:
            self.bonus1 = 0
        if self.belief2 in range(self.other_tokens2 - 1, 
                                 self.other_tokens2 + 2):
            self.bonus2 = Constants.bonus
        else:
            self.bonus2 = 0

