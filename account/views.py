from account.services.services import RegisterUserService
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


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
        result = self.register_user_service.create_user(user_data)
        if isinstance(result, tuple) and (result[0] is False):
            return Response({"error": result[1]}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message": result}, status=status.HTTP_201_CREATED)
