from rest_framework import serializers

from courses.models import Course, Category


class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=100)
    description = serializers.CharField()
    duration = serializers.IntegerField()
    is_free = serializers.BooleanField(default=False)
    price = serializers.FloatField()
    image = serializers.CharField(max_length=255)
    favorites = serializers.BooleanField(default=False)
    cat = serializers.IntegerField()
    user = serializers.CharField(max_length=255)


class CourseModelSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Course
        fields = "__all__"


class CategoryModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
