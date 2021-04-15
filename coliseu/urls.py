from django.contrib import admin
from django.urls import path

from colis.views import home_view, coli_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('colis/<int:coli_id>', coli_detail_view),
]
