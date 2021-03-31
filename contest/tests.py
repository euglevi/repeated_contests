from otree.api import Currency as c, currency_range, SubmissionMustFail, Submission
from . import pages
from ._builtin import Bot
from .models import Constants
import random


class PlayerBot(Bot):
    def play_round(self):

        if self.participant.id_in_session in [5, 6, 24, 41, 52, 34, 66]:
            yield Submission(pages.Stage1, timeout_happened=True)
        elif self.participant.vars['expiry'] is False and \
        self.participant.vars['group_formed'] is True:
            yield pages.Stage1, dict(tokens1=random.randint(0,self.player.endowment1))

        if self.group.expiry_group==False and self.participant.vars['expiry'] is False \
                and self.participant.vars['group_formed'] is True:
            yield pages.Results1
            if self.participant.id_in_session in [9, 29, 44, 81]:
                yield Submission(pages.BeliefElicitation2, timeout_happened=True)
            elif self.participant.vars['treatment']=='cost' and \
                self.player.id_in_group==self.group.winner1: 
                yield pages.BeliefElicitation2, dict(belief2=random.randint(
                    0,self.player.other_earnings1)//4*4)
            else:
                yield pages.BeliefElicitation2, dict(belief2=
                                                     random.randint
                                                     (0,self.player.other_earnings1))
        else:
            pass

        if self.group.expiry_group==False and self.participant.vars['expiry'] is False \
                and self.participant.vars['group_formed'] is True:
            if self.participant.id_in_session in [2, 4, 31, 78]:
                yield Submission(pages.Stage2, timeout_happened=True)
            elif self.participant.vars['treatment']=='cost' and \
                self.player.id_in_group!=self.group.winner1: 
                yield pages.Stage2, dict(tokens2=random.randint(
                    0,self.player.earnings1)//4*4)
            else:
                yield pages.Stage2, dict(tokens2=random.randint(0,self.player.earnings1))
        else:
            pass

        if self.group.expiry_group==False and self.participant.vars['expiry'] is False \
                and self.participant.vars['group_formed'] is True:
            yield pages.Results2


