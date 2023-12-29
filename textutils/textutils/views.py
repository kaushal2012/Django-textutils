import string
# from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def analyze(request):
    input_text = request.POST.get('text', 'default')

    remove_punctuation = request.POST.get('removepunc', 'off')
    upper_case = request.POST.get('fullcaps', 'off')
    newline_remover = request.POST.get('newlineremover', 'off')
    character_counter = request.POST.get('charcounter', 'off')

    analyzed = input_text
    purposes = []

    if remove_punctuation == 'on':
        punctuations = string.punctuation
        analyzed = ''.join([char for char in analyzed if char not in punctuations])
        purposes.append('Removed Punctuations')

    if upper_case == 'on':
        analyzed = analyzed.upper()
        purposes.append('Changed to Uppercase')

    if newline_remover == 'on':
        analyzed = ''.join([char for char in analyzed if char != '\n' and char != '\r'])
        purposes.append('Removed New Lines')

    if character_counter == 'on':
        count = len(analyzed)
        purposes.append(f'Character Counter: {count}')

    params = {'purposes': purposes, 'analyzed_text': analyzed}
    return render(request, 'analyze.html', params)
