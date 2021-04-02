from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

class CRT(Page):

    form_model = 'player'
    form_fields = ['ball', 'machine', 'lake']
    timeout_seconds = Constants.timeout_decision
    timer_text = 'Time left to take your decision:'

    def is_displayed(self):
        return self.participant.vars['group_formed'] == True and \
                    self.participant.vars['expiry_group'] is False \
                    and self.participant.vars['expiry'] is False

    def before_next_page(self):
        self.player.set_bonus()
        if self.timeout_happened(self):
            self.player.timeout_CRT = True

class Questionnaire(Page):

    form_model = 'player'
    form_fields = ['age', 'gender', 'country_birth', 'education',
                   'employment_status', 'political_beliefs',
                   'economic_beliefs', 'fairness1', 'decision1',
                   'decision_how1' ,'fairness2', 'decision2', 'decision_how2',
                   'experiments_economics', 'comments']

    def is_displayed(self):
        return self.participant.vars['group_formed'] == True and \
                    self.participant.vars['expiry_group'] is False \
                    and self.participant.vars['expiry'] is False


class Completion(Page):

    def vars_for_template(self):
        completion_link = "https://app.prolific.co/submissions/complete?cc=85BC7136"
        return dict(completion_link=completion_link, )


page_sequence = [CRT, Questionnaire, Completion]
