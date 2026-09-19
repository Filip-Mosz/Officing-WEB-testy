from django.http import JsonResponse

def hello(request):
    return JsonResponse({
        'Message': 'Officing says hello'
    })