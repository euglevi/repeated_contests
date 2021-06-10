from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class FormingGroups(WaitPage):
    """Forming groups and sending those who wait too long at the end of the
    experiment"""
    template_name = "contest/FormingGroups.html"

    group_by_arrival_time = True

    def is_displayed(self):
        return self.participant.vars['expiry'] == False

class Stage1(Page):

    timeout_seconds = Constants.timeout_decision
    timer_text = 'Time left to take your decision:'
    form_model = 'player'
    form_fields = ['tokens1']

    def is_displayed(self):
        return self.participant.vars['group_formed'] == True and \
                self.participant.vars['expiry'] == False

    def before_next_page(self):
        if self.timeout_happened:
            self.player.expiry = True
            self.group.set_expiry()

class Results1WaitPage(WaitPage):

    after_all_players_arrive = 'set_earnings1'
    template_name = "contest/ResultsWaitPage.html"

    def is_displayed(self):
        return self.participant.vars['group_formed'] == True and \
                    self.group.expiry_group is False and \
                    self.participant.vars['expiry'] == False

class Results1(Page):

    timeout_seconds = Constants.timeout_results
    timer_text = 'Time left on this screen:'

    def vars_for_template(self):
        tickets_other = self.group.total_tickets1 - self.player.tokens1
        chance = round(self.player.tokens1*100/self.group.total_tickets1, 2) \
            if self.group.total_tickets1 != 0 else 0
        chance_other = round((self.group.total_tickets1 - 
                        self.player.tokens1)*100/self.group.total_tickets1, 2) \
            if self.group.total_tickets1 != 0 else 0
        return dict(tickets_other=tickets_other,
                    chance=chance, chance_other=chance_other,)

    def is_displayed(self):
        return self.participant.vars['group_formed'] == True and \
                    self.group.expiry_group is False and \
                    self.participant.vars['expiry'] == False

    def before_next_page(self):
        self.player.record_other_earnings1()

class BeliefElicitation2(Page):

    timeout_seconds = Constants.timeout_decision
    timer_text = 'Time left to take your decision:'
    form_model = 'player'
    form_fields = ['belief2']
    
    def is_displayed(self):
        return self.participant.vars['group_formed'] == True and \
                    self.group.expiry_group is False and \
                    self.participant.vars['expiry'] == False

    def before_next_page(self):
        if self.timeout_happened:
            self.player.belief2 = 500
            self.player.expiry = True
            self.group.set_expiry()

class Belief2WaitPage(WaitPage):

    template_name = "contest/ResultsWaitPage.html"

    def is_displayed(self):
        return self.participant.vars['group_formed'] == True and \
                    self.group.expiry_group is False and \
                    self.participant.vars['expiry'] == False


class Stage2(Page):

    timeout_seconds = Constants.timeout_decision
    timer_text = 'Time left to take your decision:'
    form_model = 'player'
    form_fields = ['tokens2']

    def is_displayed(self):
        return self.participant.vars['group_formed'] == True and \
                    self.group.expiry_group is False and \
                    self.participant.vars['expiry'] == False

    def before_next_page(self):
        if self.timeout_happened:
            self.player.expiry = True
            self.group.set_expiry()

class Results2WaitPage(WaitPage):

    after_all_players_arrive = 'set_earnings2'
    template_name = "contest/ResultsWaitPage.html"

    def is_displayed(self):
        return self.participant.vars['group_formed'] == True and \
                    self.group.expiry_group is False and \
                    self.participant.vars['expiry'] == False

class Results2(Page):

    timeout_seconds = Constants.timeout_results
    timer_text = 'Time left on this screen:'

    def vars_for_template(self):
        tickets_other = self.group.total_tickets2 - self.player.tickets2
        chance = round(self.player.tickets2*100/self.group.total_tickets2, 2) \
            if self.group.total_tickets2 != 0 else 0
        chance_other = round((self.group.total_tickets2 - 
                        self.player.tickets2)*100/self.group.total_tickets2, 2) \
            if self.group.total_tickets2 != 0 else 0
        return dict(tickets_other=tickets_other,
                    chance=chance, chance_other=chance_other,)

    def is_displayed(self):
        return self.participant.vars['group_formed'] == True and \
            self.group.expiry_group is False and \
            self.participant.vars['expiry'] == False

    def before_next_page(self):
        self.player.set_earnings_beliefs()
        self.participant.vars['bonus1'] = self.player.bonus1
        self.participant.vars['bonus2'] = self.player.bonus2
        self.participant.vars['earnings2'] = self.player.earnings2

page_sequence = [FormingGroups, Stage1, Results1WaitPage, Results1,
                 BeliefElicitation2, Belief2WaitPage, Stage2, Results2WaitPage,
                 Results2]
