from rest_framework import serializers
from myfamily import models

url = "http://127.0.0.1:8000/media/"


class AlbumSer(serializers.ModelSerializer):
    cover = serializers.CharField()

    class Meta:
        model = models.Album
        # fields = '__all__'


        exclude = ["password"]


# class SearchAlbumSer(serializers.Serializer):
#     # imgurl = serializers.SerializerMethodField()
#     # cover = serializers.SerializerMethodField()
#     # cover = serializers.ImageField()
#     title = serializers.CharField()
#     cover = serializers.CharField()
#     create_time = serializers.DateTimeField()


class PhotoSer(serializers.ModelSerializer):
    class Meta:
        model = models.Photo
        fields = '__all__'
