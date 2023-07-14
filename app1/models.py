from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#  "AutoField",
#     "BLANK_CHOICE_DASH",
#     "BigAutoField",
#     "BigIntegerField",
#     "BinaryField",
#     "BooleanField",
#     "CharField",
#     "CommaSeparatedIntegerField",
#     "DateField",
#     "DateTimeField",
#     "DecimalField",
#     "DurationField",
#     "EmailField",
#     "Empty",
#     "Field",
#     "FilePathField",
#     "FloatField",
#     "GenericIPAddressField",
#     "IPAddressField",
#     "IntegerField",
#     "NOT_PROVIDED",
#     "NullBooleanField",
#     "PositiveBigIntegerField",
#     "PositiveIntegerField",
#     "PositiveSmallIntegerField",
#     "SlugField",
#     "SmallAutoField",
#     "SmallIntegerField",
#     "TextField",
#     "TimeField",
#     "URLField",
#     "UUIDField"


class emp(models.Model):
    name = models.CharField(max_length=60)
    joining_date = models.DateField()
    email_id = models.EmailField(unique= True)
    department = models.CharField(max_length=50)
    salary = models.FloatField()
    job_status = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)  #ALTER TABLE "emp_data" ADD COLUMN "is_active" boolean DEFAULT true NOT NULL;
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return f"{self.__dict__}"
    
    # def __repr__(self):
    #     return str(self)
    
    class Meta:
        db_table = "emp_data"