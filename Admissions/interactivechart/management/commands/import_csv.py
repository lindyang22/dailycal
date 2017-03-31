"""source: Daily Cal Grade Distributions Project"""
import os
import csv
# import copytext
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist
from interactivechart.models import *



class Command(BaseCommand):
    help = "Imports admissions data from a Cal Answers CSV file"

    # def add_arguments(self, parser):
        # parser.add_argument('season', type=int, help="season (0: spring, 1: summer, 2: fall)")
        # parser.add_argument('year', type=int, help="academic year")
        # parser.add_argument('inname', help="path to the csv file to read")

    def handle(self, *args, **options):
        # verbosity = options['verbosity']
        # status = create_objects(options['inname'])
        # inname = "interactivechart/applieddata2.csv"
        with open("interactivechart/applieddata2.csv") as infile:
            inreader = csv.reader(infile)
            indices = 0
            i = 0
            # processed = 0
            for row in inreader:
                if indices is 0:
                    header = [s.replace('\xef\xbb\xbf', '') for s in row]
                    indices = 1
                    continue
                student, created = Student.objects.get_or_create(ethnicity = row[0],
                    gender = row[1],        
                    residency = row[2],
                    college = row[3],
                    headcount = row[4],
                    year = row[5],
                    status = row[6]
                )
                student.save()
                
            # applied_student, created_applied = Applied.objects.get_or_create(stats = student)
                # i += 1
                # student_objects.append(data)
        """with open("interactivechart/admitteddata2.csv") as infile:
            inreader = csv.reader(infile)
            indices = 0
            i = 0
            # processed = 0
            for row in inreader:
                # print (i)
                if indices is 0:
                    header = [s.replace('\xef\xbb\xbf', '') for s in row]
                    indices = 1
                    continue
                number = 0
                if row[4] != '':
                    number = row[4]

                student, created = Student.objects.get_or_create(ethnicity = row[0],
                    gender = row[1],        
                    residency = row[2],
                    college = row[3],
                    headcount = number,
                    year = row[5],
                    status = row[6]
                )
                student.save()"""
                
                
                
            # admitted_student, created_admitted = Admitted.objects.get_or_create(stats = student)   
        """with open("interactivechart/SIReddata2.csv") as infile2:
            inreader = csv.reader(infile2)
            indices = 0
            i = 0
            # processed = 0
            for row in inreader:
                if indices is 0:
                    header = [s.replace('\xef\xbb\xbf', '') for s in row]
                    indices = 1
                    continue
                number = 0
                if row[4] != '':
                    number = row[4]
                student, created = Student.objects.get_or_create(ethnicity = row[0],
                    gender = row[1],        
                    residency = row[2],
                    college = row[3],
                    headcount = number,
                    year = row[5],
                    status = row[6]
                    )
                student.save()"""
                
            # enrolled_student, created_admitted = Enrolled.objects.get_or_create(stats = student) 

"""def create_objects(inname, verbosity=1):
    # assumption: this csv only contains data for one term, so CCNs are unique
    # student = Student()
    # data['sections'] maps CCN to a Section object
    student_data = []
    # data = {'student': {}}
    with open(inname, 'r+') as infile:
        inreader = csv.reader(infile)
        indices = None
        # processed = 0
        for row in inreader:
            if indices is None:
                header = [s.replace('\xef\xbb\xbf', '') for s in row]
                indices = find_indices(header)
                continue
            data = process_row(row, indices)
            student_objects.append(data)
    return student_data
"""


def process_row(row, indices, i):
    """Find the section corresponding to ROW, create necessary objects,
    and add the grade count."""
    
    
    student, created = Student.objects.get_or_create(i)

    student.ethnicity = row['Ethnicity'],
    student.gender = row['Gender'],        
    student.residency = row['Residency'],
    student.college = row['College'],
    student.headcount = row['Headcounts'],
    student.year = row['Academic_Yr']

    
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
        'Ethnicity': header.index("Ethnicity"),
        'Gender': header.index("Gender"),
        'Residency': header.index("Derived Residency"),    
        'College': header.index("College"),
        'Headcounts': header.index("Headcounts"),
        'Academic_Yr': header.index("Academic_Yr")
        # 'status': header.index("")
    }