from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.exceptions import APIException
from myfamily.utils.auth_ import LoginAuth
from myfamily.utils.ser_ import AlbumSer, PhotoSer
from myfamily.utils.res_ import MyResponse
from myfamily.utils.fil_ import FilterByAlbum
from myfamily import models
from rest_framework.pagination import LimitOffsetPagination


def nb(cls, user_method):
    def inner():
        obj = cls(user_method)
        return obj

    return inner


# Create your views here.
class AlbumView(MyResponse, ModelViewSet):
    """获取相册"""
    authentication_classes = [nb(LoginAuth, ["GET"])]  # get请求不需要执行登录校验逻辑
    queryset = models.Album.objects.filter(active=1).all()
    serializer_class = AlbumSer
    # filter_backends = []


class PhotoView(MyResponse, ModelViewSet):
    """获取照片"""
    authentication_classes = [nb(LoginAuth, ["GET"])]  # get请求不需要执行登录校验逻辑
    queryset = models.Photo.objects.filter(active=1).all()
    serializer_class = PhotoSer
    filter_backends = [FilterByAlbum]


class NewView(MyResponse, APIView):
    """获取公告"""


class LoginView(MyResponse, APIView):
    """登录视图"""
    pass


class SearchAlbum(MyResponse, APIView):
    """搜索相册"""

    def get(self, request):
        kw = request.query_params.get("kw", "")

        if kw == "":
            queryset = models.Album.objects.all()
        else:
            queryset = models.Album.objects.filter(title__contains=kw).all()
        ser = AlbumSer(instance=queryset, many=True)
        # 将 ImageFieldFile 对象转换为字符串

        return Response(ser.data)


class UnlockAlbum(MyResponse, APIView):
    """解锁相册"""

    def post(self, request):
        print("request.data",request.data)
        album_id = request.data.get("album_id")
        password = request.data.get("password")
        instance = models.Album.objects.filter(id=album_id,password=password).exists()
        if not instance:
            raise APIException("校验失败，密码错误！")
        return Response("校验成功")
