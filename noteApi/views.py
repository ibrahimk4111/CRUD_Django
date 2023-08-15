from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Note
from .serializer import noteSerializer
from django.shortcuts import render


# def reactView(request):
#     return render(request, "index.html")

@api_view(['GET'])
# Create your views here.
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]
    return Response(routes)

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
    newNote = Note.objects.create(
        body = data['body']
    )
    serializer = noteSerializer(newNote, many=False)
    return Response(serializer.data)



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



