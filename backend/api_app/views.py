from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict

from api_app.models import Book
from api_app.serializers import BookSerializer


@api_view(["GET"])
def api_home(request, *args, **kwargs):
    model_data = Book.objects.all().first()
    data = {}
    if model_data:
        data = BookSerializer(model_data).data
    return Response(data)
