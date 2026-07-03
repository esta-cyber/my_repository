from django.urls import path
from .views import student_qushish, studentlar_ruyxati, studentni_tahrirlash, studentni_uchirish

urlpatterns = [
    path('', studentlar_ruyxati, name='ruyxat'),
    path('qushish/', student_qushish, name='qushish'),
    path('tahrirlash/<int:id>/', studentni_tahrirlash, name='tahrirlash'),
    path('uchirish/<int:id>/', studentni_uchirish, name='uchirish'),
]