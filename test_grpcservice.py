# test_grpcservice.py
"""
Tests for GrpcService module.
"""

import unittest
from grpcservice import GrpcService

class TestGrpcService(unittest.TestCase):
    """Test cases for GrpcService class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GrpcService()
        self.assertIsInstance(instance, GrpcService)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GrpcService()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
