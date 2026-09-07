from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-student/', views.add_student, name='add_student'),
    path('classes/', views.classes_list, name='classes_list'),
    path('add-class/', views.add_new_class, name='add_class'),
    path('subjects/', views.subjects_view, name='subjects'),
    path('school-info/', views.school_info_view, name='school_info'),
    path('submit-fees/', views.submit_fees_view, name='submit_fees'),
    path('fee-particulars/', views.fee_particulars_view, name='fee_particulars'),
    path('mark-attendance/', views.mark_attendance_view, name='mark_attendance'),
    path('employees/', views.employee_list_view, name='employees'),
    path('exam-marks/', views.exam_marks_view, name='exam_marks'),
    path('export-students/', views.export_students_excel, name='export_students'),
    path('import-students/', views.import_students_excel, name='import_students'),
]