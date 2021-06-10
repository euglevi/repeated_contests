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

doc = """
This is a one-period public goods game with 3 players.
"""


class Constants(BaseConstants):
    name_in_url = 'experiment6543'
    num_rounds = 1
    players_per_group = None

    # answers to control questions
    question1_answer = False
    question2_answer = "10/30" 
    question5_cost_answer = "1 token"
    question6_answer = True
    bonus = 30
    exchange_rate = 250

    timeout_decision = 45

class Subsession(BaseSubsession):

    def creating_session(self):
        treatments = itertools.cycle(self.session.config['treatments'])
        for p in self.get_players():
            p.participant.vars['treatment'] = next(treatments)
            p.treatment = p.participant.vars['treatment']
            p.participant.vars['group_formed'] = True
            p.participant.vars['expiry'] = False
            p.participant.vars['expiry_passive'] = False
            p.participant.vars['expiry_group'] = False
            if p.treatment == 'budget':
                p.endowment1 = 25
            else:
                p.endowment1 = 100
            if p.treatment == 'baseline':
                p.question3_answer = '90 tokens'
                p.question4_answer = '100 tokens'
                p.question5_answer = '1 ticket'
            elif p.treatment == 'budget':
                p.question3_answer = '15 tokens'
                p.question4_answer = '25 tokens'
                p.question5_answer = '1 ticket'
            elif p.treatment == 'cost':
                p.question3_answer = '90 tokens'
                p.question4_answer = '100 tokens'
            elif p.treatment == 'productive':
                p.question3_answer = '90 tokens'
                p.question4_answer = '100 tokens'
                p.question5_answer = '4 tickets'


class Group(BaseGroup):

    pass

class Player(BasePlayer):

    # treatment
    treatment = models.StringField()
    endowment1 = models.IntegerField()

    # recording and checking prolific id
    prolific_id = models.StringField(label="Please insert your ProlificID")
    prolific_id_check = models.StringField(label="Please confirm your ProlificID")

    # control questions
    question1 = models.BooleanField(label=
                                    "1. You will be matched with a different co-participant in each Stage.",
                                    widget=widgets.RadioSelect)
    question2 = models.StringField(label=
                                    "2. What is your chance of winning the prize in Stage 1?",
                                    choices=["10/20", "10/30", "20/30"],
                                    widget=widgets.RadioSelect)
    question3 = models.StringField(label=
                                    "3. Suppose you do not win the prize "
                                    "in Stage 1. What is your earning in Stage"
                                    " 1?", widget=widgets.RadioSelect)
    question4 = models.StringField(label=
                                    "4. Suppose you win the prize in Stage 1. "
                                    "How many tokens can you use to buy lottery"
                                    " tickets in Stage 2?",
                                    widget=widgets.RadioSelect)
    question5 = models.StringField(label=
                                    "5. Suppose you win the prize in Stage 1."
                                    " How many tickets does each token buy "
                                    "you in Stage 2?", 
                                    choices=['1 ticket', '2 tickets',
                                             '4 tickets'],
                                   widget=widgets.RadioSelect)
    question5_cost = models.StringField(label=
                                         "5. Suppose you win the prize in Stage 1."
                                         " How many tokens does each ticket "
                                         "cost you in Stage 2?", 
                                        choices=['1 token', '2 tokens', 
                                                 '4 tokens'],
                                         widget=widgets.RadioSelect)
    question6 = models.BooleanField(label=
                                    "6. Your final earnings from the experiment"
                                    " will be your earnings after:", 
                                    choices=[[False, "Stage 1"], [True, "Stage 2"]],
                                    widget=widgets.RadioSelect)
    question3_answer = models.StringField()
    question4_answer = models.StringField()
    question5_answer = models.StringField()
    mistake1 = models.IntegerField(initial=0)
    mistake2 = models.IntegerField(initial=0)
    mistake3 = models.IntegerField(initial=0)
    mistake4 = models.IntegerField(initial=0)
    mistake5 = models.IntegerField(initial=0)
    mistake6 = models.IntegerField(initial=0)

    def question3_choices(self):
        if self.treatment == 'budget':
            choices = ['25 tokens', '15 tokens', '0 tokens']
        else:
            choices = ['100 tokens', '90 tokens', '10 tokens']
        return choices

    def question4_choices(self):
        if self.treatment == 'budget':
            choices = ['115 tokens', '25 tokens', '15 tokens']
        else:
            choices = ['190 tokens', '100 tokens', '90 tokens']
        return choices

    def question1_error_message(self, value):
        if value != Constants.question1_answer:
            self.mistake1 = self.mistake1 + 1
            return 'Check your answer to question 1!'

    def question2_error_message(self, value):
        if value != Constants.question2_answer:
            self.mistake2 = self.mistake2 + 1
            return 'Check your answer to question 2!'

    def question3_error_message(self, value):
        if value != self.question3_answer:
            self.mistake3 = self.mistake3 + 1
            return 'Check your answer to question 3!'

    def question4_error_message(self, value):
        if value != self.question4_answer:
            self.mistake4 = self.mistake4 + 1
            return 'Check your answer to question 4!'

    def question5_error_message(self, value):
        if value != self.question5_answer:
            self.mistake5 = self.mistake5 + 1
            return 'Check your answer to question 5!'

    def question5_cost_error_message(self, value):
        if value != Constants.question5_cost_answer:
            self.mistake5 = self.mistake5 + 1
            return 'Check your answer to question 5!'

    def question6_error_message(self, value):
        if value != Constants.question6_answer:
            self.mistake6 = self.mistake6 + 1
            return 'Check your answer to question 6!'

    # forms for belief elicitation
    belief1 = models.IntegerField(label=
                                  "In your estimate, how many tokens will your"
                                  " co-participant use to buy lottery tickets in"
                                  " Stage 1?", min=0)

    def belief1_max(self):
        return self.endowment1
