from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^applieddata2.csv', views.applied),
    #url(r'^admitteddata2.csv', views.admitted),
    #url(r'^SIReddata2.csv', views.SIRed),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)