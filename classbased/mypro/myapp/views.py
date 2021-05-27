from myapp.models import Contactus
from myapp.serializer import ContactusSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class SimpleApi(APIView):

    serializer_class=ContactusSerializer

    def get (self,request,*args,**kwargs):
        query_set =Contactus.objects.all()
        serialer=self.serializer_class(query_set,many=True)
        return Response(serialer.data,status=200)

    def post(self,request,*args,**kwargs):
        print(request.data)
        serialer = self.serializer_class(data=request.data)
        if serialer.is_valid(raise_exception=True):
            serialer.save()
            return Response(serialer.data)
        else:
           return Response(serialer.errors)


simple_api =SimpleApi.as_view()

# Method 1 (by using id in url)
class Simple_crud(APIView):

    serializer_class=ContactusSerializer

    def get_object(self,id):

        try:
            return Contactus.objects.get(id=id)
        except Contactus.DoesNotExist:
            return Response(status=404)

    def get(self,request,id):
        contacts = self.get_object(id)
        serializer=self.serializer_class(contacts)
        return Response(serializer.data)


    def put(self,request,id):
        contacts=self.get_object(id)
        serializer=self.serializer_class(contacts,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


    def delete(self,request,id):
        contacts=self.get_object(id)
        contacts.delete()
        return Response(status=204)


simple_crud =Simple_crud.as_view()


