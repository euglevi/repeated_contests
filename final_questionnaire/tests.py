from otree.api import Currency as c, currency_range, Submission, SubmissionMustFail
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):

        if (
            self.participant.vars["expiry_group"] is False
            and self.participant.vars["expiry"] is False
            and self.participant.vars["group_formed"] is True
        ):
            yield SubmissionMustFail(
                pages.CRT, dict(ball="0.5", machine="25", lake="33")
            )
            yield pages.CRT, dict(ball=5, machine=5, lake=49)
            if self.player.participant.vars['treatment'] == 'baseline': 
                yield pages.Questionnaire, dict(
                    age=random.randrange(18, 70),
                    gender=random.randrange(1, 4),
                    country_birth="Kosovo",
                    education=1,
                    employment_status=random.randrange(1, 5),
                    experiments_economics=3,
                    economic_beliefs=random.randrange(1, 5),
                    political_beliefs=random.randrange(1, 5),
                    fairness1=random.randrange(1, 5),
                    decision2=True,
                    decision_how2="",
                    fairness2=random.randrange(1, 5),
                    comments="",
                )
            elif self.player.participant.vars['treatment'] in ['cost', 'productive']:
                yield pages.Questionnaire, dict(
                    age=random.randrange(18, 70),
                    gender=random.randrange(1, 4),
                    country_birth="Kosovo",
                    education=1,
                    employment_status=random.randrange(1, 5),
                    experiments_economics=3,
                    economic_beliefs=random.randrange(1, 5),
                    political_beliefs=random.randrange(1, 5),
                    fairness1=random.randrange(1, 5),
                    decision1a=True,
                    decision_how1a="",
                    decision2=True,
                    decision_how2="",
                    fairness2=random.randrange(1, 5),
                    comments="",
                )
            elif self.player.participant.vars['treatment'] == 'budget':
                yield pages.Questionnaire, dict(
                    age=random.randrange(18, 70),
                    gender=random.randrange(1, 4),
                    country_birth="Kosovo",
                    education=1,
                    employment_status=random.randrange(1, 5),
                    experiments_economics=3,
                    economic_beliefs=random.randrange(1, 5),
                    political_beliefs=random.randrange(1, 5),
                    fairness1=random.randrange(1, 5),
                    decision1b=True,
                    decision_how1b="",
                    decision2=True,
                    decision_how2="",
                    fairness2=random.randrange(1, 5),
                    comments="",
                )

        yield Submission(pages.Completion, check_html=False)
