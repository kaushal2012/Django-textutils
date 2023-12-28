import string
from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def analyze(request):
    djtext = request.GET.get('text', 'default')

    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('fullcaps', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    charcounter = request.GET.get('charcounter', 'off')

    if removepunc == 'on':
        punctuations = string.punctuation
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Remove punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremover == 'on':
        analyzed = ""
        for char in djtext:
            if char != '\n':
                analyzed = analyzed + char

        params = {'purpose': 'Remove New Lines', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif charcounter == 'on':
        count = 0
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == ' '):
                count = count + 1

        analyzed = f'Total number of Characters:{count}'

        params = {'purpose': 'Character Counter', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse('Error')
