from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Instructions(Page):
    pass

class CheckPage1(Page):
    pass

class Results(Page):
    pass


page_sequence = [
Instructions,
# CheckPage1, 
Results]
