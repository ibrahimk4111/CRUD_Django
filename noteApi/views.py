from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializer import noteSerializer
from django.shortcuts import render


# getting all datas from database
@api_view(['GET'])
def dbNotes(request):
    notes = Note.objects.all()
    serializer = noteSerializer(notes, many=True)
    return Response(serializer.data)


# Get a single data from database
@api_view(['GET'])
def dbNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = noteSerializer(note, many=False)
    return Response(serializer.data)


# create a single data from database
@api_view(['POST'])
def createNote(request):
    data = request.data
    serializer = noteSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response("success")
    
    return Response("error")



# create a single data from database
@api_view(['PUT'])
def updateNote(request, pk):
    updateNote = Note.objects.get(id=pk)
    # catching a single object and putting data into itself
    serializer = noteSerializer(updateNote, data=request.data)
    if serializer.is_valid():
        serializer.save()
    
    return Response(serializer.data)


# Delete a single data from database
@api_view(['DELETE'])
def deleteNote(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted")



