# -*- coding: utf-8 -*-
# __author__ = "yw"
"""
# Serializers用于定义API的表现形式，如：返回那些字段、返回怎样的格式等。
# 这里序列化Django自带的User和Group。
# 创建数据序列化
"""
# from django.contrib.auth.models import User,Group
from rest_framework import serializers
from api.models import User,Group

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')