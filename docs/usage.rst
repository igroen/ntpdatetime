=====
Usage
=====

To use NTPDateTime::

    >>> from ntpdatetime import now
    >>> ntp_now, fetched = now()
    >>> ntp_now
    NTPDateTime(2015, 11, 26, 2, 14, 36, 932243)
    >>> fetched
    True
    >>> ntp_now.strftime('%d-%m-%Y %H:%M:%S')
    '01-12-2015 21:46:19'
