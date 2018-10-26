from django.core.management.base import BaseCommand, CommandError
# from accounts.models import Department,User,Gender
from accounts.models import *
import csv


class Command(BaseCommand):
    def handle(self,*args,**options):
        # with open('/home/user/sample_server/polls/sample_data.xls') as f:
        with open('/home/user/Subhash/DreamProject/accounts/department_data.xls') as f:
            data=csv.reader(f)
            for each in data:
                print each[0]
                Department.objects.create(name=each[0])