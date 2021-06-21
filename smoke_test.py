import subprocess
import unittest

class TestBasic(unittest.TestCase):
    def test_run(self):
        p = subprocess.Popen(
                ['java', '-jar', 'fake_test.jar'],
                stdout=subprocess.PIPE
            )
        out, _ = p.communicate()
        self.assertEqual(b'OK\r\n', out)

if __name__ == '__main__':
    unittest.main()
