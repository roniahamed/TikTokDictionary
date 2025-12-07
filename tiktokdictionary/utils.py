import requests
from django.conf import settings




def verify_recaptcha(token):

    recaptcha_secret_key = settings.RECAPTCHA_SECRET_KEY
    recaptcha_url = 'https://www.google.com/recaptcha/api/siteverify'

    data = {
        'secret': recaptcha_secret_key,
        'response': token 
    }

    response = requests.post(recaptcha_url, data=data)

    result = response.json()

    return result.get('success', False)


