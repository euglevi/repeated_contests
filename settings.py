from os import environ


SESSION_CONFIGS = [
    dict(
        name='experiment6543_alltreats',
        num_demo_participants=10,
        treatments = ['baseline', 'budget', 'productive', 'cost'],  
        app_sequence=['instructions', 'contest', 'final_questionnaire'],
    ),
    dict(
        name='experiment6543_base',
        num_demo_participants=10,
        treatments = ['baseline'],  
        app_sequence=['instructions', 'contest', 'final_questionnaire'],
    ),
    dict(
        name='experiment6543_prod',
        num_demo_participants=10,
        treatments = ['productive'],  
        app_sequence=['instructions', 'contest', 'final_questionnaire'],
    ),
    dict(
        name='experiment6543_cost',
        num_demo_participants=10,
        treatments = ['cost'],  
        app_sequence=['instructions', 'contest', 'final_questionnaire'],
    ),
    dict(
        name='experiment6543_budg',
        num_demo_participants=10,
        treatments = ['budget'],  
        app_sequence=['instructions', 'contest', 'final_questionnaire'],
    ),
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
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')


SECRET_KEY = 'gl+1nkgr29mi865!&1y_k3%cibuz6(&@gpt(iq3d-@f*=s&qxq'

INSTALLED_APPS = ['otree']
BROWSER_COMMAND = 'firefox'
