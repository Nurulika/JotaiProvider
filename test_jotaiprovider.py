# test_jotaiprovider.py
"""
Tests for JotaiProvider module.
"""

import unittest
from jotaiprovider import JotaiProvider

class TestJotaiProvider(unittest.TestCase):
    """Test cases for JotaiProvider class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = JotaiProvider()
        self.assertIsInstance(instance, JotaiProvider)
        
    def test_run_method(self):
        """Test the run method."""
        instance = JotaiProvider()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
