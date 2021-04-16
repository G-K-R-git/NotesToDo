from rest_framework import serializers
from rest_framework.fields import ListField, ChoiceField, BooleanField
from rest_framework.serializers import Serializer

from notes.models import Note


class NoteListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['title', 'date_complete', 'urgent', 'status', 'public']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class NoteEditorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        read_only_fields = ['date_add', 'author', ]


class NotePutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'


class QuerySerializer(Serializer):
    status = ListField(child=ChoiceField(choices=Note.STATUSES), required=False)
    importance = BooleanField()
    public = BooleanField()