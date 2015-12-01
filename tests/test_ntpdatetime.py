#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ntpdatetime
----------------------------------

Tests for `ntpdatetime` module.
"""
import unittest
from datetime import datetime
from socket import gaierror

from mock import patch
from ntplib import NTPClient, NTPException, NTPStats

from ntpdatetime import config, now, ntpdatetime


class TestNtpdatetime(unittest.TestCase):

    @patch.object(NTPClient, 'request')
    def test_instance(self, mock):
        ntp_dt = ntpdatetime(2002, 12, 25)
        self.assertTrue(isinstance(ntp_dt, datetime))
        mock.return_value = NTPStats()
        ntp_now, fetched = now()
        self.assertTrue(fetched)  # Fetched from NTP server
        self.assertTrue(isinstance(ntp_now, datetime))

    @patch.object(NTPClient, 'request')
    def test_ntp_exception(self, mock):
        mock.side_effect = NTPException
        ntp_now, fetched = now()
        self.assertEqual(mock.call_count,
                         self.poolservers)
        self.assertFalse(fetched)  # Not fetched from NTP server
        self.assertTrue(isinstance(ntp_now, datetime))

    @patch.object(NTPClient, 'request')
    def test_gai_error(self, mock):
        mock.side_effect = gaierror
        ntp_now, fetched = now()
        self.assertEqual(mock.call_count,
                         self.poolservers)
        self.assertFalse(fetched)  # Not fetched from NTP server
        self.assertTrue(isinstance(ntp_now, datetime))

    @property
    def poolservers(self):
        return len(config.poolservers)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
