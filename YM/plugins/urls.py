from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # your other routes here
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
