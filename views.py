# -*- coding: utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, login, logout

import os.path as op
import uuid
import logging

from settings import *

def custom_proc(request):
    return {
        'app_title': 'Empty django project',
        'app_name': 'root',
        'user': request.session.get('user', None),
        'ip_address': request.META['REMOTE_ADDR'],
        'ajax': request.GET.get('ajax', 0)
    }

def index(request):
    message = ''
    t = loader.get_template('default.html')
    c = RequestContext(
        request,
            {
            'message': message,
            },
        processors=[custom_proc]
    )
    return HttpResponse(t.render(c))

def upload(request):
    path = op.join(
        UPLOAD_ROOT, str(uuid.uuid1()) + '_' +
                     op.basename(request.POST.get('file_name', '').lower())
    )
    f = request.FILES['file']
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return HttpResponseRedirect('/')
