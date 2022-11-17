from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls
from django.apps import apps
from django.conf.urls import include, re_path

admin.site.site_header = 'Medose Admin'                 # default: "Django Administration"
admin.site.index_title = 'Medose Data'                  # default: "Site administration"
admin.site.site_title = 'All tables'                    # default: "Django site admin"

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path("docs/", include_docs_urls(title='MEDOSE API', description="All medose API's collection")),
    path('dashboard/', include('doctor.urls', namespace="doctor")),
    path('my-dashboard/', include('patient.urls', namespace="patient")),


    # The Django admin is not officially supported; expect breakage.
    # Nonetheless, it's often useful for debugging.

    path('shop/', include(apps.get_app_config('oscar').urls[0])),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]