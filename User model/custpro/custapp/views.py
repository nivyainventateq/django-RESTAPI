
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer
from .serializers import CustomerUserSerializers


class User_API(APIView):
    def get(self,request,*args,**kwargs):
        queryset=Customer.objects.all()
        serializer=CustomerUserSerializers(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer=CustomerUserSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


user_api=User_API.as_view()



class User_crud(APIView):
    serializer_class = CustomerUserSerializers
    def get_object(self,id):
        try:
            return Customer.objects.get(id=id)
        except Customer.DoesNotExist:
            return Response(status=404)

    def get(self,request,id):
        exmp = self.get_object(id)
        serializer=self.serializer_class(exmp)
        return Response(serializer.data)

    def put(self,request,id):
        print(request.data)
        exmp=self.get_object(id)
        serializer=self.serializer_class(exmp,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,request,id):
        exmp=self.get_object(id)
        exmp.delete()
        return Response(status=204)

user_crud =User_crud.as_view()