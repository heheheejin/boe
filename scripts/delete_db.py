from api.models import *


def run():
    models = [Student, Unit, Course, Faculty, Core, CuratedElective, Enrolment]
    for model in models:
        model.objects.all().delete()