from rest_framework import viewsets
from .models import Faculty, Group, Kafedra, Subject, Teacher, Student
from .serializers import (
    FacultySerializer, GroupSerializer, KafedraSerializer,
    SubjectSerializer, TeacherSerializer, StudentSerializer
)


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class KafedraViewSet(viewsets.ModelViewSet):
    queryset = Kafedra.objects.all()
    serializer_class = KafedraSerializer


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
