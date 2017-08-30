from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
import requests
import json
from django.http import JsonResponse
from django.shortcuts import render_to_response
import base64

def evaluation(request):
    if request.is_ajax() and request.method == 'POST':
        photo = request.POST['photo']
        photo = base64.b64encode(photo)
        print(photo)
        url = 'https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/a6935af8-f509-4e24-87b0-ab2b681cb482/url?iterationId=dd3054f7-b975-4943-abf3-7aeef817204c'
        headers = {
            'Prediction-Key': '58a0ad9c77734a45a6a992932e20b7bd',
            'Content-Type': 'application/octet-stream',
        }
        files = [('source', ('write.png', photo, 'application/octet-stream'))]
        r = requests.post(url, headers=headers, files=files)

        result = json.loads(r.content.decode("utf-8"))
        return HttpResponse(json.dumps({'result':result}))
    else:
        return HttpResponse(json.dumps({'result':False}))
