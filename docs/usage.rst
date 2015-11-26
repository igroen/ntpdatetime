========
Usage
========

To use NTPDateTime in a project::

    >>> from ntpdatetime import now
    >>> ntp_now, fetched = now()
    >>> ntp_now
    NTPDateTime(2015, 11, 26, 2, 14, 36, 932243)
    >>> fetched
    True
