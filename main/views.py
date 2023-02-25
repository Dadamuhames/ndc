from .models import Projects, ShortApplications
from rest_framework import generics, views, pagination, filters
from .serializers import ShortApplicationSerializer, ProjectsDetailSerializer, ProjectSerializer, ServicesSerializer, ReviewsSerializer
from .serializers import ArticleSerializer, StaticInformationSerializer, TranslationSerializer, LangsSerializer, PartnersSerializer, ArticleDetailSerializer
from admins.models import Articles, StaticInformation, Partners, Translations, Languages, FAQ, Services, Reviews
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

# pagination
class BasePagination(pagination.PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 1000


# articles list
class ArticlesList(generics.ListAPIView):
    queryset = Articles.objects.filter(active=True).order_by('position')
    serializer_class = ArticleSerializer
    pagination_class = BasePagination


# articles detail
class ArticlesDetail(generics.RetrieveAPIView):
    queryset = Articles.objects.filter(active=True)
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'


# static information
class StaticInfView(views.APIView):
    def get(self, request, format=None):
        try:
            obj = StaticInformation.objects.get(id=1)
        except:
            obj = StaticInformation.objects.create()

        serializer = StaticInformationSerializer(
            obj, context={'request': request})

        return Response(serializer.data)


# translations
class TranslationsView(views.APIView):
    def get(self, request, fromat=None):
        translations = Translations.objects.all()
        serializer = TranslationSerializer(translations, context={'request': request})
        return Response(serializer.data)


# langs list
class LangsList(generics.ListAPIView):
    queryset = Languages.objects.filter(active=True)
    serializer_class = LangsSerializer
    pagination_class = BasePagination


# partners list
class PartnersList(generics.ListAPIView):
    queryset = Partners.objects.filter(active=True).order_by('position')
    serializer_class = PartnersSerializer
    pagination_class = BasePagination


# projects
class ProjectsList(generics.ListAPIView):
    queryset = Projects.objects.filter(active=True).order_by('position')
    serializer_class = ProjectSerializer
    pagination_class = BasePagination


# projects detail
class ProjectsDetail(generics.RetrieveAPIView):
    queryset = Projects.objects.filter(active=True).order_by('position')
    serializer_class = ProjectsDetailSerializer
    lookup_field = 'slug'


# services list
class ServicesList(generics.ListAPIView):
    queryset = Services.objects.order_by('position')
    serializer_class = ServicesSerializer
    pagination_class = BasePagination


# services detail
class ServicesDetail(generics.RetrieveAPIView):
    queryset = Services.objects.order_by('position')
    serializer_class = ServicesSerializer
    lookup_field = 'slug'


# reviews
class ReviewsList(generics.ListAPIView):
    queryset = Reviews.objects.filter(active=True).order_by('position')
    serializer_class = ReviewsSerializer


# application add
class NewAppliction(generics.CreateAPIView):
    serializer_class = ShortApplicationSerializer
    queryset = ShortApplications.objects.all()
