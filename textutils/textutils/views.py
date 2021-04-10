# i have created this file -- gaurav

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('Home')
    return render(request,'index.html')

def analyze(request):
    #get the text
    djtext = request.POST.get('text','default')

    #checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    charcount = request.POST.get('charcount','off')
    purpose1 = ''

    #check which checkbox is on
    if removepunc == 'on':
        analyzed = ''
        purpose1+= 'Removed Punctuations \n'
        purpose = purpose1
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params = {'purpose' : purpose,'analyzed_text': analyzed}
        djtext = analyzed

    if fullcaps == 'on':
        analyzed = ''
        purpose1 += 'changes to upper case\n'
        purpose = purpose1
        for char in djtext:
            analyzed+=char.upper()
        params = {'purpose' : purpose,'analyzed_text': analyzed}
        djtext = analyzed

    if newlineremover == 'on':
        analyzed = ''
        purpose1+='new line remover\n'
        purpose = purpose1
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed+=char
        params = {'purpose' : purpose,'analyzed_text': analyzed}
        djtext = analyzed

    if extraspaceremover == 'on':
        analyzed = ''
        purpose1+='Extra space remover'
        purpose = purpose1
        for index,char in enumerate(djtext):
            if not(djtext[index] == ' ' and djtext[index+1] == ' '):
                analyzed+=char
        params = {'purpose' : purpose,'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request,'analyze.html',params)
    # elif charcount == 'on':
    #     count = 0
    #     for char in djtext:
    #         if  char.isalpha():
    #             count+=1
    #     params = {'purpose' : 'No of character in thi sstring','analyzed_text': djtext,'count' : count}
    #     return render(request,'analyze.html',params)
    if removepunc != 'on' and extraspaceremover != 'on' and fullcaps != 'on' and newlineremover != 'on':
        return HttpResponse('Error')
    return render(request,'analyze.html',params)


def removepunc(request):
    djtext = request.GET.get('text','default')
    print(djtext)
    return HttpResponse('remove Punc')

def capfirst(request):
    return HttpResponse('Capitalize first')

def newlineremove(request):
    return HttpResponse('new line remove')

def spaceremove(request):
    return HttpResponse('space remove <a href = "/"> back </a>')

def charcount(request):
    return HttpResponse('char count')

def navigate(request):
    return HttpResponse('''<h1>hello gaurav</h1> <a href = "https://www.youtube.com/" ><h1>youtube</h1></a>
    <a href = "https://www.facebook.com/" ><h1>facebook</h1></a>
    <a href = "https://www.google.com/" ><h1>google</h1></a>
    <a href = "https://gmail.com/" ><h1>gmail</h1></a>
    <a href = "https://www.amazon.in/" ><h1>amazon</h1></a>''')

def about(request):
    return HttpResponse('about gaurav')