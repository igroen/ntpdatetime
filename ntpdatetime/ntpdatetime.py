# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import datetime

import ntplib

from . import config


class NTPDateTime(datetime):

    @classmethod
    def ntp_now(cls):
        """Returns a datatime object based on the time
           received from an NTP server"""
        for poolserver in config.poolservers:
            try:
                response = ntplib.NTPClient().request(
                    poolserver,
                    version=3,
                    timeout=2
                )
                return cls.fromtimestamp(response.tx_time), True
            except:
                continue

        # No poolservers supplied or no resposne from poolservers
        # Just return the system time for now
        return cls.now(), False

ntpdatetime = NTPDateTime
now = NTPDateTime.ntp_now
