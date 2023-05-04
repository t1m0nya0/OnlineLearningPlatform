from rest_framework import serializers

from courses.models import Course, Category


class CourseModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = "__all__"


class CategoryModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = "__all__"
