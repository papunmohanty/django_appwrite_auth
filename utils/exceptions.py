from rest_framework import status
from rest_framework.exceptions import APIException


class RegisterUserException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Bad request while creating user"
