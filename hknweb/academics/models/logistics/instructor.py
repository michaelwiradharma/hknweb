from django.db import models

from hknweb.academics.models.base_models import AcademicEntity


class Instructor(AcademicEntity):
    instructor_id = models.CharField(max_length=500, primary_key=True)