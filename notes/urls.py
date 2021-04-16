from django.urls import path

from . import views

app_name = 'notes'
urlpatterns = [
    path('note/', views.NotesToDo.as_view(), name='all notes'),
    path('note/<int:note_id>/', views.NoteDetailView.as_view(), name='one note'),
    path('note/add/', views.NoteEditorView.as_view(), name='add note'),
    path('note/<int:note_id>/save/', views.NoteEditorView.as_view(), name='save note'),
    path('note/about/', views.About.as_view(), name='about'),
    path('note/completed', views.CompletedView.as_view(), name='Completed tasks'),
]