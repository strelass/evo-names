from django.conf.urls import url
import mypackage.views

urlpatterns = [
    url(r'^', mypackage.views.index, name='home')
]
