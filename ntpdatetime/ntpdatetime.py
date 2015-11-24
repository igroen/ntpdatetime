# -*- coding: utf-8 -*-
from datetime import datetime

import ntplib


class NTPDateTime(datetime):
    _poolservers = (
        'nl.pool.ntp.org',
        'europe.pool.ntp.org',
        'pool.ntp.org',
    )

    @classmethod
    def ntp_now(cls):
        """Returns a datatime object based on the time
           received from an NTP server"""
        for poolserver in cls._poolservers:
            try:
                response = ntplib.NTPClient().request(
                    poolserver,
                    version=3,
                    timeout=2
                )
                return cls.fromtimestamp(response.tx_time)
            except:
                continue

        # No poolservers supplied or no resposne from poolservers
        # Just return the system time for now
        return cls.now()


ntp_now = NTPDateTime.ntp_now

# print(ntp_now().strftime('%d-%m-%Y %H:%M:%S'))
