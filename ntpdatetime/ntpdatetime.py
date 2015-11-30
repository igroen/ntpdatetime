# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import datetime
from socket import gaierror

from ntplib import NTPClient, NTPException

from .config import poolservers


class NTPDateTime(datetime):

    @classmethod
    def ntp_now(cls):
        """Returns a datatime object based on the time
           received from an NTP server"""
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
