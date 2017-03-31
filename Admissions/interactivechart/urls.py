from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
 
    # url(r'^static/csv/applieddata2.csv', views.applied),
    # url(r'^static/admitteddata2.csv', views.admitted),
    # url(r'^static/SIReddata2.csv', views.SIRed)
    # url(r'^$', TemplateView.as_view(template_name='fiterTest.html'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)