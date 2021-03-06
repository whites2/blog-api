Python Client for Stackdriver Logging
=====================================

    Python idiomatic client for `Stackdriver Logging`_

.. _Stackdriver Logging: https://cloud.google.com/logging/

|pypi| |versions|

-  `Documentation`_

.. _Documentation: https://googlecloudplatform.github.io/google-cloud-python/stable/logging-usage.html

Quick Start
-----------

.. code-block:: console

    $ pip install --upgrade google-cloud-logging

Authentication
--------------

With ``google-cloud-python`` we try to make authentication as painless as
possible. Check out the `Authentication section`_ in our documentation to
learn more. You may also find the `authentication document`_ shared by all
the ``google-cloud-*`` libraries to be helpful.

.. _Authentication section: http://google-cloud-python.readthedocs.io/en/latest/google-cloud-auth.html
.. _authentication document: https://github.com/GoogleCloudPlatform/gcloud-common/tree/master/authentication

Using the API
-------------

`Stackdriver Logging`_ API (`Logging API docs`_) allows you to store, search,
analyze, monitor, and alert on log data and events from Google Cloud Platform.

.. _Logging API docs: https://cloud.google.com/logging/docs/

.. code:: python

    from google.cloud import logging
    client = logging.Client()
    logger = client.logger('log_name')
    logger.log_text('A simple entry')  # API call

Example of fetching entries:

.. code:: python

    for entry in logger.list_entries():
        print(entry.payload)

See the ``google-cloud-python`` API `logging documentation`_ to learn how to
connect to Stackdriver Logging using this Client Library.

.. _logging documentation: https://googlecloudplatform.github.io/google-cloud-python/stable/logging-usage.html

.. |pypi| image:: https://img.shields.io/pypi/v/google-cloud-logging.svg
   :target: https://pypi.python.org/pypi/google-cloud-logging
.. |versions| image:: https://img.shields.io/pypi/pyversions/google-cloud-logging.svg
   :target: https://pypi.python.org/pypi/google-cloud-logging


