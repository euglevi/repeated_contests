from otree.api import Currency as c, currency_range, SubmissionMustFail, Submission, expect
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
        yield pages.Instructions2_Examples
        yield pages.Instructions3

        if self.participant.vars['treatment']=='ineq' and self.player.cq_20 is True:
            yield pages.ControlQuestions, dict(question1=False,question2=True,question3=False,question4a=30,question4b=25)
        elif self.participant.vars['treatment']=='ineq' and self.player.cq_20 is False:
            yield pages.ControlQuestions, dict(question1=False,question2=True,question3=False,question4a=120,question4b=100)
        elif self.participant.vars['treatment']=='poor':
            yield pages.ControlQuestions, dict(question1=False,question2=True,question3=True,question4a=30,question4b=25)
        elif self.participant.vars['treatment']=='rich':
            yield pages.ControlQuestions, dict(question1=False,question2=True,question3=True,question4a=120,question4b=100)


        if self.participant.vars['treatment']=='ineq':
            yield pages.BeliefElicitation1, dict(belief_poor=random.randint(0,20),belief_rich=random.randint(0,80))
        elif self.participant.vars['treatment']=='poor':
            yield pages.BeliefElicitation1, dict(belief_poor=random.randint(0,20))
        elif self.participant.vars['treatment']=='rich':
            yield pages.BeliefElicitation1, dict(belief_rich=random.randint(0,80))


