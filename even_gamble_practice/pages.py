from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass

class CheckPage1(Page):
    form_model = 'player'
    form_fields = ['cq1_1', 'cq1_2', 'cq1_3', 'cq1_4', 'cq1_5']

class CheckPage2(Page):
    form_model = 'player'
    form_fields = ['cq2_1', 'cq2_2', 'cq2_3']

class Results(Page):
    pass


page_sequence = [
Instructions,
CheckPage1,
CheckPage2,
Results]
