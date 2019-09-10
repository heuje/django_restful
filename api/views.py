from django.shortcuts import render
# from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from api.serializers import UserSerializer,GroupSerializer
from api.models import User,Group

# Create your views here.
"""
默认导入的就有render，用来响应调用之后的http的response。
创建视图：
    视图用于如何向用户展示数据，展示那些数据。比如：用户查询User信息或查询Group信息，那么程序内部要定义好怎么去查询。
    在Django REST framework中，ViewSets用于定义视图的展现形式，例如返回那些内容，需要做哪些权限处理。
"""
class UserViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a user instance.

        list:
            Return all users,ordered by most recently joined.

        create:
            Create a new user.

        delete:
            Remove a existing user.

        partial_update:
            Update one or more fields on a existing user.

        update:
            Update a user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
        retrieve:
            Return a group instance.

        list:
            Return all groups,ordered by most recently joined.

        create:
            Create a new group.

        delete:
            Remove a existing group.

        partial_update:
            Update one or more fields on a existing group.

        update:
            Update a group.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
