from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pick/', views.pick, name='pick'),
    path('addplan/', views.add_plan, name='add-plan'),
    path('plans/', views.PlanListView.as_view(), name='plans'),
    path('plan/<int:pk>', views.PlanDetailView.as_view(), name='plan-detail'),
    path('locations/', views.LocationListView.as_view(), name='locations'),
    path('location/<int:pk>', views.LocationDetailView.as_view(), name='location-detail'),
]