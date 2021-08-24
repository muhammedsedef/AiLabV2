from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>/document-stats', views.stats_algorithms, name='stats_algorithms'),
    path('<int:pk>/document-stats/<str:algorithm>', views.apply_stats_algorithm,
         name='apply_stats_algorithm'),
    path('<int:project_pk>/document-stats/<str:algorithm>/<int:report_pk>', views.view_stats_report, name='view_stats_report'),


]

