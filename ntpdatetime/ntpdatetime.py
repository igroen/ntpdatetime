# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import datetime
from socket import gaierror

from ntplib import NTPClient, NTPException

from .config import poolservers


class NTPDateTime(datetime):
    """Extends the datetime module to add a custom method
    """

    @classmethod
    def ntp_now(cls):
        """Returns a tuple containing a datatime object based on the time
           received from an NTP poolserver and a boolean value depending on
           whether it was fetched from a poolserver or not
        """
        for poolserver in poolservers:
            try:
                response = NTPClient().request(
                    poolserver,
                    version=3,
                    timeout=2
                )
                return cls.fromtimestamp(response.tx_time), True
            except (NTPException, gaierror):
                continue

        # No poolservers supplied or no resposne from poolservers
        # Just return the system time for now
        return cls.now(), False

ntpdatetime = NTPDateTime
now = NTPDateTime.ntp_now
