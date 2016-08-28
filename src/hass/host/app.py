
import hass.core.application

import hass.host.config
import hass.host.views


class HostApplication(hass.core.application.Application):

    name = hass.host.config.HostConfig.name
    app_name = 'host'

    views = [
        (hass.host.views.MainView, r'^main.html$', 'main',),
    ]


application = HostApplication()
