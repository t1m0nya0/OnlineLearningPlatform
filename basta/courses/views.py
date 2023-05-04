from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import viewsets, generics, mixins, status
from rest_framework import filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from .models import Course, Category
from .serializers import CourseModelSerializer, CategoryModelSerializer
from .permissions import IsOwnerOrReadOnly


class CourseApiList(generics.ListCreateAPIView):
    search_fields = ['^name']
    filter_backends = (filters.SearchFilter,)
    permission_classes = (IsAuthenticatedOrReadOnly, )
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        free = self.request.query_params.get('is_free', None)
        if free == 'true':
            queryset = queryset.filter(is_free=True)
        return queryset


class CourseApiDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly, )
    queryset = Course.objects.all()
    serializer_class = CourseModelSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, )
    serializer_class = CategoryModelSerializer


#################################################################################


class CourseByCategoryList(mixins.ListModelMixin,
                           mixins.CreateModelMixin,
                           GenericAPIView):

    def create(self, request, *args, **kwargs):
        request.data["cat"] = kwargs["cat_id"]
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    serializer_class = CourseModelSerializer

    def get_queryset(self):
        return Course.objects.filter(cat_id=self.kwargs["cat_id"])
