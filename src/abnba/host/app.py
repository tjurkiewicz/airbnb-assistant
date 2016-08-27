
import abnba.core.application

import abnba.host.config
import abnba.host.views


class HostApplication(abnba.core.application.Application):

    name = abnba.host.config.HostConfig.name
    app_name = 'host'

    views = [
        (abnba.host.views.MainView, r'^main.html$', 'main',),
    ]


application = HostApplication()
