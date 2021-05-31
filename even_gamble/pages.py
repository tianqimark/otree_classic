from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, set_time, gamble_generator
import numpy as np
import pandas as pd
import time

class InitialPage(Page):
    def is_displayed(self):
        return self.round_number == 1

class FixationPage(Page):
    # timeout_seconds = 0.5
    # This page should stay for 1 second in real experiment

    timeout_seconds = 1

    def before_next_page(self):
        self.player.pydectime = set_time() # here we set the start of the dectime in unix seconds


confirm_time = 500 # confirmation time shown in ms
# Currently the display of the confirmation signs is realised by using the setTimeout function
# in the JavaScript. However, this seems to affect the time recording.
# It is more reliable to use an "afterpage" aswas don in the first study.

class DecisionPage(Page):

    form_model = 'player'
    form_fields = ['accept', 'jsdectime_start', 'jsdectime_end']

    def vars_for_template(self):

        start = 1
        end = 5
        seed = 666888

        trial_table =  gamble_generator(start = start, end = end, seed = seed)

        gain = int(trial_table['gain'][self.round_number - 1])
        loss = int(trial_table['loss'][self.round_number - 1])
        display = trial_table['display'][self.round_number - 1]

        # Recording information about the trial
        self.player.gain = gain
        self.player.loss = loss
        self.player.display = display

        return {
            'gain': "+" + str(gain),
            'loss': "–" + str(loss),

            'confirm_time': confirm_time,

            # 'display': display,
        }

    def before_next_page(self):
        # Python Method of dectime collection:
        self.player.pydectime = set_time() - self.player.pydectime - (confirm_time /1000)
        # JavaScript Method of dectime collection:
        self.player.jsdectime = (self.player.jsdectime_end - self.player.jsdectime_start) / 1000

        if self.round_number in rest_round:
            self.player.pyresttime = set_time()
        else:
            pass

# Specify information about the resting page:
rest_round = [3] # for testing during development
# rest_round = [50, 100, 150] # In actual experiment rest after trial 50, 100 and 150
rest_limit = 300 # seconds

class RestPage(Page):
    timeout_seconds = rest_limit
    timer_text = 'Time remaining for this break:'

    def is_displayed(self):
        rest = rest_round

        if self.round_number in rest:
            return True
        else:
            return False

    def vars_for_template(self):
        rest_minites = rest_limit / 60

        if rest_minites.is_integer():
            rest_minites = int(rest_minites)

        trials_gone = self.round_number
        trials_left = Constants.num_rounds - self.round_number

        return {
            'rest_minites': rest_minites,

            'trials_gone': trials_gone,
            'trials_left': trials_left
        }

    def before_next_page(self):
        self.player.pyresttime = set_time() - self.player.pyresttime


class FinishPage(Page):

    def is_displayed(self):
        return self.round_number == Constants.num_rounds

    def vars_for_template(self):

        return {
            'prolificurl': self.session.config['prolificurl']
        }


page_sequence = [
InitialPage,
FixationPage,
DecisionPage,
RestPage,
FinishPage
]
