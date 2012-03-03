from django.db import models


class Entrant(models.Model):
    name = models.TextField()
    organization = models.TextField()
    twitter = models.TextField()
    country = models.TextField()


class Entry(models.Model):
    url = models.URLField()
    invalid = models.BooleanField(default=False)
    title = models.TextField(default="")
    what = models.TextField(default="")
    who_else = models.TextField(default="")
    description = models.TextField(default="")
    why = models.TextField(default="")
    who = models.TextField(default="")
    already_done = models.TextField(default="")
    sustain = models.TextField(default="")

    amount = models.TextField(default="")  # Maybe they're asking for lots?
    time = models.TextField(default="")
    total_cost = models.TextField(default="")

    # Allow to be empty, because some people can't fill out a form
    entrant = models.ForeignKey(Entrant, null=True, blank=True)


{'data': {'Describe the network with which you intend to build or work. [50 words]': [u'Kaliki is the audio newspaper network. When a newspaper publishes a new issue, Kaliki will provide the audio version of the top 10 articles in < 2 hrs. The audio version will be available for consumption on the newspaper\u2019s website, on all mobile devices, and within connected vehicles .'],
          'How would you sustain the project after the funding expires? [50 words]': ['By partnering with the Knight Foundation, we want to pilot the Kaliki platform with select newspapers in the US market. After the funding expires, we will enter into a business relationship with each individual newspaper who deems the pilot as a success.'],
          'Is anyone doing somethinmag like this now and how is your project different? [30 words]': ['Yes, Typecaster.net is doing something similar, however, our platform is different because we have relationships with automakers to enable a seamless listening experience in vehicles.'],
          'What do you propose to do? [20 words]': [u'Create the end-to-end platform that enables busy people to listen to newspaper articles \u2014 especially during their morning commute.'],
          'What part of the project have you already built? [100 words]': [u'The audio network consists of two major components: the server infrastructure and the various mobile audio players. So far we have built 50% of the server infrastructure and 60% of the mobile audio players. Video Demo:\xa0http://www.kaliki.com/videoDemo/sfChron_nov_2011.mp4'],
          'Who is working on it? [100 words]': ['Kaliki is being actively developed by BT Software and Research Inc, located in El Cajon, CA. BT Software was founded in 2009, and consists of experts in streaming media and mobile development.'],
          'Why will it work? [100 words]': [u'Kaliki will work because we have already tested pilot of the platform in the Indian market in 2011 with one of it\u2019s largest print publishers. The goal of the pilot was to have 50k downloads of an \u201caudio news player\u201d mobile app in 12 months, and we accomplished 100k downloads in 4 months. We have easily proven the case that consumers want utilize their ears to read the newspaper, because it frees them to multitask and do other things.']},
 'details': {'amount': u'$350,000Expected amount of time required to complete project: 9 monthsTotal Project Cost: $700,000',
             'time': None,
             'total_cost': None},
 'entrant': {'country': None,
             'name': u'Bruce HopkinsTwitter: @kaliki_audioOrganization: BT Software and\xa0Research\xa0Inc.Country: USA',
             'organization': None,
             'twitter': None},
 'title': 'The Audio Newspaper Network for Mobile Devices and Connected Vehicles: Kaliki'}
