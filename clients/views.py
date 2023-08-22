

from rest_framework import status
from rest_framework.response import Response
from clients.models import Client
from drfutil.authentication_class import AsyncAuthentication, AsyncIsAuthenticated
from drfutil.views import AsyncAPIView

class ClientsView(AsyncAPIView):
    authentication_classes = [AsyncAuthentication, ]
    permission_classes = [AsyncIsAuthenticated, ]

    async def get(self, request):
        data = Client.objects.filter().values()
        return Response(data, status=status.HTTP_200_OK)
    
    async def post(self, request):
        if not request.data:
            return Response({"error": "Invalid request data"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            first_name = request.data["first_name"]
            last_name = request.data["last_name"]
            email = request.data["email"]

            await Client.objects.acreate(
                first_name = first_name,
                last_name = last_name,
                email = email
            )
            return Response({"message": "Client successfully created!"}, status=status.HTTP_201_CREATED)
        
        except Exception as e:
            print("error: ", e)
            return Response({"error": "Could not create client."}, status=status.HTTP_400_BAD_REQUEST)
