from otree.api import Currency as c, currency_range, SubmissionMustFail, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):

        yield pages.InformedConsent
        yield SubmissionMustFail(pages.Instructions1,dict(prolific_id="123", prolific_id_check="234"))
        yield pages.Instructions1, dict(prolific_id="123",prolific_id_check="123")
        yield pages.Instructions2
        yield pages.Instructions3
        yield pages.Instructions4
        yield pages.Instructions5
        yield pages.Instructions6

        if self.participant.vars['treatment']=='baseline':
            yield pages.ControlQuestions, dict(question1=False, question2='10/30', 
                                               question3='90 tokens',
                                               question4='190 tokens',
                                               question5='1 ticket',
                                               question6=True)
        elif self.participant.vars['treatment']=='budget':
            yield pages.ControlQuestions, dict(question1=False, question2='10/30', 
                                               question3='15 tokens',
                                               question4='115 tokens',
                                               question5='1 ticket',
                                               question6=True)
        elif self.participant.vars['treatment']=='cost':
            yield pages.ControlQuestions, dict(question1=False, question2='10/30', 
                                               question3='90 tokens',
                                               question4='190 tokens',
                                               question5_cost='1 token',
                                               question6=True)
        elif self.participant.vars['treatment']=='productive':
            yield pages.ControlQuestions, dict(question1=False, question2='10/30', 
                                               question3='90 tokens',
                                               question4='190 tokens',
                                               question5='4 tickets',
                                               question6=True)

        
        if self.participant.vars['treatment']=='budget':
            yield pages.BeliefElicitation1, dict(belief1=random.randint(0,25))
        elif self.participant.id_in_session in [11, 49, 63]:
            yield Submission(pages.BeliefElicitation1, timeout_happened=True)
        else:
            yield pages.BeliefElicitation1, dict(belief1=random.randint(0,100))



