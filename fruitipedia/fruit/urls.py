from django.urls import path
from .views import create_fruit, fruit_details, fruit_edit, fruit_delete

urlpatterns = [
    path('create/', create_fruit, name='create-fruit'),
    path('<int:fruit_id>/details/', fruit_details, name='fruit_details'),
    path('<int:fruit_id>/edit/', fruit_edit, name='fruit_edit'),
    path('<int:fruit_id>/delete/', fruit_delete, name='fruit_delete')
]
