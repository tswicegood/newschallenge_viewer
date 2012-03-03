from celery.task import task
from .management.commands.scraper import cmd


@task
def grab_entries():
    cmd()
