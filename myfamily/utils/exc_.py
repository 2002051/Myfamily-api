from django.http import Http404

from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import Throttled
from rest_framework.exceptions import PermissionDenied
from rest_framework.exceptions import NotAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import set_rollback
from rest_framework.exceptions import APIException
class ExtraException(APIException):
    pass
def exception_handler(exc, context):
    if isinstance(exc, Http404):
        exc = exceptions.NotFound()
        exc.ret_code = 2001
    elif isinstance(exc, PermissionDenied):
        exc = exceptions.PermissionDenied()
        exc.ret_code = 2002
    elif isinstance(exc, (AuthenticationFailed, NotAuthenticated)):
        exc.ret_code = 2003
    elif isinstance(exc, Throttled):
        exc.ret_code = 2004
    elif isinstance(exc, ValidationError):
        exc.ret_code = 2005
    # ...

    if isinstance(exc, exceptions.APIException):
        headers = {}
        if getattr(exc, 'auth_header', None):
            headers['WWW-Authenticate'] = exc.auth_header
        if getattr(exc, 'wait', None):
            headers['Retry-After'] = '%d' % exc.wait
        # if isinstance(exc.detail, (list, dict)):
        #     data = exc.detail
        # else:
        #     exc_code = getattr(exc, 'ret_code', None) or -1
        #     data = {'code': exc_code, 'detail': exc.detail}
        exc_code = getattr(exc, 'ret_code', None) or -1
        data = {'code': exc_code, 'detail': exc.detail}
        set_rollback()
        return Response(data, status=exc.status_code, headers=headers)
    # return None
    data = {'code': -1, 'detail': str(exc)}
    return Response(data, status=500)
