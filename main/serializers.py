from .models import Projects, ShortApplications
from rest_framework import serializers
from django.conf import settings
from django.core.files.storage import default_storage
from easy_thumbnails.templatetags.thumbnail import thumbnail_url, get_thumbnailer
from admins.models import Articles, StaticInformation, Languages, Translations, MetaTags, Partners, FAQ, Services, Reviews



# image serializer
class ThumbnailSerializer(serializers.BaseSerializer):
    def __init__(self, alias, instance=None, **kwargs):
        super().__init__(instance, **kwargs)
        self.alias = alias

    def to_representation(self, instance):
        alias = settings.THUMBNAIL_ALIASES.get('').get(self.alias)
        if alias is None:
            return None

        size = alias.get('size')[0]
        url = None

        if instance:
            orig_url = instance.path.split('.')
            thb_url = '.'.join(orig_url) + f'.{size}x{size}_q85.{orig_url[-1]}'
            if default_storage.exists(thb_url):
                print("if")
                last_url = instance.url.split('.')
                url = '.'.join(last_url) + f'.{size}x{size}_q85.{last_url[-1]}'
            else:
                print('else')
                url = get_thumbnailer(instance)[self.alias].url

        if url == '' or url is None:
            return None

        request = self.context.get('request', None)
        if request is not None:
            return request.build_absolute_uri(url)

        return url


# field lang serializer
class JsonFieldSerializer(serializers.BaseSerializer):
    def to_representation(self, instance):
        language = self.context['request'].headers.get('Language')
        default_lang = Languages.objects.filter(default=True).first().code

        if not language:
            language = default_lang

        data = instance.get(language)

        if data is None or data == '':
            data = instance.get(default_lang)

        return data


# meta serializer
class MetaFieldSerializer(serializers.ModelSerializer):
    meta_keys = JsonFieldSerializer()
    meta_deck = JsonFieldSerializer()

    class Meta:
        model = MetaTags
        exclude = ['id']


# articles
class ArticleSerializer(serializers.ModelSerializer):
    title = JsonFieldSerializer()
    subtitle = JsonFieldSerializer()
    body = JsonFieldSerializer()
    created_date = serializers.DateField(format="%d.%m.%Y")
    image = ThumbnailSerializer(alias='prod_photo')
    author = serializers.ReadOnlyField(source='author.username')
    meta = MetaFieldSerializer()

    class Meta:
        model = Articles
        fields = '__all__'


# article detail serializer
class ArticleDetailSerializer(serializers.ModelSerializer):
    title = JsonFieldSerializer()
    subtitle = JsonFieldSerializer()
    body = JsonFieldSerializer()
    created_date = serializers.DateField(format="%d.%m.%Y")
    image = ThumbnailSerializer(alias='original')
    meta = MetaFieldSerializer()

    class Meta:
        model = Articles
        fields = '__all__'


# static information
class StaticInformationSerializer(serializers.ModelSerializer):
    title = JsonFieldSerializer()
    subtitle = JsonFieldSerializer()
    deskription = JsonFieldSerializer()
    about_us = JsonFieldSerializer()
    adres = JsonFieldSerializer()
    work_time = JsonFieldSerializer()
    logo_first = ThumbnailSerializer(alias='prod_photo')
    logo_second = ThumbnailSerializer(alias='prod_photo')

    class Meta:
        model = StaticInformation
        exclude = ['id']


# translation serializer
class TranslationSerializer(serializers.Serializer):
    def to_representation(self, instance):
        data = {}

        for item in instance:
            val = JsonFieldSerializer(item.value, context={'request': self.context.get('request')}).data
            key = str(item.group.sub_text) + '.' + str(item.key)
            data[key] = val

        return data


# langs serializer
class LangsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'


# parnters serializer
class PartnersSerializer(serializers.ModelSerializer):
    name = JsonFieldSerializer()
    deckription = JsonFieldSerializer()
    image = ThumbnailSerializer(alias='avatar')

    class Meta:
        model = Partners
        fields = '__all__'


# short apl serializer
class ShortApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShortApplications
        fields = '__all__'


# sevice serializer
class ServicesSerializer(serializers.ModelSerializer):
    title = JsonFieldSerializer()
    sub_title = JsonFieldSerializer()
    deckription = JsonFieldSerializer()
    image = ThumbnailSerializer(alias='product_img')
    meta = MetaFieldSerializer()

    class Meta:
        model = Services
        fields = '__all__'


# services simple serializer
class ServicesSimpleSerializer(serializers.ModelSerializer):
    title = JsonFieldSerializer()
    sub_title = JsonFieldSerializer()

    class Meta:
        model = Services
        fields = ['title', 'sub_title', 'slug']


# project serializer
class ProjectSerializer(serializers.ModelSerializer):
    title = JsonFieldSerializer()
    description = JsonFieldSerializer()
    meta = MetaFieldSerializer()
    services = ServicesSimpleSerializer(many=True)
    image_first = ThumbnailSerializer(alias='product_img')

    class Meta:
        model = Projects
        exclude = ['image_second']



# projects detal serializer
class ProjectsDetailSerializer(ProjectSerializer):
    class Meta:
        model = Projects
        fields = '__all__'



# reviews
class ReviewsSerializer(serializers.ModelSerializer):
    title = JsonFieldSerializer()
    text = JsonFieldSerializer()
    image = ThumbnailSerializer(alias='ten')
    subtitle = JsonFieldSerializer()


    class Meta:
        model = Reviews
        fields = '__all__'
