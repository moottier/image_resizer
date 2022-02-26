import unittest
import resizer

class TestParseSize(unittest.TestCase):
    def test_valid_size(self):
        s = ["1x1","1X1"]
        expected = (1,1)
        for val in s:
            with self.subTest(val=val):
                actual = resizer.parse_size(val)
                self.assertTrue(expected == actual)

    def test_invalid_size_spaces(self):
        s = ["1 x1"," 1 x1"," 1x1","1x 1","1x 1 ","1x1 ","1 x1 "," 1x 1"," 1x1 ","1 x 1", "1 x 1 "," 1 x1"," 1 x 1 "]
        expected = ValueError
        for val in s:
            with self.subTest(val=val):
                self.assertRaises(expected, resizer.parse_size, val)

    def test_invalid_size_non_numeric(self):
        s = ["x1","x","1x","axa","ax","xa","axa"]
        expected = ValueError
        for val in s:
            with self.subTest(val=val):
                self.assertRaises(expected, resizer.parse_size, val)

    def test_invalid_size_bad_format(self):
        s = ["x","111"]
        expected = ValueError
        for val in s:
            with self.subTest(val=val):
                self.assertRaises(expected, resizer.parse_size, val)

class TestValidateSize(unittest.TestCase):
    def test_valid_size(self):
        s = ["1x1","1X1"]
        for val in s:
            with self.subTest(val=val):
                actual = resizer.validate_size(val)
                self.assertTrue(actual)

    def test_invalid_size_spaces(self):
        s = ["1 x1"," 1 x1"," 1x1","1x 1","1x 1 ","1x1 ","1 x1 "," 1x 1"," 1x1 ","1 x 1", "1 x 1 "," 1 x1"," 1 x 1 "]
        for val in s:
            with self.subTest(val=val):
                actual = resizer.validate_size(val)
                self.assertFalse(actual)

    def test_invalid_size_non_numeric(self):
        s = ["x1","x","1x","axa","ax","xa","axa"]
        for val in s:
            with self.subTest(val=val):
                actual = resizer.validate_size(val)
                self.assertFalse(actual)
    
    def test_invalid_size_length(self):
        s = ["1","1"*30]
        for val in s:
            with self.subTest(val=val):
                actual = resizer.validate_size(val)
                self.assertFalse(actual)

    def test_invalid_size_bad_format(self):
        s = ["x","111"]
        for val in s:
            with self.subTest(val=val):
                actual = resizer.validate_size(val)
                self.assertFalse(actual)

class TestGetSizes(unittest.TestCase):
    def test_valid_sizes(self):
        s = ["1x1","1X2"]
        expected = [(1,1),(1,2)]
        actual = resizer.get_sizes(s)
        self.assertTrue(actual == expected)

    def test_invalid_sizes(self):
        s = ["1x1","1X2"]
        expected = [(1,1),(1,2)]
        actual = resizer.get_sizes(s)
        self.assertTrue(actual == expected)    