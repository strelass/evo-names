# -*- coding: utf-8 -*-
import os
from django.http import HttpResponse
from django.shortcuts import render
from evo_server.settings import ON_OPENSHIFT

if ON_OPENSHIFT:
    f = open(os.path.join(os.environ.get('DOCUMENT_ROOT', ''), 'epitets.txt'), 'r')
else:
    f = open("epitets.txt", 'r')
epitet_list = []
for line in f:
    epitet_list += [line.decode('cp1251')]
CONST_EPITET_SET = set(epitet_list)
f.close()

temp_set = CONST_EPITET_SET.copy()
name_epitet = {}


def index(request):
    if request.method == "POST":
        name = request.POST["name"]
        if name:
            if name not in name_epitet.keys():
                global temp_set
                name_epitet[name] = temp_set.pop()
                if len(temp_set) == 0:
                    temp_set |= CONST_EPITET_SET
            epitet = name_epitet[name]
            text = (u"Рад тебя видеть снова, %s %s!" % (epitet, name))
            return HttpResponse(
                text,
                content_type="text/plain"
            )
    context = {}
    return render(request, "index.html", context)
