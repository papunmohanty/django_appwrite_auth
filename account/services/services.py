from appwrite.client import Client
from appwrite.id import ID
from appwrite.services.users import Users
from django.conf import settings

client = (
    Client()
    .set_endpoint(settings.APPWRITE_CONFIG.get("ENDPOINT_URL"))
    .set_project(settings.APPWRITE_CONFIG.get("PROJECT_ID"))
    .set_key(settings.APPWRITE_CONFIG.get("SECRET_KEY"))
)


class RegisterUserService:
    """
    Class to register various types of users
    """

    def create_user(self, user_data):
        users = Users(client)
        try:
            result = users.create(
                user_id=ID.unique(),
                email=user_data.get("email"),
                phone=user_data.get("phone"),
                password=user_data.get("password"),
                name=user_data.get("name"),
            )
            print(f"Result response {result}")
        except Exception as err:
            print(f"Error creating user in appwrite {str(err)}")
            return False, str(err)
        return result

    def create_super_user():
        pass
