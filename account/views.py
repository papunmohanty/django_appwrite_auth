from account.services.services import RegisterUserService
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.exceptions import RegisterUserException


class ResgisterUser(APIView):
    """
    View to register user
    """

    def __init__(self, *args, **kwargs):
        self.register_user_service = RegisterUserService()
        super().__init__(*args, **kwargs)

    def post(self, request):
        user_data = request.data
        print(f"User Data {user_data}")
        try:
            result = self.register_user_service.create_user(user_data)
        except RegisterUserException as err:
            raise RegisterUserException(err)
        return Response({"message": result}, status=status.HTTP_201_CREATED)
