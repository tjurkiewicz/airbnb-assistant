from __future__ import absolute_import  # Python 2 only

import django.conf
import django.contrib.staticfiles.storage
import django.core.urlresolvers
import django.utils.timezone

import jinja2


def append_once(list, element):
    if element not in list:
        list.append(element)


def strftime(fmt, date=None):
    if not date:
        date = django.utils.timezone.now()
    return date.strftime(fmt.encode('utf-8')).decode('utf-8')

def environment(**opts):
    extensions = opts.get('extensions', [])
    append_once(extensions, 'jinja2.ext.i18n')
    append_once(extensions, 'jinja2.ext.with_')
    opts['extensions'] = extensions

    env = jinja2.Environment(**opts)
    env.globals.update({
        'strftime': strftime,
        'settings': django.conf.settings,
        'static': django.contrib.staticfiles.storage.staticfiles_storage.url,
        'url': django.core.urlresolvers.reverse
    })
    env.install_null_translations()

    print opts, env
    return env