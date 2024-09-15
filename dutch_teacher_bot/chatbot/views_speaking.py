from django.shortcuts import render
from .chatgpt_api import get_response

def spreken_view(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        response = get_response(prompt)
        return render(request, 'chatbot/spreken.html', {'response': response})
    return render(request, 'chatbot/spreken.html')
