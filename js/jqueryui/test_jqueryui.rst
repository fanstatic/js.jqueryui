How to use?
===========

You can import jQuery UI from ``js.jqueryui`` and ``need`` it
where you want these resources to be included on a page::

  >>> from js.jqueryui import jqueryui
  >>> jqueryui.need()

Themes
------

The themes in the jQuery UI themes distribution are included as well::

  >>> from js.jqueryui import black_tie
  >>> black_tie.need()

Locales
-------

Also included are locales for the jQuery UI datepicker.

How to get the right locale for the current request depends on your web framework.
In `Pyramid`_ you could e.g. do something like this::

    from js.jqueryui import ui_datepicker_locales
    from pyramid.i18n import get_locale_name

    locale_name = get_locale_name(request)
    if locale_name in ui_datepicker_locales:
        ui_datepicker_locales[locale_name].need()

.. _`Pyramid`: http://www.pylonsproject.org
