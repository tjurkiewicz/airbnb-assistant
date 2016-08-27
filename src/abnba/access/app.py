
import abnba.core.application

import abnba.access.config


class AccessApplication(abnba.core.application.Application):

    name = abnba.access.config.AccessConfig.name
    app_name = 'access'

    views = [
    ]


application = AccessApplication()
