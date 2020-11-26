from django.urls import path

from .import views

urlpatterns = [
    path('login/', views.login),
    path('display/',views.displaydetails),
    path('display/<id>',views.details,name = 'detail'),
    path('form/', views.displayform),
    path('displayfiles',views.displayfiles),
    path('mail/',views.email),
    path('session1/',views.session1,name='login'),
    path('getsession/',views.sessionshow,name='getsession'),
    path('api/',views.ListStudent.as_view()),
    path('<int:pk>/',views.DetailStudent.as_view()),
    path('contact/',views.ContactView.as_view())
    ]