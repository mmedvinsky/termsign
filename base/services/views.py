from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from services.models import Client
from services.models import User
from services.termsign import TermSign


@api_view(['PUT', 'POST'])
def clientWrites(request):
    if request.method == 'PUT':  
        #
        # Return current client information.
        #
        return Response("<ula/>")

    elif request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            
            client = Client(name=data["client"]["name"])
            user = User(name=data["user"]["name"], email=data["user"]["email"], password=data["user"]["password"])
            # Register client 
            termSign = TermSign.instance()
            client = termSign.registerClient(client);
            user = termSign.registerUser(client, user)
            return Response({"client" : {"id": client.id, "name" : client.name}, 
                                 "user" : {"id": user.id, "name" : user.name}}, status=200)
        except ValueError: 
            return Response({'error': 'E_RegisterClient'}, status=403)
        except: 
            return Response({'error': 'E_RegisterClient'}, status=404)

@api_view(['GET'])         
def clientRead(request, cid):
    if request.method == 'GET':  
        try:
            termSign = TermSign.instance()
            client = termSign.getClientById(cid)
            return Response({"client" : {"id": client.id, "name" : client.name }}, status=200)
        except ValueError: 
            return Response({'error': 'E_RegisterClient'}, status=403)
        except: 
            return Response({'error': 'E_RegisterClient'}, status=404)
            

@api_view(['GET', 'PUT', 'DELETE'])
def ulas(request, uid):
    if request.method == 'GET':  
        return Response("<ula/>")

    elif request.method == 'POST':
        return Response("<ula/>",200)
