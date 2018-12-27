from django.core.management.base import BaseCommand, CommandError
import random 
import string 
import sys
import datetime
from random import randint
from beneficiary.models import Patient,Appointment
from accounts.models import Worker,User,Doctor
import redis
import json,ast

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

def random_string_generator(size,type=None):
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
            patientr_obj_list=[]
            user_username_list=[]
            for each_user in user_list:
                user_username_list.append(each_user)
            wrk=Worker.objects.get(pk=1)
            redisClient = redis.StrictRedis(host='localhost',port=6379,db=10)
            for i in range(no_anms):
                kwargs={
                    'app_name':'abcd',
                    
                    'registration_number':random_string_generator(10,'number'),
                    'registration_date':current_date.isoformat(),
                    'aadhar_number':random_string_generator(12,'number'),
                    'rationcard_number':random_string_generator(10,'charnum'),
                    'title':random.choice(TITLE_CHOICE),
                    'name':random_string_generator(7,'string'),
                    'surname':random_string_generator(7,'string'),                  
                    'gender':random.choice(GENDER),
                    'guardian':random.choice(GUARDIAN_CHOICES),
                    'guardian_name':random_string_generator(10,'string'),                   
                    'age':random_string_generator(2,'number'),
                    'age_in':random_string_generator(2,'string'),                   
                    'blood_group':random.choice(BLOOD_GROUP),
                    'date_of_birth':datetime.date(randint(2005,2025), randint(1,12),randint(1,28)).isoformat(),
                    'email':random_string_generator(10,'string') + '@gmail.com',
                    'mobile_number':str(random.choice(MOBILE_STARTS)) + random_string_generator(9,'number'),
                    'marital_status':random.choice(MARITIAL_STATUS),
                    'religion':random.choice(RELIGION),
                    'occupation':random.choice(OCCUPATION),
                    'education':random.choice(EDUCATION),
                    'nationality':random.choice(NATIONALITY),
                    'socio_ecnomic':random_string_generator(10,'string'),
                    'address':random_string_generator(10,'string'),
                    'pincode': '5'+random_string_generator(5,'number'),
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
                
                patient_obj =Patient.objects.create(**kwargs)
                patient_obj.save()
                patient_obj.worker.add(worker_obj_list)
                patientr_obj_list.append(patient_obj)
                try:
                    appointment_obj = Appointment.objects.get(registration_number=request.data['registration_number'],visit_date=current_date,status__in=['NEW','DOCTOR-PICKUP','DOCTOR-TO-ANM-CALL','UNANSWERED','REJECTED'])
                except Exception as e:
                    appointment_obj = None 
                token_number=""
                try:
                    app_obj = Appointment.objects.filter(visit_date=current_date.isoformat()) 
                    if app_obj != '':
                        token_number = len(app_obj) + 1
                    else:
                        token_number = 1
                except Exception as e:
                    pass                
                #patient_obj = Patient.objects.get(registration_number=each.registration_number)
                worker_obj = Worker.objects.get(user__username=patient_obj.worker.all().first().user.username)
                try:
                    location_obj = Location.objects.get(state_code=worker_obj.state_code,district_code=worker_obj.district_code,division_code=worker_obj.division_code,facility_code=worker_obj.facility_code,subfacility_code=worker_obj.subfacility_code)    
                    print location_obj,"dfgsdfgds"
                except Exception as e:
                    location_obj = "" 
                doctor_obj_list=[]
                try:
                    doctor_obj = Doctor.objects.all()
                    for each1 in doctor_obj:
                        doctor_obj_list.append(each1.pk)


                except Exception as e:
                    print e
                kwargs1 ={                    
                    "patient_id":patient_obj.pk,
                    "registration_number":patient_obj.registration_number,
                    "doctor_id":random.choice(doctor_obj_list),
                    "worker_id":worker_obj.pk,
                    "status":'NEW',
                    "visit_date":current_date.isoformat(),
                    "state_code" : worker_obj.state_code,
                    "district_code" : worker_obj.district_code,
                    "division_code":worker_obj.division_code,
                    "block_code":worker_obj.block_code,
                    "facility_code":worker_obj.facility_code,
                    "subfacility_code":worker_obj.subfacility_code,
                    "village_code":worker_obj.village_code,
                    "token_number" : token_number              
                    }
                # print kwargs1,"dfgdsfg"
                if appointment_obj == None:
                    print "hello"
                    appointment_obj =Appointment.objects.create(**kwargs1)
                    kwargs1.update({"worker_username":worker_obj.user.username})
                    key_name = "appointment_{0}".format(current_date.isoformat())
                    redisClient.rpush(key_name, patient_obj.registration_number)
                    print patient_obj.date_of_birth,"dfsfgsdfgfsdgdf"
                    kwargs1.update(
                        {
                        "patient_name" : "{0} {1}".format(patient_obj.name,patient_obj.surname),
                        "age" : patient_obj.age,
                        "gender" : patient_obj.gender,
                        "appointment_id" : appointment_obj.id,
                        "token_number" : token_number,
                        "date_of_birth"  : patient_obj.date_of_birth,
                        "subcenter_name":location_obj.subfacility_name if location_obj else ''
                    })
                    print kwargs1,"dfstgsdfgdsfgdfs"                 
                    key_name = "patient_appointment_{0}".format(current_date)
                    redisClient.hset(key_name,patient_obj.registration_number,json.dumps(kwargs1))
                    print "success"
                
        except Exception as e:
            print e
            pass
