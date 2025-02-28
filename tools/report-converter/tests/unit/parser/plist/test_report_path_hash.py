# -------------------------------------------------------------------------
#
#  Part of the CodeChecker project, under the Apache License v2.0 with
#  LLVM Exceptions. See LICENSE for license information.
#  SPDX-License-Identifier: Apache-2.0 WITH LLVM-exception
#
# -------------------------------------------------------------------------
""" Test Store handler features.  """


import os
import unittest

from codechecker_report_converter.report import report_file
from codechecker_report_converter.report.hash import get_report_path_hash


class ReportPathHashHandler(unittest.TestCase):
    """
    Test report path hash generation handler features.
    """

    @classmethod
    def setup_class(cls):
        # Already generated plist files for the tests.
        cls.__this_dir = os.path.dirname(__file__)
        cls.__plist_test_files = os.path.join(
            cls.__this_dir, 'plist_test_files')

    def test_report_path_hash_generation(self):
        """
        Test report path hash generation.
        """
        clang50_trunk_plist = os.path.join(
            self.__plist_test_files, 'clang-5.0-trunk.plist')
        reports = report_file.get_reports(clang50_trunk_plist)
        self.assertEqual(len(reports), 3)

        report_hash_to_path_hash = {
            '79e31a6ba028f0b7d9779faf4a6cb9cf':
                '2dc99e0cd54ee4216bd884d49f0bc8c7',
            '8714f42d8328bc78d5d7bff6ced918cc':
                'a316a401913aaef9af56692bef6ba109',
            'a6d3464f8aab9eb31a8ea7e167e84322':
                '9653c97c587fd7a365fbe0ce3df00d7e'
        }

        for report in reports:
            path_hash = get_report_path_hash(report)
            self.assertEqual(
                path_hash, report_hash_to_path_hash[report.report_hash])
