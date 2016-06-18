# -*- coding: utf-8 -*-
import os
from django.http import HttpResponse
from django.shortcuts import render
from evo_server.settings import ON_OPENSHIFT

if ON_OPENSHIFT:
    f = open(os.path.join(os.environ.get('OPENSHIFT_REPO_DIR', ''), "epitets.txt"), 'r')
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
            global name_epitet
            if name not in name_epitet.keys():
                global temp_set
                if len(temp_set) == 0:
                    temp_set |= CONST_EPITET_SET
                name_epitet[name] = temp_set.pop()
            epitet = name_epitet[name]
            text = (u"Рад тебя видеть снова, %s %s!" % (epitet, name))
            return HttpResponse(
                text,
                content_type="text/plain"
            )
    context = {}
    return render(request, "index.html", context)
