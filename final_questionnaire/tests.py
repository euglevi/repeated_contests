from otree.api import Currency as c, currency_range, Submission, SubmissionMustFail
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):

    def play_round(self):
        
        if self.participant.vars['expiry']<2 and self.participant.vars['treatment']=='ineq':
            yield pages.Questionnaire, dict(age=random.randrange(18, 70), gender=random.randrange(1, 4), country_birth="Kosovo", education=1,
                                            employment_status=random.randrange(1, 5),
                                            experiments_economics=3, economic_beliefs=random.randrange(1, 5),
                                            political_beliefs=random.randrange(1, 5), decision=True, decision_how="", fairness=random.randrange(1,5), comments="")
        elif self.participant.vars['expiry']<2:
            yield pages.Questionnaire, dict(age=random.randrange(18, 70), gender=random.randrange(1, 4), country_birth="Kosovo", education=1,
                                            employment_status=random.randrange(1, 5),
                                            experiments_economics=3, economic_beliefs=random.randrange(1, 5),
                                            political_beliefs=random.randrange(1, 5), comments="")
        else:
            pass

        yield Submission(pages.Completion, check_html=False)
