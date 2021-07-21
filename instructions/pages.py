from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants
import time
import random

class InformedConsent(Page):
    """Informed consent, contact information and basic info on the study"""


class Instructions1(Page):
    """Description of the game: How to play and returns expected"""

    form_model = 'player'
    form_fields = ['prolific_id', 'prolific_id_check']

    def error_message(self, values):
        if values['prolific_id'] != values['prolific_id_check']:
            return 'Check again your ProlificID!'

class Instructions2(Page):
    """Description of the game: How to play and returns expected"""

class Instructions3(Page):
    """Description of the game: How to play and returns expected"""

class Instructions4(Page):
    """Description of the game: How to play and returns expected"""

class Instructions5(Page):
    """Description of the game: How to play and returns expected"""

class Instructions6(Page):
    """Description of the game: How to play and returns expected"""

class ControlQuestions(Page):
    """Description of the game: How to play and returns expected"""
    
    form_model = 'player'

    def get_form_fields(self):
        if self.player.treatment == 'cost':
            return ['question1', 'question2', 'question3', 'question4',
                    'question5_cost', 'question6_cost', 'question7']
        else:
            return ['question1', 'question2', 'question3', 'question4',
                    'question5', 'question6', 'question7']

class BeliefElicitation1(Page):
    """Belief elicition before group formation"""
    
    timeout_seconds = Constants.timeout_decision
    timer_text = 'Time left to take your decision:'
    form_model = 'player'
    form_fields = ['belief1']

    def before_next_page(self):
        self.participant.vars['belief1'] = self.player.belief1
        self.participant.vars['wait_page_arrival'] = time.time()
        if self.timeout_happened:
            self.player.belief1 = 500
            self.participant.vars['expiry'] = True


page_sequence = [InformedConsent, Instructions1, Instructions2, Instructions3,
                 Instructions4, Instructions5, Instructions6, ControlQuestions,
                 BeliefElicitation1]
