# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404   # Standard Django error page
from django.contrib.auth.models import User

from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse

from brands.models import Info
from brands.serializers import InfoSerializer, UserSerializer
from brands.permissions import IsOwnerOrReadOnly



@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'info': reverse('info-list', request=request, format=format)
    })



class InfoViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retreive`,
    `update` and `destroy` actions.
    """
    queryset = Info.objects.all()
    serializer_class = InfoSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)



class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
