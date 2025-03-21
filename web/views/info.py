from django.http import JsonResponse

def client_info_view(request):
    return JsonResponse({
        'status': 'success',
        'data': {
            'summary': request.client_info.summary(),
            'full_info': request.client_info.full_info()  # 根据隐私政策开放
        }
    })