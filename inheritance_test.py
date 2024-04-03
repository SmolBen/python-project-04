import unittest
from practical_project_3 import Record, DefaultRecordFormatter

class TestRecordFormatter(unittest.TestCase):
    """
    Unit test class by Ben Nguyen for testing the overridden output format of DefaultRecordFormatter.
    """

    def test_default_record_format(self):
        """
        Test if the overridden output format of DefaultRecordFormatter is correct.
        """
        # Create a sample record
        sample_record = Record("Source", "Latin Name", "English Name", "French Name", "2024", "March", "24")
        
        # Create an instance of DefaultRecordFormatter
        formatter = DefaultRecordFormatter()
        
        # Expected output format
        expected_output = "Source: Source, Latin Name: Latin Name, English Name: English Name, French Name: French Name, Year: 2024, Month: March, Number of Otoliths: 24"
        
        # Get the formatted record
        formatted_record = formatter.format_record(sample_record)
        
        # Assert if the formatted record matches the expected output
        self.assertEqual(formatted_record, expected_output, "Output format does not match expected format")

if __name__ == "__main__":
    unittest.main()
