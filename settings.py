from os import environ

SESSION_CONFIGS = [

    dict(
        name = 'ECI_survey',
        display_name = 'Emotional and Cognitive Ability Survey',
        num_demo_participants = 5,
        app_sequence = ['ECI_survey'],
    ),

    dict(
        name = 'REItest',
        display_name = 'CA Tests',
        num_demo_participants = 1,
        app_sequence = ['REItest', 'BDMauction', 'choice_practice', 'cognitivenoise'],
        endowment = 25,
        exchange = 5,
        prolificurl = 'http://www.google.com',
    ),

    dict(
        name = 'BDMauction',
        display_name = 'Preference Elicitation in Cognitive Noise Study',
        num_demo_participants = 1,
        # app_sequence = ['BDMauction', 'choice_practice', 'cognitivenoise'],
        app_sequence = ['BDMauction', 'cognitivenoise'],
    ),

    dict(
        name = 'choice_practice',
        display_name = 'Practice Session for the Binary Choices',
        num_demo_participants = 1,
        app_sequence = ['choice_practice', 'cognitivenoise'],
    ),

    dict(
        name = 'cognitivenoise',
        display_name = 'Decision Task in Cognitive Noise Study',
        num_demo_participants = 1,
        app_sequence = ['cognitivenoise'],
    )


    # dict(
    #    name='public_goods',
    #    display_name="Public Goods",
    #    num_demo_participants=3,
    #    app_sequence=['public_goods', 'payment_info']
    # ),

]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'GBP'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

# It looks like "DEMO_PAGE_INTRO_HTML" used to be named as "DEMO_PAGE_INTRO_TEXT"
DEMO_PAGE_INTRO_HTML = """
<ul>
    <li>
        <a href="https://github.com/oTree-org/otree" target="_blank">
            oTree on GitHub
        </a>.
    </li>
    <li>
        <a href="http://www.otree.org/" target="_blank">
            oTree homepage
        </a>.
    </li>
</ul>
<p>
    Here are various games implemented with oTree. These games are all open
    source, and you can modify them as you wish.
</p>
"""

""

# don't share this with anybody.
SECRET_KEY = 'mvw&oo=*hxo!s9qc6(u7eni9d6&a8$dx(gaz!t20ynj8!v%^8a'

# if an app is included in SESSION_CONFIGS, you don't need to list it here
INSTALLED_APPS = ['otree']
