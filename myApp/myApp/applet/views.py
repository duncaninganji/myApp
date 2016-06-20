from django.shortcuts import render
#import json, requests, random, re
from pprint import pprint

from django.views import generic
from django.http.response import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

PAGE_ACCESS_TOKEN = "EAAMsc7GwjFIBAAVVDy1A3wiIP4rEysB5djUFi8JL22dW3txTH9" \
                    "kmJWRVnumiv63BcljlznZCjZCIcpZCAmVIPqk3evgNTvmZC" \
                    "SzYudHcKPUs83F4wKxVGpOaaYXvlC2NLIGaTgKZBNysNG8Mb1UW9HZBmJJRZBAB4lcbiFpOv2ukQZDZD"
VERIFY_TOKEN = "2318934571"
post_message_url = 'https://graph.facebook.com/v2.6/me/messages?access_token=%s' % PAGE_ACCESS_TOKEN


class AppletView(generic.View):
    def get(self):
        if self.request.GET['hub.verify_token'] == VERIFY_TOKEN:
            return HttpResponse(self.request.GET['hub.challenge'])
        else:
            return HttpResponse('Error, invalid token')

