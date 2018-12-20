from django.core.management.base import BaseCommand, CommandError
import random 
import string 
import sys
import datetime
from random import randint
from beneficiary.models import Patient
from accounts.models import Worker,User


GENDER=['Male','Female']

GUARDIAN_CHOICES = ('D/O','S/O','W/O')

TITLE_CHOICE =('Mr','Ms')
BLOOD_GROUP= ('AB-','AB+','A+','A-','B+','B-','O+','O-')
MARITIAL_STATUS=('Yes','No')
RELIGION=('Hindu','Muslim','Christian')
OCCUPATION=('Doctor','Farmer','Labour')
EDUCATION=('MBA','B.Tech','10th','INTER','Not Known')
NATIONALITY =('Indian','American')
MOBILE_STARTS=(6,7,8,9)
DISTRICT_CHOICE=(505,520,521)
DIVISION_CHOICE=(7777,8888,9999)
BLOCK_CHOICE=(503,504,506,509,513,514,537,538,539,541,545,584,590)
FACILITY_CHOICE=(1970,2046,2046,1704,2057,2044,2044,3060,3060,1701,1131,1136,1080,1137,1097,1137,1082,1137,2455,1130,1081,1109,1082,1115,1117,1082,1114,1096,1130,1093,786,854,875,845,869,875,815,985,867,1241
)
SUBFACILITY_CHOICES=(11111,10459,10463,8738,300001,300002,10425,16144,11177,7608,11976,15799,14266,11784,15789,15783,15682,15745,14306,15096,15913,11782,15680,15772,15768,15681,33333,15098,11965,15448,3940,55555,3949,3993,5405,5412,3979,3975,5419,5822
)
VILLAGE_CHOICES=(18099,17947,17950,17915,400001,400002,400003,400004,400005,400006,16581,16051,15126,15313,14987,15033,14921,15506,16316,16494,14860,15326,14892,14415,14514,14914,15301,16423,16552,16396,13100,12789,10000457,12986,10012688,13203,12910,10014300,10012700,13029
)

def randon_string_generator(size,type=None):
	if type == 'char':
		data = string.ascii_uppercase+string.ascii_lowercase
	elif type == 'string':
		data = string.ascii_uppercase + string.ascii_lowercase
	elif type == 'number':
		data = string.digits
	  
	elif type== 'charnum':
		data = string.ascii_lowercase + string.digits
	return ''.join(random.choice(data) for _ in range(size))


class Command(BaseCommand):


	def add_arguments(self, parser):
		parser.add_argument('no_anms', type=int)

	def handle(self, *args, **options):
		try:
			no_anms = options.get('no_anms')
			response_data=[]
			current_date = datetime.datetime.now().date()
			worker_obj_list = Worker.objects.all().first()
			user_list=User.objects.all()
			user_username_list=[]
			for each_user in user_list:
				user_username_list.append(each_user)
			wrk=Worker.objects.get(pk=1)
			for i in range(no_anms):
				kwargs={
	 				'app_name':'abcd',
	 				
	 				'registration_number':randon_string_generator(10,'number'),
	 				'registration_date':current_date.isoformat(),
	 				'aadhar_number':randon_string_generator(12,'number'),
	 				'rationcard_number':randon_string_generator(10,'charnum'),
	 				'title':random.choice(TITLE_CHOICE),
				    'name':randon_string_generator(7,'string'),
					
					'surname':randon_string_generator(7,'string'),					
					'gender':random.choice(GENDER),
					'guardian':random.choice(GUARDIAN_CHOICES),
					'guardian_name':randon_string_generator(10,'string'),					
					'age':randon_string_generator(2,'number'),
					'age_in':randon_string_generator(2,'string'),					
					'blood_group':random.choice(BLOOD_GROUP),
					'date_of_birth':datetime.date(randint(2005,2025), randint(1,12),randint(1,28)).isoformat(),
					'email':randon_string_generator(10,'string') + '@gmail.com',
					'mobile_number':str(random.choice(MOBILE_STARTS)) + randon_string_generator(9,'number'),
					'marital_status':random.choice(MARITIAL_STATUS),
					'religion':random.choice(RELIGION),
					'occupation':random.choice(OCCUPATION),
					'education':random.choice(EDUCATION),
					'nationality':random.choice(NATIONALITY),
					'socio_ecnomic':randon_string_generator(10,'string'),
					'address':randon_string_generator(10,'string'),
					'pincode': '5'+randon_string_generator(5,'number'),
					'state_code':'1',
					'district_code':random.choice(DISTRICT_CHOICE),
					'division_code':random.choice(DISTRICT_CHOICE),
					'block_code':random.choice(BLOCK_CHOICE),
					'facility_code':random.choice(FACILITY_CHOICE),
					'facility_type':'PHC',
					'subfacility_code':random.choice(SUBFACILITY_CHOICES),
					'village_code':random.choice(VILLAGE_CHOICES),
					'updated_by':random.choice(user_username_list),
					'created_by':random.choice(user_username_list)
					
					}
				# print kwargs
				patient_obj =Patient.objects.create(**kwargs)
				patient_obj.save()
				patient_obj.worker.add(worker_obj_list)
		except Exception as e:
			print e
			pass


	

