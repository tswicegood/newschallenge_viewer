# This script builds a list of all of the entries to the
# Knight Foundation News Challenge.
#
# The Knight Foundation recently opened their first 2012
# News Challenge up for submissions.  They're "leveraging
# existing technology" by using Tumblr to handle the submission
# process.  On the surface, this seems like an awesome idea.
# The problem though, is that they've taken structured data
# and trapped it inside a fancy <textarea> so there's no way
# to do analysis on the data in aggregate without first
# scrapping all of that data.
#
# That's where this script comes in.  It loads the NC site,
# pulls all of the data down, then inserts all of the entries
# into a database using Django's built-in ORM.
#
# Hopefully, the usefullness of this is obvious.  Trapping data
# inside blobs severely limits what can be done with the data.
# Organizations that are leading the charge for making journalism
# relevant to citizens should be leading the charge, not just
# using things off the shelf because they work.
#
# This code is meant to be used for learning purposes.  It can
# be viewed in annotated format using [Pycco].
#
# [Pycco]: http://fitzgen.github.com/pycco/
#
# ## The Code
#
# Start by importing a few modules that are required
import datetime
from django.conf import settings
from django.core.management.base import NoArgsCommand
import json
from pyquery import PyQuery as pq
import re
import requests
import time

from nc_viewer.models import Entry, Entrant

# This is the base URL that we are processing off of
BASE_URL = "http://newschallenge.tumblr.com"


# Below we grab the data data necessary off of the list pages to
# generate a list of all of the entries.
def find_all_entries():
    entry_urls = []

    doc = pq(url=BASE_URL)
    while True:
        entry_urls += [a.attrib["href"] for a in
                doc.find("div.posts div.contestPost a")]

        try:
            next_page = doc.find("div.pagination a")[0]
            next_url = "%s%s" % (BASE_URL, next_page.attrib["href"])
            doc = pq(url=next_url)

        # An `IndexError` will be thrown once there are no more pagination
        # urls to find.  We catch it here then continue on to the next step.
        except IndexError:
            break
    return entry_urls


ENTRY_REGEX = re.compile(
    u"1.\s*What do you propose to do\? \[20 words\](?P<what>.*)"
    u"2.\s*Is anyone doing something like this now and how is your project different\? \[30 words\](?P<who_else>.*)"
    u"3.\s*Describe the network with which you intend to build or work. \[50 words\](?P<description>.*)"
    u"4.\s*Why will it work\? \[100 words\](?P<why>.*)"
    u"5.\s*Who is working on it\? \[100 words\](?P<who>.*)"
    u"6.\s*What part of the project have you already built\? \[100 words\](?P<already_done>.*)"
    u"7.\s*How would you sustain the project after the funding expires\? \[50 words\](?P<sustain>.*)"
    u"Requested amount from Knight News Challenge:(?P<amount>.*)"
    u"Expected amount of time required to complete project:(?P<time>.*)"
    u"Total Project Cost:(?P<total_cost>.*)"
    u"Name:(?P<entrant_name>.*)"
    u"Twitter:(?P<twitter>.*)"
    u"Organization:(?P<organization>.*)"
    u"Country:(?P<country>.*)"
)


def scrap_page(url):
    # TODO: Use the API for everything
    doc = pq(url=url)
    split_url = url.split("/")
    post_id = split_url[-2]
    blog_id = split_url[2]
    api_url = "http://api.tumblr.com/v2/blog/%s/posts/text?id=%s&api_key=%s" % (
        blog_id, post_id, settings.TUMBLR_API_KEY)
    response = json.loads(requests.get(api_url).content)
    # TODO: There has to be a better way, but this work
    struct = time.strptime(response["response"]["posts"][0]["date"],
            "%Y-%m-%d %H:%M:%S %Z")
    date = datetime.datetime.fromtimestamp(time.mktime(struct))

    children = doc.find("div.single").children()
    title = response["response"]["posts"][0]["title"] or "N/A"
    children = children[2:-1]
    text = "".join([a.text_content() for a in children])
    entry = {
            "url": url,
            "created_on": date,
            "title": title,
            "data": {},
            "invalid": False,
    }
    result = ENTRY_REGEX.match(text)
    if not result:
        entry["invalid"] = True
        return entry
    for key, value in result.groupdict().items():
        entry["data"][key.strip()] = value.strip()
    return entry


def cmd():
    entry_urls = find_all_entries()
    print "Found %d entries" % len(entry_urls)
    for url in entry_urls:
        print "processing %s..." % url
        data = scrap_page(url)
        if not data["invalid"]:
            entrant_data = (data["data"].pop("entrant_name"), data["data"].pop("twitter"),
                    data["data"].pop("organization"), data["data"].pop("country"), )

            if "".join(entrant_data) != "":
                entrant, created = Entrant.objects.get_or_create(
                        name=entrant_data[0],
                        twitter=entrant_data[1],
                        organization=entrant_data[2],
                        country=entrant_data[3])
        if Entry.objects.filter(url=data["url"]).count() > 0:
            continue
        data_for_model = {
            "title": data["title"],
            "url": data["url"],
            "created_on": data["created_on"],
        }
        if data["invalid"]:
            data_for_model["invalid"] = True
        else:
            data_for_model.update(data["data"])
        Entry.objects.create(**data_for_model)


# Now we need to process each page and scrap the data from it.
class Command(NoArgsCommand):
    def handle_noargs(self, **options):
        cmd()
