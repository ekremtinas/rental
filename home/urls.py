from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name="home" ),
    path('my_rentals', views.my_rentals,name="my_rentals" ),
    path('models_by_brand/<int:brand_id>', views.models_by_brand ),
    path('rental', views.rental ),
]
