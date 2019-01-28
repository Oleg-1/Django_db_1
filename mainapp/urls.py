from django.urls import path

import mainapp.views as controller

app_name = 'mainapp'

urlpatterns = [
    path('', controller.company_index, name='index'),
    path('<int:id>/', controller.company_view, name='view'),
]