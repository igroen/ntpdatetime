#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_ntpdatetime
----------------------------------

Tests for `ntpdatetime` module.
"""
import unittest
from datetime import datetime

import mock

from ntpdatetime import now, ntpdatetime


class TestNtpdatetime(unittest.TestCase):

    def test_instance(self):
        ntp_dt = ntpdatetime(2002, 12, 25)
        self.assertTrue(isinstance(ntp_dt, datetime))
        ntp_now, fetched = now()
        self.assertTrue(fetched)  # Fetched from NTP server
        self.assertTrue(isinstance(ntp_now, datetime))

    @mock.patch('ntplib.NTPClient')
    def test_poolserver_exception(self, ntpclient):
        ntpclient().request = Exception()
        ntp_now, fetched = now()
        self.assertFalse(fetched)  # Not fetched from NTP server
        self.assertTrue(isinstance(ntp_now, datetime))

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
