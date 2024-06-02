from rest_framework.authentication import BaseAuthentication


class LoginAuth(BaseAuthentication):
    def __init__(self, user_method: list):
        self.user_method = user_method

    def authenticate(self, request):
        if request.method in self.user_method:
            print("无需登录")
            return
        # 校验用户是否登录，如果登录则更新数据库中的token

        return 1, 2
