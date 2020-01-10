from django.conf.urls import url
from Resume import views

app_name = 'Resume'

urlpatterns = [
    url(r'form/',views.post_form,name='form'),
    # url(r'pdf/',views.GeneratePDF.as_view(),name='pdf'),
]
