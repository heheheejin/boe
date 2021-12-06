from django.db import models

SEMESTER_CHOICE = [
    ("1", "Semester 1"),
    ("2", "Semester 2"),
    ("3", "October Semester")
]


class Faculty(models.Model):
    faculty_name = models.CharField(
        max_length=64, verbose_name="Faculty Name",
        unique=True
    )

    class Meta:
        ordering = ["faculty_name"]
        verbose_name = 'faculty'
        verbose_name_plural = 'faculties'

    def __str__(self):
        return f'Faculty: {self.faculty_name}'


class Course(models.Model):
    course_code = models.CharField(
        max_length=16, verbose_name="Course Code"
    )
    course_version = models.PositiveSmallIntegerField(
        null=True,
        default=None,
        verbose_name="Course Version"
    )
    faculty = models.ForeignKey(
        to='Faculty',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Faculty in which the Course belongs to"
    )
    course_name = models.CharField(
        max_length=50, verbose_name="Course Name"
    )
    course_required_credits = models.PositiveSmallIntegerField(
        verbose_name="Total Credits Requried to Complete this Course"
    )
    course_duration_limit = models.PositiveSmallIntegerField(
        default=8,
        verbose_name="Maximum Years to Complete this Course"
    )
    course_curate_electives_credits = models.PositiveSmallIntegerField(
        verbose_name="Specialized list of Electives required to complete this Course"
    )

    class Meta:
        ordering = ['faculty', 'course_code']
        verbose_name = 'course'
        verbose_name_plural = 'courses'
        unique_together = [['course_code', 'course_version']]

    def save(self, *args, **kwargs):
        if not Course.objects.filter(pk=self.pk).exists():
            self.course_version = max([
                x.course_version for x in Course.objects.filter(course_name=self.course_name)
            ] + [0]) + 1
        super(Course, self).save(*args, **kwargs)

    def __str__(self):
        return f'Course: {self.course_code}.v{self.course_version}'


class Student(models.Model):
    student_id = models.CharField(
        max_length=128,
        verbose_name="Student ID"
    )
    course = models.ForeignKey(
        to="Course",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Course in which the Student is enrolled in"
    )
    student_name = models.CharField(
        max_length=256, verbose_name="Student's Name"
    )
    student_email = models.EmailField(  # Can build custom validator for monash emails
        max_length=128,
        verbose_name="Student Email"
    )
    student_intake_year = models.PositiveSmallIntegerField(
        verbose_name="Student's Intake Year"
    )
    student_intake_semester = models.CharField(  # not sure if should use charfield
        max_length=64,
        choices=SEMESTER_CHOICE,
        verbose_name="Student's First Semester Intake"
    )
    has_graduated = models.BooleanField(verbose_name="Have Student Graduated?")

    class Meta:
        ordering = ['course', 'student_id']
        verbose_name = 'student'
        verbose_name_plural = 'students'

    def __str__(self):
        return f'Student: {self.student_id} {self.student_name}'


class Unit(models.Model):
    unit_code = models.CharField(
        max_length=32,
        verbose_name="Unit Code"
    )
    faculty = models.ForeignKey(
        to="Faculty",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Faculty Responsible for the Unit"
    )
    unit_name = models.CharField(
        max_length=128,
        verbose_name="Name of the Unit"
    )
    unit_credits = models.PositiveSmallIntegerField(
        verbose_name="Credits Awarded for Completing this Unit"
    )

    class Meta:
        ordering = ['faculty', 'unit_code']
        verbose_name = 'unit'
        verbose_name_plural = 'units'

    def __str__(self):
        return f'Unit: {self.unit_code} {self.unit_name}'


class Core(models.Model):
    course = models.ForeignKey(
        to="Course",
        on_delete=models.CASCADE
    )
    unit = models.ForeignKey(
        to="Unit",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = [['course', 'unit']]
        ordering = ['course', 'unit']
        verbose_name = 'core'
        verbose_name_plural = 'cores'

    def __str__(self):
        return f'Core: {self.course} - {self.unit}'


class CuratedElective(models.Model):
    course = models.ForeignKey(
        to="Course",
        on_delete=models.CASCADE
    )
    unit = models.ForeignKey(
        to="Unit",
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = [['course', 'unit']]
        ordering = ['course', 'unit']
        verbose_name = 'curated elective'
        verbose_name_plural = 'curated electives'

    def __str__(self):
        return f'CuratedElective: {self.course} - {self.unit}'


class Enrolment(models.Model):
    student = models.ForeignKey(
        to="Student",
        on_delete=models.CASCADE,  # cascade???
        verbose_name="Student Object in this Enrolment"
    )
    unit = models.ForeignKey(
        to="Unit",
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Unit in which the Student has Enrolled in"
    )
    enrolment_year = models.PositiveSmallIntegerField(
        verbose_name="Year in which Student is Taking this Unit"
    )
    enrolment_semester = models.CharField(  # not sure if should use charfield
        max_length=64,
        choices=SEMESTER_CHOICE,
        verbose_name="Semester in which Student is Taking this Unit"
    )
    enrolment_marks = models.SmallIntegerField(
        null=True,
        verbose_name="Marks obtained by the Student in this Unit"
    )
    has_passed = models.BooleanField(
        verbose_name="Has the Student Passed this Unit?"
    )

    class Meta:
        ordering = ['student', 'unit']
        verbose_name = 'enrolment'
        verbose_name_plural = 'enrolments'

    def __str__(self):
        return f'Enrolment: {self.student.student_id} - {self.unit.unit_code}'