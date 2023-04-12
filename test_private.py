"""""
test_private.py
    - Algorithms and Data Structures
    - Assignment 2 Divide and Conquer
    - Dian Visser s3207846
    - Tjarda Leppers s3642844
    - This file contains (private) unit tests for the Inteldevice functions defined in divconq.py.
"""

import numpy as np
import typing

from divconq import IntelDevice


class PrivateTestIntelDevice(unittest.TestCase):

    def test_encode_empty_message(self):

        """
        This unittest checks if the encode_message function correctly handles an empty string as a message.
        """

        ob = IntelDevice(3, 5, [], [], 0)
        solution = None
        query = [""]

        for query, answer in zip(query, answer):
            self.assertEqual(ob.encode_message(query), answer)
