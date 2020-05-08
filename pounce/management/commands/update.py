import os
import requests

from django.core.management.base import BaseCommand

from ...models import Course, Section


# this might be realy slow to update
def update(term='1212', subject='COS'):
    if os.getenv('HEROKU'):
        subject = 'all'

    url = f"http://etcweb.princeton.edu/webfeeds/courseofferings/?fmt=json&term={term}&subject={subject}"
    data = requests.get(url).json()

    # might be a better way to do this in bulk
    # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create
    # https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-update
    for subject in data['term'][0]['subjects']:
        for course in subject['courses']:
            c, _ = Course.objects.update_or_create(
                course_id=course['course_id'],
                defaults={
                    'subject' : subject['code'],
                    'number'  : course['catalog_number'],
                    'title'   : course['title']
                }
            )

            try:
                for section in course['classes']:
                    s, _ = Section.objects.update_or_create(
                        class_number=section['class_number'],
                        defaults={
                            'course'     : c,
                            'name'       : section['section'],
                            'status'     : section['status'],
                            'start_time' : section['schedule']['meetings'][0]['start_time'],
                            'end_time'   : section['schedule']['meetings'][0]['end_time'],
                            'days'       : " ".join(section['schedule']['meetings'][0].get('days', []))           
                        }
                    )
            except:
                print(c)


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        update()
