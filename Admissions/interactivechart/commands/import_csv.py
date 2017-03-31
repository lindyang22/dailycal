"""source: Daily Cal Grade Distributions Project"""

import csv
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from models import *

class Command(BaseCommand):
    help = "Imports admissions data from a Cal Answers CSV file"

    def add_arguments(self, parser):
        # parser.add_argument('season', type=int, help="season (0: spring, 1: summer, 2: fall)")
        # parser.add_argument('year', type=int, help="academic year")
        parser.add_argument('inname', help="path to the csv file to read")

    def handle(self, *args, **options):
        # verbosity = options['verbosity']
        status = create_objects(options['inname'])

def create_objects(inname, verbosity=1):
    # assumption: this csv only contains data for one term, so CCNs are unique
    # student = Student()
    # data['sections'] maps CCN to a Section object
    student_data = []
    # data = {'student': {}}
    with open(inname, 'r+') as infile:
        inreader = csv.reader(infile)
        indices = None
        processed = 0
        for row in inreader:
            if indices is None:
                header = [s.replace('\xef\xbb\xbf', '') for s in row]
                indices = find_indices(header)
                continue
            data = process_row(row, indices)
            student_objects.append(data)
    return student_data


def process_row(row, indices):
    """Find the section corresponding to ROW, create necessary objects,
    and add the grade count."""
    
        """
        Create all or any of the
        subject, course, section, grade, and grade count
        if they don't exist.
        """
    student = Student.objects.get_or_create(
        student.ethnicity = row[indices['ethnicity']],
        student.gender = row[indices['gender']],        
        student.residency = row[indices['residency']],
        student.college = row[indices['college']],
        student.headcount = row[indices['headcount']],
        student.year = int(str(row[indices['year']])[:4]),
    )[0]
    
    # data['student'][data_index] = student
    """letter = row[indices['letter']] == "Letter Grade"
    points = row[indices['points']]
    points = float(points) if len(points) > 0 else None
    grade = Grade.objects.get_or_create(name=row[indices['grade_name']],
                                        letter=letter,
                                        points=points)[0]
    try:
        gradecount = GradeCount.objects.get(section_id=data['sections'][ccn].id, grade_id=grade.id)
    except ObjectDoesNotExist:
        gradecount = GradeCount(section=data['sections'][ccn], grade=grade)
    gradecount.count = int(row[indices['count']])
    gradecount.save()"""
    return student

def find_indices(header):
    """Return the positions of relevant fields in our rows."""
    return {
        # 'subject': header.index("Course Subject Short Nm"),
        'ethnicity': header.index("Ethnicity"),
        'gender': header.index("Gender"),
        'residency': header.index("Derived Residency"),    
        'college': header.index("College"),
        'headcount': header.index("Headcounts"),
        'year': header.index("Academic_Yr")
    }