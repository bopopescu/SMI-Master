from rest_framework import serializers
from .models import Group
from .models import GroupType


class GroupTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupType
        fields = (
            'name',
            'url'
        )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = (
            'name',
            'type',
            'url'
        )
