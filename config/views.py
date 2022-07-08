from django.shortcuts import render
from rest_framework.views import APIView

class Main(APIView):
    def get(self, request):
        print("GET으로 호출!!")
        return render(request, 'starstagram/main.html')

    def post(self, request):
        print("POST으로 호출!!")
        return render(request, 'starstagram/main.html')