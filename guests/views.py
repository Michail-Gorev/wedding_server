import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Guest


@csrf_exempt
def save_guest(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            Guest.objects.create(
                name=data.get('name'),
                phone=data.get('phone'),
                alcohol=data.get('alcohol'),
                custom_alcohol=data.get('customAlcohol', ''),
                hot=data.get('hot'),
                music=data.get('music'),
                car=data.get('car') == 'true',
                comment=data.get('comment', '')
            )
            return JsonResponse({'status': 'success', 'message': 'Гость успешно добавлен'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Метод не разрешен'}, status=405)
