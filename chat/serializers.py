from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Message
from details.models import Faculty


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    online = serializers.ReadOnlyField(source='userprofile.online')

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'online']


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())
    receiver = serializers.SlugRelatedField(many=False, slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Message
        fields = ['sender', 'receiver', 'message', 'timestamp']


class FacultySerializer(serializers.ModelSerializer):
    faculty_id = serializers.CharField()
    faculty_name = serializers.CharField()
    image = serializers.FileField()

    class Meta:
        model = Faculty
        fields = ['faculty_id', 'faculty_name', 'image']


# class TimelineSerializer(serializers.Serializer):
#     faculties = FacultySerializer(many=True)
#     users = UserSerializer(many=True)


