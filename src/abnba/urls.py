import abnba.core.urls


urlpatterns = abnba.core.urls.get_patterns(
    (r'^host/', 'abnba.host.app')
)
