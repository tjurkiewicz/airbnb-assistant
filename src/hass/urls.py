import django.conf
import django.conf.urls.static

import hass.core.urls


urlpatterns = list(hass.core.urls.get_patterns(
    (r'^host/', 'hass.host.app'),
))  + django.conf.urls.static.static(django.conf.settings.STATIC_URL, document_root=django.conf.settings.STATIC_ROOT)
