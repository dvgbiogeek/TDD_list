import requests
import sys
from accounts.models import ListUser

class PersonaAuthenticationBackend(object):
    
    def authenticate(self):
        # Send the assertion to Mozilla's verifier service.
        data = {'assertion': assertion, 'audience': 'localhost'}
        print('sending to mozilla', data, file=sys.stderr)
        resp = requests.post('http://verifier.login.persona.org/verify', data=data)
        print('got', resp.content, file=sys.stderr)

        # Did the verifier respond?
        if resp.ok:
            # Parse the response
            verification_data = resp.json()
            if verification_data['status'] =='okay':
                email.verification_data['email']
                try:
                    return self.get_user(email)
                except ListUser.DoesNotExist:
                    return ListUser.objects.create(email=email)

    def get_user(self, email):
        return ListUser.objects.get(email=email)
