import unittest
from practical_project_1 import BusinessLayer 

class TestBusinessLayer(unittest.TestCase):
    """
    A class for unit testing the BusinessLayer class.
    """
    
    def test_load_records(self):
        filename = "test_dataset.csv"  # Create a test dataset 
        business_layer = BusinessLayer(filename)
        self.assertTrue(len(business_layer.records) > 0, "Records should be loaded")

if __name__ == "__main__":
    unittest.main()