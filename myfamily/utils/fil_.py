from rest_framework.filters import BaseFilterBackend
from rest_framework.exceptions import APIException
from myfamily import models
class FilterException(APIException):
    pass

class FilterByAlbum(BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        album_id = request.query_params.get("album","")
        print(album_id)
        try:
            album_id = int(album_id)
        except:
            raise FilterException("缺少album参数，或传album_id不为整数")
        instance = models.Album.objects.filter(id=album_id).first()
        print("qu",instance)
        if not instance:
            raise FilterException("相册不存在")


        return queryset.filter(album_id=instance.id)
