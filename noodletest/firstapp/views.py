from hashlib import new
from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from django.views.generic import TemplateView
from rest_framework.response import Response
import json
import uuid

class RegisterUser(viewsets.ModelViewSet):
    queryset = Users.objects.all()

    def post(self, request, *args, **kwargs):
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        if not "name" in body or not "email" in body:
            return Response(400)

        user = Users.objects.create(id=str(uuid.uuid4()), name=body.get("name"), email=body.get("email"))

        return Response({"user_id": user.id})


class GetNewsletters(viewsets.ModelViewSet):
    queryset = Newsletter.objects.all()

    def get(self, request, *args, **kwargs):
        categories = kwargs.get("cat")
        # categories = request.GET.get('categories')
        print("categories", categories)
        newsletters = Newsletter.objects.filter(category__name__in=categories)

        return_data = {"newsletters": []}
        data = {}
        if len(newsletters) == 0:
            return Response(return_data)
        for nl in newsletters:
            if nl.category.name in data:
                data[nl.category.name].append({"newsletter_id": nl.id, "title": nl.title})
            else:
                data[nl.category.name] = [{"newsletter_id": nl.id, "title": nl.title}]
        ret_list = []
        for i in data:
            ret_list.append(data[i])
        return_data["newsletters"] = ret_list

        return Response(return_data)

