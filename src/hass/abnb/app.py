
import hass.core.application

import hass.abnb.config


class AirBNBApplication(hass.core.application.Application):

    name = hass.abnb.config.AirBNBConfig.name
    app_name = 'abnb'

    views = [
    ]


application = AirBNBApplication()
