from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import HttpResponse
from rest_framework.views import exception_handler
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed

class MyResponse(APIView):
    def finalize_response(self, request, response, *args, **kwargs):
        response = super().finalize_response(request, response, *args, **kwargs)

        # 1.非正常返回
        if response.exception:
            return response

        # 2.正常数据返回
        response.data = {"code": 0, "data": response.data}
        return response
