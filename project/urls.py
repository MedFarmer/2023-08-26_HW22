from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import home, delete, students, StudentsCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('students/', students, name='students'),
    path('students/add/', StudentsCreate.as_view(), name='add'),
    path('delete/<int:id>', delete, name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
