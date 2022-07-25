# I have created this file - Mahin H

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    # Get the text
    global params
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraSpaceRemover', 'off')

    # Check which checkbox is on
    if removepunc == "on":
        punctuations = '''.?!,;:/&^%$#@!~`--'"[]{}‘()“—'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To UpperCase', 'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == "on":
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}

    if removepunc != "on" and newlineremover != "on" and fullcaps != "on" and extraspaceremover != "on":
        return HttpResponse("Please select an option & try again!")

    return render(request, 'analyze.html', params)
