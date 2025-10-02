from django.contrib import admin
from django.urls import path, include
from django.conf import settings                
from django.conf.urls.static import static    

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
]

# --- 3. เพิ่มเงื่อนไขนี้เข้าไปที่ท้ายไฟล์ ---
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)