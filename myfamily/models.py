from django.db import models


class ActiveBaseModel(models.Model):
    # 抽象类 。可以实现逻辑删除和物理删除
    active = models.SmallIntegerField(verbose_name="状态", default=1, choices=((0, "逻辑删除"), (1, "使用中")))

    class Meta:
        abstract = True


# Create your models here.

class Album(ActiveBaseModel):
    """相册"""
    title = models.CharField(verbose_name="标题", max_length=128)
    cover = models.ImageField(verbose_name="封面", upload_to="cover")
    password = models.CharField(verbose_name="密码",max_length=256,default="88888888")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)


class Photo(ActiveBaseModel):
    """照片"""
    url = models.ImageField(verbose_name="图片地址", upload_to="photo")
    album = models.ForeignKey(verbose_name="所属相册", to="Album", on_delete=models.CASCADE)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)


class News(ActiveBaseModel):
    """公告"""
    title = models.CharField(verbose_name="标题", max_length=128)
    author = models.CharField(verbose_name="作者", max_length=128)
    content = models.TextField(verbose_name="正文内容")
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)


class Root(ActiveBaseModel):
    """管理员"""
    nickname = models.CharField(verbose_name="昵称", max_length=128)
    username = models.CharField(verbose_name="用户名", max_length=128)
    password = models.CharField(verbose_name="密码", max_length=256)
    token = models.CharField(verbose_name="令牌", max_length=128)


# class Config(ActiveBaseModel):
#     """全局配置"""
#     pass
