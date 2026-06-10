from django.urls import path
from course_app.views import *

urlpatterns =[
    path('', course_view, name='course_view'),
    path('add-course/', course_add, name='course_add'),
    path('edit-course/<str:c_id>/', course_edit, name='course_edit'),
    path('delete-course/<str:c_id>/', course_delete, name='course_delete'),
]
