import unittest

import os
import subprocess


def call_command(command_to_call):
    call = subprocess.check_call(command_to_call, shell=True)
    output = subprocess.check_output(command_to_call, shell=True)
    return call, output[:-1]


class TestBC(unittest.TestCase):

    def test_divide(self):
        result = call_command("echo '6.5 / 2.7' | bc")
        self.assertEqual( result[0], 0)
        self.assertEqual( result[1], '2')

    def test_sum(self):
        result = call_command("echo '2 + 5' | bc")
        self.assertEqual( result[0], 0)
        self.assertEqual( result[1], '7')

    def test_difference(self):
        result = call_command("echo '10 - 4' | bc")
        self.assertEqual( result[0], 0)
        self.assertEqual( result[1], '6')

    def test_multiplying(self):
        result = call_command("echo '3 * 8' | bc")
        self.assertEqual( result[0], 0)
        self.assertEqual( result[1], '24')

    def test_scale(self):
        result = call_command("echo 'scale = 2; 2 / 3' | bc")
        self.assertEqual( result[0], 0)
        self.assertEqual( result[1], '.66')

    def test_remainder(self):
        result = call_command("echo '6 % 4' | bc")
        self.assertEqual( result[0], 0)
        self.assertEqual( result[1], '2')

    def test_exponent(self):
        result = call_command("echo '10^2' | bc")
        self.assertEqual( result[0], 0)
        self.assertEqual( result[1], '100')


if __name__ == '__main__':
    unittest.main()

