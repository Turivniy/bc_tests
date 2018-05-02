import unittest

import os
import subprocess
import xmlrunner

from xml.dom import minidom


def call_command(command_to_call):
    call = subprocess.check_call(command_to_call, shell=True)
    output = subprocess.check_output(command_to_call, shell=True)
    return call, output[:-1]


def check_results(test_results_file):
    xmldoc = minidom.parse(test_results_file)
    itemlist = xmldoc.getElementsByTagName('testsuite')
    failures = int(itemlist[0].attributes['failures'].value)
    errors = int(itemlist[0].attributes['errors'].value)
    if failures > 0 or errors > 0:
        exit(1)
    exit(0)


def create_test_results_dir(results_dir='artifacts'):
    cwd = os.path.dirname(os.getcwd())
    full_patch = '{}/{}/'.format(cwd, results_dir)
    if not os.path.exists(full_patch):
        os.makedirs(full_patch)
    return full_patch


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
        self.assertEqual( result[1], 'ss.66')

    def test_remainder(self):
        result = call_command("echo '6 % 4' | bc")
        self.assertEqual( result[0], 0)
        self.assertEqual( result[1], '2')

    def test_exponent(self):
        result = call_command("echo '10^2' | bc")
        self.assertEqual( result[0], 0)
        self.assertEqual( result[1], '100')


if __name__ == '__main__':
    results_dir = create_test_results_dir()
    test_results_file = 'results.xml'
    test_results_patch = results_dir + test_results_file
    print("TRP", test_results_patch)
    with open(test_results_patch, 'wb') as output:
        unittest.main(testRunner=xmlrunner.XMLTestRunner(output=output),
                      failfast=False, buffer=False, catchbreak=False)
    check_results(test_results_patch)
