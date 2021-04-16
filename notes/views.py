from django.db.models import Q
from django.shortcuts import render
from django.views import View
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from NotesToDo import settings
from notes.models import Note
from serializers import NoteListSerializer, NoteSerializer, NoteEditorSerializer, NotePutSerializer, QuerySerializer


class NotesToDo(APIView, LimitOffsetPagination):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        notes = Note.objects.all().order_by('date_complete', 'urgent').select_related('author')

        query_params = QuerySerializer(data=request.query_params)
        print('params here', query_params)
        if query_params.is_valid():
            if query_params.data.get('status'):
                q_status = Q()
                for stat in query_params.data['status']:
                    q_status |= Q(status=stat)
                notes = notes.filter(q_status)

            if 'importance' in request.query_params:
                notes = notes.filter(urgent=query_params.data['importance'])

            if 'public' in request.query_params:
                notes = notes.filter(public=query_params.data['public'])

        else:
            return Response(query_params.errors, status=status.HTTP_400_BAD_REQUEST)

        results = self.paginate_queryset(notes, request, view=self)
        serialized = NoteListSerializer(results, many=True)
        return self.get_paginated_response(serialized.data)


class NoteDetailView(APIView):
    permission_classes = (IsAuthenticated,)
    def check_existance(self, note_id):
        note = Note.objects.filter(pk=note_id).first()
        if not note:
            raise NotFound('No such note')
        else:
            return note

    def get(self, request, note_id):
        note = self.check_existance(note_id)
        serialized = NoteSerializer(note)
        return Response(serialized.data)

    def put(self, request, note_id):
        note = self.check_existance(note_id)
        new_note = NotePutSerializer(note, data=request.data, partial=True)
        if new_note.is_valid():
            new_note.save()
            return Response(new_note.data, HTTP_201_CREATED)
        else:
            return Response(new_note.errors, status=HTTP_400_BAD_REQUEST)

    def patch(self, request, note_id):
        note = self.check_existance(note_id)
        new_note = NoteEditorSerializer(note, data=request.data, partial=True)
        if new_note.is_valid():
            new_note.save()
            return Response(new_note.data, status=status.HTTP_200_OK)
        else:
            return Response(new_note.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, note_id):
        note = self.check_existance(note_id)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NoteEditorView(APIView):
    permission_classes = (IsAuthenticated, )

    def post(self, request):
        new_note = NoteEditorSerializer(data=request.data)

        if new_note.is_valid():
            new_note.save(author=request.user)
            return Response(new_note.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_note.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        notes = Note.objects.all()
        serialized = NoteListSerializer(notes, many=True)
        return Response(serialized.data)


class About(View):
    def get(self, request):
        context = {'SERVER_VERSION': settings.SERVER_VERSION}
        return render(request, 'about.html', context)


class CompletedView(APIView):
    def get(self, request):
        notes = Note.objects.all().filter(status=0).order_by('date_complete')
        serialized = NoteListSerializer(notes, many=True)
        return Response(serialized.data)
