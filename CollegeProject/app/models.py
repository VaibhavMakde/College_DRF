from django.db import models
from users.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class SessionYear(models.Model):

    id = models.AutoField(primary_key=True)
    session_start_year = models.DateField()
    session_end_year = models.DateField()
    objects = models.Manager()

    class Meta:
        verbose_name = 'Session Year'
        verbose_name_plural = 'Session Years'



class AdminHOD(models.Model):

    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

  

    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'



class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()


    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professors'


class Courses(models.Model):
    id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    def __str__(self):
        return self.course_name

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

class Subjects(models.Model):
    id =models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=255)

    course_id = models.ForeignKey(Courses, on_delete=models.CASCADE, default=1)
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        verbose_name = 'Subject'
        verbose_name_plural = 'Subjects'

    def __str__(self):
        return self.subject_name


class Exam(models.Model):
    id = models.AutoField(primary_key=True)
    EXAM_CHOICES = (
        ('SEM 1', 'SEM 1'),
        ('SEM 2', 'SEM 2'),
        ('SEM 3', 'SEM 3'),
        ('SEM 4', 'SEM 4'),
        ('SEM 5', 'SEM 5'),
        ('SEM 6', 'SEM 6'),
        ('SEM 7', 'SEM 7'),
        ('SEM 8', 'SEM 8'),
    )
    exam = models.CharField(max_length=5, choices=EXAM_CHOICES)
    date = models.DateField()
    subjects = models.ManyToManyField(Subjects, verbose_name="Subject", related_name="subjects")

    class Meta:
        verbose_name = 'Exam'
        verbose_name_plural = 'Exams'

    def __str__(self):
        return self.exam


class Students(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.OneToOneField(User, on_delete = models.CASCADE)
    gender = models.CharField(max_length=50)
    profile_pic = models.FileField()
    address = models.TextField()
    course_id = models.ForeignKey(Courses, on_delete=models.DO_NOTHING, default=1)
    session_year_id = models.ForeignKey(SessionYear, null=True,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'
    

@receiver(post_save, sender=User)
 
# Now Creating a Function which will
# automatically insert data in HOD, Staff or Student
def create_user_profile(sender, instance, created, **kwargs):
    # if Created is true (Means Data Inserted)
    if created:
        print("User Created!!!-------------------->")
        print(type(instance.user_type))
        # Check the user_type and insert the data in respective tables
        if int(instance.user_type) == 1:
            print("123424")
            AdminHOD.objects.create(user_id=instance)
            print("Admin created")
        if int(instance.user_type) == 2:
            Professor.objects.create(user_id=instance)
        if int(instance.user_type) == 3:
            Students.objects.create(user_id=instance,
                                    course_id=Courses.objects.get(id=7),
                                    session_year_id=SessionYear.objects.get(id=1),
                                    address="",
                                    profile_pic="",
                                    gender="")
     
 
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type == 1:
        instance.adminhod.save()
    if instance.user_type == 2:
        instance.professor.save()
    if instance.user_type == 3:
        instance.students.save()