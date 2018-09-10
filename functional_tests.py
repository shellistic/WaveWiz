import unittest

from pyconductor import *


class NewUserTest(unittest.TestCase):

    def setUp(self):
        self.preloaded_dict = load_test_values()

    def test_user_can_run_material_testcase(self):
        calculate_conductance(self.preloaded_dict["air"])

    def test_user_can_add_material_to_materialdict(self):
        pass

if __name__ == "__main__":
    unittest.main()
