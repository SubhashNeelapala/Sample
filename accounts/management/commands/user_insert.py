from django.core.management.base import BaseCommand, CommandError
# from accounts.models import Department,User,Gender
from accounts.models import *
import csv

class Command(BaseCommand):
    def handle(self,*args,**options):
        with open('/home/user/Subhash/DreamProject/accounts/user_data.xls')as f:
            data=csv.reader(f)
            for each in data:
                print each
                kwargs={
                    "username":each[0],
                    "first_name":each[1],
                    "last_name":each[2],
                    "mobile_number":each[5],
                    "age":each[4],
                    "gender":Gender.objects.get(name=each[6]),
                    "department":Department.objects.get(name=each[7]),
                    "email":each[3]
                }
                User.objects.create(**kwargs)