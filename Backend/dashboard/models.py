# from django.db import models
# from django.contrib.auth.models import User        
# from django.utils.translation import gettext_lazy as _

# from django.core.validators import RegexValidator


# # Create your models here.






# class Doctor_data(models.Model):
#      ## firstname lastname email
#     USER_ID =  models.OneToOneField(User,related_name='doctor_USER_ID',on_delete=models.CASCADE,null=False, primary_key=True,unique=True)
#     Speciality = models.CharField(max_length=500)
#     Experience = models.IntegerField()
    
#     phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must start with '9999999999'")
#     PHONENUMBER = models.CharField(validators=[phone_regex], help_text=_('Enter Number in format: "9999999999"') , max_length=10, blank=True, unique=True)

#     def __str__(self):
#         return self.USER_ID




# class Insurance_Provider_data(models.Model):
#     USER_ID =  models.OneToOneField(User,related_name='Insurance_USER_ID',on_delete=models.CASCADE,null=False, primary_key=True,unique=True)

#     phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must start with '9999999999'")
#     PHONENUMBER = models.CharField(validators=[phone_regex], help_text=_('Enter Number in format: "9999999999"') , max_length=10, blank=True, unique=True)

#     def __str__(self):
#         return self.USER_ID



# class Insurance_plan_data(models.Model):
#     Provider_id =  models.OneToOneField(Insurance_Provider_data,related_name='Insurance_Provider_id',on_delete=models.CASCADE,null=False, unique=True)

#     Insurance_plan_id = models.IntegerField(primary_key=True,serialize=True)

#     Plan_name =  models.CharField(max_length = 200)
#     Plan_description =  models.CharField(max_length = 1000)
#     Monthly_premium = models.IntegerField()
#     Coverage_amount = models.IntegerField()

#     def __str__(self):
#         return self.Insurance_plan_id





# class Patient_data(models.Model):
#     ## firstname lastname email
#     USER_ID =  models.OneToOneField(User,related_name='patient_USER_ID',on_delete=models.CASCADE,null=False, primary_key=True,unique=True)
#     Date_of_Birth = models.DateField()
    
#     GENDER_MALE = 0
#     GENDER_FEMALE = 1
#     GENDER_CHOICES = [(GENDER_MALE, 'Male'), (GENDER_FEMALE, 'Female')]
#     gender = models.IntegerField(choices=GENDER_CHOICES)

#     phone_regex = RegexValidator(regex=r'^[7-9]{1}\d{9}', message="Phone number must start with '9999999999'")
#     PHONENUMBER = models.CharField(validators=[phone_regex], help_text=_('Enter Number in format: "9999999999"') , max_length=10, blank=True, unique=True)

#     is_covid = models.BooleanField()
#     Date_of_Admission= models.DateField()
#     Date_of_Discharge= models.DateField()
#     Room_number = models.IntegerField()
#     bed_number = models.IntegerField()

#     Doctor_id = models.OneToOneField(Doctor_data,related_name='Patient_Doctor_id',on_delete=models.CASCADE,null=False,unique=True)
#     Insurance_plan_id = models.OneToOneField(Insurance_plan_data,related_name='Patient_Insurance_plan_id',on_delete=models.CASCADE,null=False,unique=True)

#     def __str__(self):
#         return self.USER_ID





# class Appointmnet_data(models.Model):
#     Appointment_id = models.IntegerField(primary_key=True,serialize=True)
#     Patient_id = models.OneToOneField(Patient_data,related_name='Appointmnet_Patient_id',on_delete=models.CASCADE,null=False, unique=True)
#     Doctor_id = models.OneToOneField(Doctor_data,related_name='Appointmnet_Doctor_id',on_delete=models.CASCADE,null=False, unique=True)

#     Appointmnet_Date = models.DateField()
#     Appointmnet_Time  = models.DateTimeField()
#     Symptons = models.CharField(max_length = 500)
#     Nodes = models.CharField(max_length = 1000)
    

#     def __str__(self):
#             return self.Appointment_id


# class Medical_history_data(models.Model):
#     Patient_id = models.OneToOneField(Patient_data,related_name='Medical_history_Patient_id',on_delete=models.CASCADE,null=False)
#     Doctor_id = models.OneToOneField(Doctor_data,related_name='Medical_history_Doctor_id',on_delete=models.CASCADE,null=False )
   
#     Date_of_visit = models.DateField(unique=True)
#     Diagnosis  = models.CharField(max_length = 500)
#     Treatment = models.CharField(max_length = 500)
#     Nodes = models.CharField(max_length = 1000)
    

#     def __str__(self):
#             return self.Patient_id

# class Symptom_Specialities_data (models.Model):

#     Symptom_Name = models.CharField(max_length = 500)    
#     Speciality = models.CharField(max_length = 500)    

#     def __str__(self):
#             return self.Symptom_Name

