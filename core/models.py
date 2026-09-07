from django.db import models
from django.utils import timezone

class SchoolInfo(models.Model):
    name = models.CharField(max_length=200, default="Guru Nanak Sr Sec School")
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to="school_logo/", blank=True, null=True)

    def __str__(self):
        return self.name

class ClassSection(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        unique_together = ('class_name', 'section')

    def __str__(self):
        return f"{self.class_name} - {self.section or 'All'}"

class Subject(models.Model):
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE, related_name="subjects")
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.subject_name} ({self.class_section})"

class Student(models.Model):
    registration_no = models.CharField(max_length=50, unique=True)
    student_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    class_section = models.ForeignKey(ClassSection, on_delete=models.SET_NULL, null=True, blank=True)
    section = models.CharField(max_length=10, blank=True, null=True)
    roll_no = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=20, default="Male")
    dob = models.DateField(default=timezone.now)
    blood_group = models.CharField(max_length=10, blank=True, null=True)
    father_name = models.CharField(max_length=100, blank=True, null=True)
    mother_name = models.CharField(max_length=100, blank=True, null=True)
    father_mobile = models.CharField(max_length=20, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    mobile_for_sms = models.CharField(max_length=20, default="0000000000")
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="student_photos/", blank=True, null=True)
    date_of_admission = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_name} ({self.registration_no})"

class Employee(models.Model):
    employee_id = models.CharField(max_length=50, unique=True, blank=True, null=True)
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    joining_date = models.DateField(default=timezone.now)
    salary = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    address = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="employee_photos/", blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.designation or 'Staff'})"

class BankDetail(models.Model):
    bank_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=50, unique=True)
    ifsc_code = models.CharField(max_length=20)
    branch_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.bank_name} - {self.account_number}"

class FeeParticular(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

class FeeStructure(models.Model):
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    particular = models.ForeignKey(FeeParticular, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.class_section} - {self.particular.title}: ₹{self.amount}"

class FeePayment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="fee_payments")
    particular = models.ForeignKey(FeeParticular, on_delete=models.CASCADE)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateField(default=timezone.now)
    bank_detail = models.ForeignKey(BankDetail, on_delete=models.SET_NULL, null=True, blank=True)
    receipt_no = models.CharField(max_length=50, unique=True, blank=True, null=True)

    def __str__(self):
        return f"Receipt {self.receipt_no} - {self.student.student_name}: ₹{self.amount_paid}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')], default='Present')

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student.student_name} - {self.date} ({self.status})"

class EmployeeAttendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent'), ('Late', 'Late')], default='Present')

    class Meta:
        unique_together = ('employee', 'date')

    def __str__(self):
        return f"{self.employee.name} - {self.date} ({self.status})"

class Exam(models.Model):
    exam_name = models.CharField(max_length=100)
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    term = models.CharField(max_length=50, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.exam_name} ({self.class_section})"

class ExamMark(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="marks")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    max_marks = models.DecimalField(max_digits=5, decimal_places=2, default=100)

    def __str__(self):
        return f"{self.student.student_name} - {self.subject.subject_name}: {self.marks_obtained}/{self.max_marks}"

class Homework(models.Model):
    class_section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    assigned_date = models.DateField(default=timezone.now)
    submission_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.title} - {self.subject.subject_name}"

class MessageNotice(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    recipient_type = models.CharField(max_length=50, default="All")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title