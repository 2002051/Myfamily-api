from django.contrib import admin

# Register your models here.
from myfamily import models

admin.site.site_title = "后台管理系统"
# 登录页导航条和首页导航条标题
admin.site.site_header = "台管理系统"
# 主页标题
admin.site.index_title = "欢迎登陆"


@admin.register(models.Album)
class DeviceAdmin(admin.ModelAdmin):
    # list_display = ["device_id", "douyin", "brand"]
    pass


@admin.register(models.Photo)
class DeviceAdmin(admin.ModelAdmin):
    # list_display = ["device_id", "douyin", "brand"]
    pass


@admin.register(models.Root)
class DeviceAdmin(admin.ModelAdmin):
    # list_display = ["device_id", "douyin", "brand"]
    pass


@admin.register(models.News)
class DeviceAdmin(admin.ModelAdmin):
    # list_display = ["device_id", "douyin", "brand"]
    pass
