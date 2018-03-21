js.jqueryui
***********

Introduction
============

This library packages `jQuery UI`_ for `fanstatic`_. It is aware of different modes (normal, minified).

.. _`fanstatic`: http://fanstatic.org
.. _`jQuery UI`: http://jqueryui.com

This requires integration between your web framework and ``fanstatic``,
and making sure that the original resources (shipped in the ``resources``
directory in ``js.jqueryui``) are published to some URL.


Update this package
===================

.. XXX --> keine einzelnen JS-Dateien mehr, auflösem der Abhängigkeiten funktioniert nicht automatisch!


* Remove the contents of `js/jquerui/resources/`.
* Create a directory `js/jquerui/resources/ui/`.
* Download the stable release from http://jqueryui.com/download/. Do not use
  the form to create a specific version but use the link named `Stable` next to `Quick download` near the top of the page.
* Copy `jquery-ui.*` from the downloaded archive to `js/jquerui/resources/ui/`.
* Download the themes from http://jqueryui.com/download/. Do not use
  the form to create a specific version but use the link named `Themes` next to `Quick download` near the top of the page.
* Copy the `themes` directory from the downloaded archive to
  `js/jquerui/resources/`.
* Download the latest release from
  https://github.com/jquery/jquery-ui/releases.
* Copy the directory `ui/i18n` to `js/jquerui/resources/ui/`.
* Install thhe following packages using ``npm``:

    * uglify-js
    * clean-css-cli
* Make sure the binaries created by the packages are in your ``PATH``.
* Call: ``python compress.py`` in the root dir of this package.
