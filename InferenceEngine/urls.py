from django.conf.urls import url,include
from InferenceEngine import views,models
from DSSaaS import settings
from django.conf.urls.static import static


urlpatterns = [
	url(r'^index', views.index, name='index'),
	url(r'^REST-API', views.processSingleReq, name='processSingleReq'),
	url('upload/', views.create_profile, name = 'create'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)