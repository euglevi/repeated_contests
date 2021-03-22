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
    name_in_url = 'f3'
    players_per_group = None
    num_rounds = 1
    country_list = ['Afghanistan',
                    'Albania',
                    'Algeria',
                    'Andorra',
                    'Angola',
                    'Antigua & Deps',
                    'Argentina',
                    'Armenia',
                    'Australia',
                    'Austria',
                    'Azerbaijan',
                    'Bahamas',
                    'Bahrain',
                    'Bangladesh',
                    'Barbados',
                    'Belarus',
                    'Belgium',
                    'Belize',
                    'Benin',
                    'Bhutan',
                    'Bolivia',
                    'Bosnia Herzegovina',
                    'Botswana',
                    'Brazil',
                    'Brunei',
                    'Bulgaria',
                    'Burkina',
                    'Burundi',
                    'Cambodia',
                    'Cameroon',
                    'Canada',
                    'Cape Verde',
                    'Central African Rep',
                    'Chad',
                    'Chile',
                    'China',
                    'Colombia',
                    'Comoros',
                    'Congo',
                    'Congo {Democratic Rep}',
                    'Costa Rica',
                    'Croatia',
                    'Cuba',
                    'Cyprus',
                    'Czech Republic',
                    'Denmark',
                    'Djibouti',
                    'Dominica',
                    'Dominican Republic',
                    'East Timor',
                    'Ecuador',
                    'Egypt',
                    'El Salvador',
                    'Equatorial Guinea',
                    'Eritrea',
                    'Estonia',
                    'Ethiopia',
                    'Fiji',
                    'Finland',
                    'France',
                    'Gabon',
                    'Gambia',
                    'Georgia',
                    'Germany',
                    'Ghana',
                    'Greece',
                    'Grenada',
                    'Guatemala',
                    'Guinea',
                    'Guinea-Bissau',
                    'Guyana',
                    'Haiti',
                    'Honduras',
                    'Hungary',
                    'Iceland',
                    'India',
                    'Indonesia',
                    'Iran',
                    'Iraq',
                    'Ireland {Republic}',
                    'Israel',
                    'Italy',
                    'Ivory Coast',
                    'Jamaica',
                    'Japan',
                    'Jordan',
                    'Kazakhstan',
                    'Kenya',
                    'Kiribati',
                    'Korea North',
                    'Korea South',
                    'Kosovo',
                    'Kuwait',
                    'Kyrgyzstan',
                    'Laos',
                    'Latvia',
                    'Lebanon',
                    'Lesotho',
                    'Liberia',
                    'Libya',
                    'Liechtenstein',
                    'Lithuania',
                    'Luxembourg',
                    'Macedonia',
                    'Madagascar',
                    'Malawi',
                    'Malaysia',
                    'Maldives',
                    'Mali',
                    'Malta',
                    'Marshall Islands',
                    'Mauritania',
                    'Mauritius',
                    'Mexico',
                    'Micronesia',
                    'Moldova',
                    'Monaco',
                    'Mongolia',
                    'Montenegro',
                    'Morocco',
                    'Mozambique',
                    'Myanmar, {Burma}',
                    'Namibia',
                    'Nauru',
                    'Nepal',
                    'Netherlands',
                    'New Zealand',
                    'Nicaragua',
                    'Niger',
                    'Nigeria',
                    'Norway',
                    'Oman',
                    'Pakistan',
                    'Palau',
                    'Panama',
                    'Papua New Guinea',
                    'Paraguay',
                    'Peru',
                    'Philippines',
                    'Poland',
                    'Portugal',
                    'Qatar',
                    'Romania',
                    'Russian Federation',
                    'Rwanda',
                    'St Kitts & Nevis',
                    'St Lucia',
                    'Saint Vincent & the Grenadines',
                    'Samoa',
                    'San Marino',
                    'Sao Tome & Principe',
                    'Saudi Arabia',
                    'Senegal',
                    'Serbia',
                    'Seychelles',
                    'Sierra Leone',
                    'Singapore',
                    'Slovakia',
                    'Slovenia',
                    'Solomon Islands',
                    'Somalia',
                    'South Africa',
                    'South Sudan',
                    'Spain',
                    'Sri Lanka',
                    'Sudan',
                    'Suriname',
                    'Swaziland',
                    'Sweden',
                    'Switzerland',
                    'Syria',
                    'Taiwan',
                    'Tajikistan',
                    'Tanzania',
                    'Thailand',
                    'Togo',
                    'Tonga',
                    'Trinidad & Tobago',
                    'Tunisia',
                    'Turkey',
                    'Turkmenistan',
                    'Tuvalu',
                    'Uganda',
                    'Ukraine',
                    'United Arab Emirates',
                    'United Kingdom',
                    'United States',
                    'Uruguay',
                    'Uzbekistan',
                    'Vanuatu',
                    'Vatican City',
                    'Venezuela',
                    'Vietnam',
                    'Yemen',
                    'Zambia',
                    'Zimbabwe']

    ball_answer = 5
    machine_answer = 5
    lake_answer = 47
    bonus = 50

    exchange_rate = 300


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    #CRT
    ball = models.IntegerField(label="1) A bat and a ball cost $1.10. The bat \
                               costs $1.00 more than the ball. How much does \
                               the ball cost?", min=0, max=1000)
    machine = models.IntegerField(label="2) If it takes 5 machines 5 minutes to \
                                  make 5 widgets, how long would it take 100 \
                                  machines to make 100 widgets?", min=0,
                                  max=1000)
    lake = models.IntegerField(label="3) In a lake, there is a patch of lily \
                               pads. Every day, the patch of lily pads doubles \
                               in size. If it takes 48 days for the patch to \
                               cover the entire lake, how long would it take \
                               for the patch to cover half the lake?", min=0,
                               max=1000)
    bonus_ball = models.IntegerField()
    bonus_machine = models.IntegerField()
    bonus_lake = models.IntegerField()
    bonus3 = models.IntegerField()
    final_earnings = models.FloatField()

    # def ball_error_message(self, value):
        # if "," or "." in value:
            # return "Answers must be in cents!"

    def set_bonus(self):
        self.bonus_ball = Constants.bonus if self.ball == Constants.ball_answer \
            else 0
        self.bonus_machine = Constants.bonus if self.machine == Constants.machine_answer \
            else 0
        self.bonus_lake = Constants.bonus if self.lake == Constants.lake_answer \
            else 0
        self.bonus3 = self.bonus_ball + self.bonus_machine + self.bonus_lake
        self.participant.vars['total_earnings'] = self.participant.vars['bonus1'] \
            + self.participant.vars['bonus2'] + self.bonus3 + \
            self.participant.vars['earnings2']
        self.final_earnings = round(self.participant.vars['total_earnings']/
                                    Constants.exchange_rate, 2)


    # final questionnaire
    age = models.IntegerField(label="How old are you?", min=18, max=90)
    gender = models.IntegerField(choices=[[1, 'Male'], [2, 'Female'], [3, 'Self-identify/other'], [4, 'Prefer not to say'],
                                          ], widget=widgets.RadioSelect,
                                 label="Gender")
    education = models.IntegerField(
        choices=[[1, 'Below high school'], [2, 'High school'], [3, 'Some undergraduate university training'],
                 [4, 'Undergraduate degree'], [5, 'Masters degree'], [6, 'Doctorate or Professional qualification'],
                 [7, 'Prefer not to say'], ], label="Which is your level of education?")
    employment_status = models.IntegerField(
        choices=[[1, 'Employed'], [2, 'Unemployed'], [3, 'Retired'], [4, 'Student'], [5, 'Not looking for a job'],
                 [6, 'Prefer not to say'], ],
        label="What is your current employment status?"
    )
    country_birth = models.StringField(choices=Constants.country_list, label="In which country is your hometown?")
    experiments_economics = models.IntegerField(
        label="How many economics experiments have you participated in before this one?", min=0, max=1000)
    political_beliefs = models.IntegerField(
        choices=[[1, "Very left"], [2, "Left"], [3, "Neither left nor right"], [4, "Right"], [5, "Very right"]],
        label="How would you describe your political beliefs?",
        widget=widgets.RadioSelectHorizontal
    )
    economic_beliefs = models.IntegerField(
        choices=[[1, "Very left"], [2, "Left"], [3, "Neither left nor right"], [4, "Right"], [5, "Very right"]],
        label="How would you describe your economic beliefs?",
        widget=widgets.RadioSelectHorizontal
    )



    fairness1 = models.IntegerField(choices=[[1, "Very unfair"],[2, "Somewhat unfair"],[3, "Neither fair nor unfair"],[4,"Somewhat fair"],[5,"Very fair"]],widget=widgets.RadioSelectHorizontal, label="In the experiment, did you consider fair the way in which outcomes were decided in Stage 1?")
    decision1 = models.BooleanField(choices=[[True, "Yes"],[False,"No"]],widget=widgets.RadioSelect,label="Did the possibility of different endowments in Stage 2 affect your decision in Stage 1?")
    decision_how1 = models.LongStringField(label="If yes, how?", blank=True)


    fairness2 = models.IntegerField(choices=[[1, "Very unfair"],[2, "Somewhat unfair"],[3, "Neither fair nor unfair"],[4,"Somewhat fair"],[5,"Very fair"]],widget=widgets.RadioSelectHorizontal, label="In the experiment, did you consider fair the way in which outcomes were decided in Stage 2?")
    decision2 = models.BooleanField(choices=[[True, "Yes"],[False,"No"]],widget=widgets.RadioSelect,label="Did the possibility of different endowments in Stage 2 affect your decision in Stage 2?")
    decision_how2 = models.LongStringField(label="If yes, how?", blank=True)

    comments = models.LongStringField(label="Any other comment?", blank=True)
