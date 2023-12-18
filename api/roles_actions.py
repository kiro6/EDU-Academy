"""
Contains functions for the actions that are different between user roles.
"""

from django.shortcuts import redirect
from django.urls import reverse
from django.db.models import Avg
from rest_framework.response import Response
from .serializers import *
from .views_checks import *

# Note that `request.FILES` will only contain data if the request method was POST,
# at least one file field was actually posted,
# and the <form> that posted the request has the attribute enctype="multipart/form-data".
# Otherwise, `request.FILES` will be empty.


# REMEMBER TO REMOVE PARTIAL

######################
# Profile completion #
######################

def teacher_complete_profile(request):
    serializer = TeacherProfileSerializer(data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
    
    teacher = Teacher.objects.create(
        teacher = request.user,
        # personal_photo = data['personal_photo'],
        # national_ID_photo = data['national_ID_photo'],
    )
    teacher.save()
    TeachRequest.objects.create(teacher=teacher).save()
    return redirect("api:view_profile", username=request.user.username)

def student_complete_profile(request):
    serializer = StudentProfileSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
    
    Student.objects.create(
        student=request.user,
        academic_year = data['academic_year'],
        study_field = data['study_field'] if data.get('study_field') else None,
        parent_name = data['parent_name'],
        parent_phone_number = data['parent_phone_number'],
        personal_photo = data['personal_photo'] if data.get('personal_photo') else None,
    ).save()
    return redirect("api:view_profile", username=request.user.username)

def assistant_complete_profile(request):
    serializer = AssistantProfileSerializer(data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
    
    Assistant.objects.create(
        assistant=request.user,
        # personal_photo = data['personal_photo'],
        # national_ID_photo = data['national_ID_photo'],
    ).save()
    return redirect("api:view_profile", username=request.user.username)


###################
# Profile viewing #
###################

def teacher_view_profile(user, user_profile: dict, view_self):
    teacher = Teacher.objects.get(teacher=user)
    user_profile.update(
        {
            "balance" : teacher.balance if view_self else None,
            "accepted" : teacher.accepted,
            "personal_photo" : teacher.personal_photo,
            "national_ID_photo" : teacher.national_ID_photo if view_self else None,
        }
    )
    return Response(user_profile)
    
def student_view_profile(user, user_profile: dict, view_self):
    student = Student.objects.get(student=user)
    badges_list = student.badge_set.all()
    user_profile.update(
        {
            "academic_year" : student.academic_year,
            "study_field" : student.study_field,
            "parent_phone_number" : student.parent_phone_number,
            "parent_name" : student.parent_name,
            "points" : student.points if view_self else None,
            "balance" : student.balance if view_self else None,
            "verified" : student.verified if view_self else None,
            "personal_photo" : student.personal_photo if student.personal_photo else None,
            "badges" : [badge.badge_name for badge in badges_list]
        }
    )
    return Response(user_profile)

def assistant_view_profile(user, user_profile: dict, view_self):
    assistant = Assistant.objects.get(assistant=user)
    user_profile.update(
        {
            "personal_photo" : assistant.personal_photo,
            "national_ID_photo" : assistant.national_ID_photo if view_self else None,
        }
    )
    return Response(user_profile)


########
# Home #
########

def teacher_home(user):
    return Response("Home Page")

def student_home(user):
    enrolled_courses = student_my_courses(user)
    student = Student.objects.get(student=user)
    courses = Course.objects.all().difference(student.course_set.all())[:20]

    not_enrolled_courses = [
        {
            "name": course.course_name,
            "description": course.description,
            "is_completed": course.completed,
            "teacher": User.objects.get(pk=course.teacher.pk).first_name + " " +
                       User.objects.get(pk=course.teacher.pk).last_name,
            # "thumbnail": course.thumbnail,
            "subject": course.subject.subject_name,
        } for course in courses
    ]

    output = {
        "enrolled_courses": enrolled_courses,
        "not_enrolled_courses": not_enrolled_courses,
    }

    return Response(output)

def assistant_home(user):
    return Response("Home Page")


##############
# My courses #
##############

def teacher_my_courses(user):
    teacher = Teacher.objects.get(teacher=user)
    courses = teacher.course_set.all()
    output = [
        {
            "name": course.course_name,
            "description": course.description,
            "is_completed": course.completed,
            "creation_date": course.creation_date.date(),
            # "thumbnail": course.thumbnail,
            "subject": course.subject.subject_name,
        } for course in courses
    ]
    return output

def student_my_courses(user):
    student = Student.objects.get(student=user)
    courses = student.course_set.all()
    output = [
        {
            "name": course.course_name,
            "description": course.description,
            "is_completed": course.completed,
            "enrolled_date": Enrollment.objects.get(course=course, student=student).start_date.date(),
            "teacher": User.objects.get(pk=course.teacher.pk).first_name + " " +
                       User.objects.get(pk=course.teacher.pk).last_name,
            # "thumbnail": course.thumbnail,
            "subject": course.subject.subject_name,
        } for course in courses
    ]
    return output

def assistant_my_courses(user):
    assistant = Assistant.objects.get(assistant=user)
    courses = assistant.course_set.all()
    output = [
        {
            "name": course.course_name,
            "description": course.description,
            "is_completed": course.completed,
            "assisting_date": Assisting.objects.get(course=course, assistant=assistant).start_date.date(),
            "teacher": User.objects.get(pk=course.teacher.pk).first_name + " " +
                       User.objects.get(pk=course.teacher.pk).last_name,
            # "thumbnail": course.thumbnail,
            "subject": course.subject.subject_name,
        } for course in courses
    ]
    return output

###############
# View course #
###############

def get_basic_course_info(course_id:int):
    course = Course.objects.get(pk=course_id)
    info = {
        "course_name" : course.course_name,
        "teacher" : {
            f"{course.teacher.teacher.first_name} {course.teacher.teacher.last_name}" : 
                reverse("api:view_profile",args=(course.teacher.teacher.username,))
        },
        "subject" : course.subject.subject_name,
        "lectures" : [
            {
                "lecture_title" : lecture.lecture_title,
                "upload_date" : lecture.upload_date
            } for lecture in Lecture.objects.filter(course=course)
        ],
        "assistants" : [
            {
                f"{assistant.assistant.first_name} {assistant.assistant.last_name}" :
                    reverse("api:view_profile",args=(assistant.assistant.username,))
            } for assistant in course.assistants.all()
        ],
        "description" : course.description,
        "lecture_price" : course.lecture_price,
        "package_size" : course.package_size,
        # "thumbnail" : course.thumbnail,
        "creation_date" : course.creation_date,
        "completed" : course.completed,
        "rating" : CourseRating.objects.filter(course=course).aggregate(avg_rating=Avg('rating'))['avg_rating']
    }
    return (info, course)

def teacher_view_course(user, course_id):
    basic_course_info, course = get_basic_course_info(course_id)
    if not teacher_created_course(user, course_id):
        return basic_course_info
    
    basic_course_info.update(
        {
            "students" : [
                {
                    f"{student.student.first_name} {student.student.last_name}" :
                        reverse("api:view_profile",args=(student.student.username,))
                } for student in course.students.all()
            ]
        }
    )
    return basic_course_info

def student_view_course(user, course_id):
    student = Student.objects.get(student=user)
    basic_course_info, course = get_basic_course_info(course_id)    
    if not student_enrolled_in_course(user, course_id):
        return basic_course_info
    basic_course_info.update(
        {
            "enrollment_date" :  Enrollment.objects.get(student=student, course=course).start_date,
            "warnings_count" : Warnings.objects.filter(student=student, course=course).count()
        }
    )
    return basic_course_info

def assistant_view_course(user, course_id):
    assistant = Assistant.objects.get(assistant=user)
    basic_course_info, course = get_basic_course_info(course_id)    
    if not assistant_assisting_in_course(user, course_id):
        return basic_course_info
    basic_course_info.update(
        {
            "start_date" :  Assisting.objects.get(assistant=assistant, course=course).start_date,
        }
    )
    return basic_course_info

####################
# Roles -> actions #
####################

roles_to_actions = {
    "Teacher": {
        "completion": teacher_complete_profile,
        "viewing": teacher_view_profile,
        "home": teacher_home,
        "my_courses": teacher_my_courses,
        "view_course": teacher_view_course,
    },
    "Student": {
        "completion": student_complete_profile,
        "viewing": student_view_profile,
        "home": student_home,
        "my_courses": student_my_courses,
        "view_course": student_view_course,
    },
    "Assistant": {
        "completion": assistant_complete_profile,
        "viewing": assistant_view_profile,
        "home": assistant_home,
        "my_courses": assistant_my_courses,
        "view_course": assistant_view_course,
    },
}