from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from .serializers import CipherSerializer
from string import ascii_lowercase
import json


class CipherView(GenericAPIView):
    """
    This view handles returning the ciphered message and storing the result on disk
    """

    def post(self, request):
        serializer = CipherSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=500)

        shift = serializer.validated_data['shift']
        message = serializer.validated_data['message']

        trans = str.maketrans(ascii_lowercase, ascii_lowercase[shift:] + ascii_lowercase[:shift])

        response_data = {
            'EncodedMessage': message.lower().translate(trans)
        }

        file = open('translations.txt', 'w')
        file.write(json.dumps(response_data))
        file.close()
        return Response(response_data)

