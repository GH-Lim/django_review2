from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.pk}번 의사 {self.name}'


# patient.doctors.all()
# patient_set.all() 이 아닌 doctor.patients.all() 로 하고 싶어
class Patient(models.Model):
    name = models.CharField(max_length=200)
    doctors = models.ManyToManyField(Doctor, related_name='patients')
    # 두번째로 만든 모델에 첫번째로 만든 모델 정보를 넘겨준다
    # 중계 모델 없어도 된다.
    def __str__(self):
        return f'{self.pk}번 환자 {self.name}'


# class Reservation(models.Model):
#     doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.doctor.id}번 의사의 {self.patient.id}번 환자'
