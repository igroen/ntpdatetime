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

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_instance(self):
        ntp_dt = ntpdatetime(2002, 12, 25)
        assert isinstance(ntp_dt, datetime)
        assert isinstance(now(), datetime)

    @mock.patch('ntplib.NTPClient')
    def test_poolserver_exception(self, ntpclient):
        ntpclient().request = Exception()
        assert isinstance(now(), datetime)

if __name__ == '__main__':
    import sys
    sys.exit(unittest.main())
