from django.contrib import admin
from .models import (
    SchoolInfo, ClassSection, Subject, Student, Employee, 
    BankDetail, FeeParticular, FeeStructure, FeePayment, 
    Attendance, EmployeeAttendance, Exam, ExamMark, Homework, MessageNotice
)

@admin.register(SchoolInfo)
class SchoolInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email')

@admin.register(ClassSection)
class ClassSectionAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'section')

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'class_section', 'subject_code')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('registration_no', 'student_name', 'class_section', 'father_name', 'phone_number')
    search_fields = ('student_name', 'registration_no', 'phone_number')

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('employee_id', 'name', 'designation', 'phone', 'salary')
    search_fields = ('name', 'employee_id')

@admin.register(BankDetail)
class BankDetailAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'account_number', 'ifsc_code')

@admin.register(FeeParticular)
class FeeParticularAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(FeeStructure)
class FeeStructureAdmin(admin.ModelAdmin):
    list_display = ('class_section', 'particular', 'amount')

@admin.register(FeePayment)
class FeePaymentAdmin(admin.ModelAdmin):
    list_display = ('receipt_no', 'student', 'particular', 'amount_paid', 'payment_date')

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'date', 'status')
    list_filter = ('status', 'date')

@admin.register(EmployeeAttendance)
class EmployeeAttendanceAdmin(admin.ModelAdmin):
    list_display = ('employee', 'date', 'status')
    list_filter = ('status', 'date')

@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'class_section', 'term', 'start_date')

@admin.register(ExamMark)
class ExamMarkAdmin(admin.ModelAdmin):
    list_display = ('exam', 'student', 'subject', 'marks_obtained', 'max_marks')

@admin.register(Homework)
class HomeworkAdmin(admin.ModelAdmin):
    list_display = ('title', 'class_section', 'subject', 'assigned_date')

@admin.register(MessageNotice)
class MessageNoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'recipient_type', 'created_at')