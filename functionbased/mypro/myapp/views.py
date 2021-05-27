from rest_framework import status
from rest_framework.decorators import api_view
from myapp.models import Contactus
from myapp.serializer import ContactusSerializer
from rest_framework.response import Response


@api_view(['GET','POST',''])
def Contact_list(request):
    if request.method=='GET':
        queryset=Contactus.objects.all()
        serializer=ContactusSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        print(request.data)
        serializer=ContactusSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)



@api_view(['GET', 'PUT', 'DELETE'])
def Contact_details(request,pk):
    try:
        queryset=Contactus.objects.get(pk=pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method=='GET':
        serializer=ContactusSerializer(queryset)
        return Response(serializer.data)

    elif request.method=='PUT':
        serializer=ContactusSerializer(queryset,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    elif request.method=="DELETE":
        queryset.delete()



