from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_menu),
    path('<str:some_weapone>', views.get_info_about_type_of_weapone, name = 'weapon-name'),
    path('<int:some_smg>', views.get_info_about_some_smg_by_number),
    path('<str:some_smg>', views.get_info_about_some_smg, name = 'smg-name'),
]