from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def result(request):
    sentence = request.GET['sentence']

    nameList = sentence.split(',')

    return render(request, 'result.html',{'fulltext':sentence, 'count':len(nameList), 'nameList':nameList})    