import json
import facebook
from pprint import pprint
from myApp.applet.tokens_keys import *
from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


class SurveyApplet:
    def __init__(self):
        self.active = False
        self.access_token = access_token
        self.verify_token = verify_token
        self.outgoing_key = outgoing_key
        self.incoming_key = incoming_key
        self.post_message_url = post_message_url


def check_if_admin():
    pass


class AppletView(generic.View):
    def get(self, request, *args, **kwargs):
        if self.request.GET['hub.verify_token'] == verify_token:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return generic.View.dispatch(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        incoming_message = json.loads(self.request.body.decode('utf-8'))
        print("***************************************INCOMING***************************************\n")
        pprint(incoming_message)
        graph = facebook.GraphAPI(access_token=access_token)
        args = {'fields': 'roles'}
        page = graph.get_object('1758067134406535', **args)
        pprint(page)
        '''with open('outf.json', 'w') as f:
            json.dump(page, f)'''
        #incoming_message['access_code'] = MSURVEY_ACCESS_CODE
        if 'access_key' in incoming_message:
            if incoming_message['access_key'] == incoming_message:
                pass
            else:
                pass
        else:
            pass
        return HttpResponse()

