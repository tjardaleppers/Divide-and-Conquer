"""""
test_private.py
    - Algorithms and Data Structures
    - Assignment 2 Divide and Conquer
    - Dian Visser s3207846
    - Tjarda Leppers s3642844
    - This file contains (private) unit tests for the Inteldevice functions defined in divconq.py.
"""
import unittest
import numpy as np
from divconq import IntelDevice

class PrivateTestIntelDevice(unittest.TestCase):
    def test_search_solution_small_grid(self):
        # this test is designed to check whether the divconq_search function works with a small grid
        small_grid = np.array(
            [[2],
             [4]])

        raw_locations = [f"l{i}" for i in range(2)]
        raw_codes = [str(x) for x in small_grid.reshape(-1)]

        ob = IntelDevice(1, 2, [], [], caesar_shift=5)

        enc_locs = []
        for loc in raw_locations:
            enc_locs.append(ob.encode_message(loc))

        enc_codes = []
        for code in raw_codes:
            enc_codes.append(ob.encode_message(code))

        ob = IntelDevice(1, 2, enc_locs, enc_codes, caesar_shift=5)

        ob.fill_coordinate_to_loc()
        ob.fill_loc_grid()

        solutions = enc_locs
        for vid, v in enumerate(small_grid.reshape(-1)):
            if v == 2:
                continue
            result = ob.start_search(v)
            self.assertEqual(result, solutions[vid])

        # values that do not occur should lead to None
        for v in [1, 3]:
            result = ob.start_search(v)
            self.assertIsNone(result)

    def test_search_solution_big_grid(self):
        # this test is designed to check whether the divconq_search function works with a big grid

        # making a 2D grid with 10 rows and 10 columns
        rows = 10
        columns = 10
        big_grid = np.zeros((rows, columns), dtype=int)

        # filling grid with increasing integers from left to right
        for i in range(rows):
            for j in range(columns):
                big_grid[i][j] = i * columns + j + 1

        raw_locations = [f"l{i}" for i in range(100)]
        raw_codes = [str(x) for x in big_grid.reshape(-1)]

        ob = IntelDevice(10, 10, [], [], caesar_shift=5)

        enc_locs = []
        for loc in raw_locations:
            enc_locs.append(ob.encode_message(loc))

        enc_codes = []
        for code in raw_codes:
            enc_codes.append(ob.encode_message(code))

        ob = IntelDevice(10, 10, enc_locs, enc_codes, caesar_shift=5)

        ob.fill_coordinate_to_loc()
        ob.fill_loc_grid()

        solutions = enc_locs
        for vid, v in enumerate(big_grid.reshape(-1)):
            if v == 100:
                continue
            result = ob.start_search(v)
            self.assertEqual(result, solutions[vid])

        # values that do not occur should lead to None
        for v in [111, 212, 421, 120]:
            result = ob.start_search(v)
            self.assertIsNone(result)

    def test_search_solution_long_horizontal_grid(self):
        # this test is designed to check whether the divconq_search function works with a small grid

        horizontal_grid = np.array([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])

        raw_locations = [f"l{i}" for i in range(10)]
        raw_codes = [str(x) for x in horizontal_grid.reshape(-1)]

        ob = IntelDevice(10, 1, [], [], caesar_shift=6)

        enc_locs = []
        for loc in raw_locations:
            enc_locs.append(ob.encode_message(loc))

        enc_codes = []
        for code in raw_codes:
            enc_codes.append(ob.encode_message(code))

        ob = IntelDevice(10, 1, enc_locs, enc_codes, caesar_shift=6)

        ob.fill_coordinate_to_loc()
        ob.fill_loc_grid()

        solutions = enc_locs
        for vid, v in enumerate(horizontal_grid.reshape(-1)):
            if v == 10:
                continue
            result = ob.start_search(v)
            self.assertEqual(result, solutions[vid])

        # values that do not occur should lead to None
        for v in [1, 3, 5, 7, 9]:
            result = ob.start_search(v)
            self.assertIsNone(result)
