import time

#use to test if the database connection is available
from django.db import connections
#Operational error that django throws if the database is not available
from django.db.utils import OperationalError
#import base command the classs that we build on in order to create
# the custome command
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    """Django command to pause execution until database is available"""

    #handle function of what is run whenever we run this management Command
    def handle(self, *args, **options):
        #how is this different than using print
        self.stdout.write('waiting for database....')
        db_conn = None
        while not db_conn:
            try:
                db_conn = connections['default']
            except OperationalError:
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database available!'))
