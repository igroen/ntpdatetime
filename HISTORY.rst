.. :changelog:

History
-------

0.1.0 (2015-11-25)
------------------

* First release on PyPI.


0.1.1 (2015-11-26)
------------------

* ``ntp_now()`` Now returns a tuple containing the current datetime and a boolean value::

    True  # Time was fetched from an NTP server
    False  # Error occurred when connection to an NTP poolserver. System datetime is returned


0.1.2 (2015-11-27)
------------------

* Patch for release on pypi. Old version (0.1.1) was removed and cannot be released again.
