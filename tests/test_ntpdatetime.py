#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ntpdatetime
----------------------------------

Tests for `ntpdatetime` module.
"""
import socket
import unittest
from datetime import datetime

import mock
import ntplib

from ntpdatetime import config, now, ntpdatetime

ntp_exception_mock = mock.Mock()
ntp_exception_mock.side_effect = ntplib.NTPException

socket_gaierror_mock = mock.Mock()
socket_gaierror_mock.side_effect = socket.gaierror


class TestNtpdatetime(unittest.TestCase):

    def test_instance(self):
        ntp_dt = ntpdatetime(2002, 12, 25)
        self.assertTrue(isinstance(ntp_dt, datetime))
        ntp_now, fetched = now()
        self.assertTrue(fetched)  # Fetched from NTP server
        self.assertTrue(isinstance(ntp_now, datetime))

    @mock.patch.object(ntplib.NTPClient, 'request', ntp_exception_mock)
    def test_ntp_exception(self):
        ntp_now, fetched = now()
        self.assertEqual(ntp_exception_mock.call_count,
                         self.poolservers)
        self.assertFalse(fetched)  # Not fetched from NTP server
        self.assertTrue(isinstance(ntp_now, datetime))

    @mock.patch.object(ntplib.NTPClient, 'request', socket_gaierror_mock)
    def test_gai_error(self):
        ntp_now, fetched = now()
        self.assertEqual(socket_gaierror_mock.call_count,
                         self.poolservers)
        self.assertFalse(fetched)  # Not fetched from NTP server
        self.assertTrue(isinstance(ntp_now, datetime))

    @property
    def poolservers(self):
        return len(config.poolservers)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
