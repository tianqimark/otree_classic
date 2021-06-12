from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'even_gamble_practice'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    # Check_up questions
    # Page 1/2
    cq1_1 = models.PositiveIntegerField(
        choices = [[1,'40 points'],[2, '25 points']], widget=widgets.RadioSelect())

    cq1_2 = models.PositiveIntegerField(
        choices = [[1,'40 points'],[2, '25 points']], widget=widgets.RadioSelect())

    cq1_3 = models.PositiveIntegerField(
        choices = [[1,'Wining: 25 percent; Losing: 75 percent'],
                   [2,'Wining: 40 percent; Losing: 60 percent'],
                   [3,'Wining: 50 percent; Losing: 50 percent']], widget=widgets.RadioSelect())

    cq1_4 = models.PositiveIntegerField(
        choices = [[1,'Pressing the Up Arrow key (↑)'],
                   [2,'Pressing the Down Arrow key (↓)']], widget=widgets.RadioSelect())

    cq1_5 = models.PositiveIntegerField(
        choices = [[1,'Pressing the Up Arrow key (↑)'],
                   [2,'Pressing the Down Arrow key (↓)']], widget=widgets.RadioSelect())

    # Page 2/2
    cq2_1 = models.PositiveIntegerField(
        choices = [[1,'100 points'],[2, '35 points'],[3, '70 points'],[4, 'None of the above']], widget=widgets.RadioSelect())

    cq2_2 = models.PositiveIntegerField(
        choices = [[1,'170 points'],[2, '30 points'],[3, '135 points'],[4, '65 points']], widget=widgets.RadioSelect())

    cq2_3 = models.PositiveIntegerField(
        choices = [[1,'170 points'],[2, '30 points'],[3, '135 points'],[4, '65 points']], widget=widgets.RadioSelect())


    # Error Messages
    # 1/2
    def cq1_1_error_message(self, value):
        if value != 2:
            return "Your answer to the question 1 is wrong. The reward in event of winning is indicated by the plus signs (+). The side of display of reward and loss values on the screen varies from trial to trial."

    def cq1_2_error_message(self, value):
        if value != 1:
            return "Your answer to the question 2 is wrong. The loss in event of losing is indicated by the minus signs (–). The side of display of reward and loss values on the screen varies from trial to trial."

    def cq1_3_error_message(self, value):
        if value != 3:
            return "Your answer to the question 3 is wrong. For every gamble, there is an equal probability of winning and losing certain amounts of experiment points. The probabilities of winning and losing do not depend on the reward and loss."

    def cq1_4_error_message(self, value):
        if value != 1:
            return "Your answer to the question 4 is wrong. You can accept a gamble by pressing the Up Arrow key."

    def cq1_5_error_message(self, value):
        if value != 2:
            return "Your answer to the question 5 is wrong. You can reject a gamble by pressing the Down Arrow key."

    # 2/2
    def cq2_1_error_message(self, value):
        if value != 1:
            return "Your answer to the question 1 is wrong. If you chose to reject the gamble, you will not receive the outcome of the gamble and keep the fund that is initally given to you."

    def cq2_2_error_message(self, value):
        if value != 4:
            return "Your answer to the question 2 is wrong. In case of losing, the loss be deducted from your intial fund."

    def cq2_3_error_message(self, value):
        if value != 1:
            return "Your answer to the question 3 is wrong. In case of wining, the reward will be added to your intial fund."
