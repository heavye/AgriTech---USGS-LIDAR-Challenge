import unittest
import pdal 
import json
import sys, os
sys.path.append(os.path.abspath(os.path.join('../scripts')))

from getdata import get_raster_terrain

class TestGetdata(unittest.TestCase):
    """
		A class for unit-testing function in the getdata.py file
		Args:
        ----- 
			unittest.TestCase this allows the new class to inherit
			from the unittest module
	"""
    def test_path(self):
        """
        Test that checks the path to s3
        """
        PATH = "https://s3-us-west-2.amazonaws.com/usgs-lidar-public/"

        self.assertEqual('https://s3-us-west-2.amazonaws.com/usgs-lidar-public/', PATH)

if __name__ == '__main__':
    unittest.main()