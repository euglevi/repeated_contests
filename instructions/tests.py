from otree.api import Currency as c, currency_range, SubmissionMustFail, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):

        yield pages.InformedConsent
        yield SubmissionMustFail(
            pages.Instructions1, dict(prolific_id="123", prolific_id_check="234")
        )
        yield pages.Instructions1, dict(prolific_id="123", prolific_id_check="123")
        yield pages.Instructions2
        yield pages.Instructions3
        yield pages.Instructions4
        yield pages.Instructions5
        yield pages.Instructions6

        if self.participant.vars["treatment"] == "baseline":
            yield pages.ControlQuestions, dict(
                question1=False,
                question2="10/30",
                question3="90 tokens",
                question4="100 tokens",
                question5="1 ticket",
                question6="1 ticket",
                question7="The sum of your earnings from Stage 1 and Stage 2",
            )
        elif self.participant.vars["treatment"] == "budget":
            yield pages.ControlQuestions, dict(
                question1=False,
                question2="10/30",
                question3="90 tokens",
                question4="25 tokens",
                question5="1 ticket",
                question6="1 ticket",
                question7="The sum of your earnings from Stage 1 and Stage 2",
            )
        elif self.participant.vars["treatment"] == "cost":
            yield pages.ControlQuestions, dict(
                question1=False,
                question2="10/30",
                question3="90 tokens",
                question4="100 tokens",
                question5_cost="1 token",
                question6_cost="4 tokens",
                question7="The sum of your earnings from Stage 1 and Stage 2",
            )
        elif self.participant.vars["treatment"] == "productive":
            yield pages.ControlQuestions, dict(
                question1=False,
                question2="10/30",
                question3="90 tokens",
                question4="100 tokens",
                question5="4 tickets",
                question6="1 ticket",
                question7="The sum of your earnings from Stage 1 and Stage 2",
            )

        yield pages.BeliefElicitation1, dict(belief1=random.randint(0, 100))
