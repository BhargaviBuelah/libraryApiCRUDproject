from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer,UserRegistrationSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import requires_csrf_token
import io
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate


'''
@csrf_exempt
@requires_csrf_token

def book_detail(request ,pk):
    bk = Book.objects.get(id=pk)
    #print(bk)
    serializer = BookSerializer(bk)
    #print(serializer)
    #print(serializer.data)
    json_data =JSONRenderer().render(serializer.data)
    
    #print(json_data)
   
    return HttpResponse(json_data,content_type='application/json')


def book_list(request):
    if request.method == "GET":
        bk = Book.objects.all()
        serializer = BookSerializer(bk,many=True)
        json_data =JSONRenderer().render(serializer. data)
    
        return HttpResponse(json_data,content_type='application/json')
    elif request.method =="POST":
        json_data = request.body
        stream = io.BytesIO(json_data)
        print(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = BookSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'DAta Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data,content_type='application/json')
@csrf_exempt
def book_create(request):
    if request.method == "POST":
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata =JSONParser().parse(stream)
        serializer =BookSerializer( data=pythondata )
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'DAta Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data,content_type='application/json')

@csrf_exempt
def book_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream =io.BytesIO(json_data)
        pythondata =JSONParser().parse(stream)
        id = pythondata.get('id',None)
        if id is not None:
            bk= Book.objects.get(id=id)
            serializer =BookSerializer(bk)
            json_data =JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        bk= Book.objects.all()
        serializer=BookSerializer(bk,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = BookSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        bk = Book.objects.get(id=id)
        # serializer =BookSerializer(bk, data=pythondata)
        # Partial Update - all data not requird
        serializer = BookSerializer(bk, data=pythondata, partial=True)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'Data Updated!!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')
    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id=pythondata.get('id')
        bk =Book.objects.get(id=id)
        bk.delete()
        res = {'msg' : 'Data Deleted!!'}
        #json_data = JSONRenderer().render(res)
        #return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res, safe=False)
'''
'''
class BookDetailView(APIView):
    def get(self,request,format=None):
        bk = Book.objects.get(id=pk)
        #print(bk)
        serializer = BookSerializer(bk)
        #print(serializer)
        #print(serializer.data)
        json_data =JSONRenderer().render(serializer. data)
        #print(json_data)
        return HttpResponse(json_data,content_type='application/json')
'''
class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer =UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception = True):
            user= serializer.save()
            return Response({'msg':'Registration Successful'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception =True):
            email= serializer.data.get('email')
            password= serializer.data.get('password')
            user = authenticate(email=email,password=password)
            if user is not None:
                return Response({'msg':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}},status=status.HTTP_404_NOT_FOUND)
