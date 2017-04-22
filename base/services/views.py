from rest_framework.decorators import api_view
from rest_framework.response import Response
from services.models import User


@api_view(['GET', 'PUT', 'DELETE'])
def ulas(request, uid):
    """
    Get the instance of ULA
    """
    if request.method == 'GET':  
        return Response("<ula/>")

    elif request.method == 'POST':
        return Response("<ula/>",200)
