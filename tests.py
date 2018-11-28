import unittest
import os
from tempfile import mkdtemp
from shutil import rmtree

class TestBase(unittest.TestCase):
    '''
    TestCase that need existing git repositories can
    derive from this class.
    '''
    
    def setUp(self):
        super(TestBase, self).setUp()
        # Make the current directory being an empty temporary directory
        self.cwd = mkdtemp(prefix='git-bv_test')
        os.chdir(self.cwd)

    def tearDown(self):
        super(TestBase, self).tearDown()
        rmtree(self.cwd)

class CreateRepositories(object):
    '''
    TestCase that need existing git repositories can
    derive from this class.
    '''
    
    def setUp(self):
        super(CreateRepositories, self).setUp()

    def tearDown(self):
        super(CreateRepositories, self).tearDown()


class Test(TestBase, CreateRepositories):

    def test_current_directory(self):
        self.assertEqual(os.listdir(os.getcwd()),[])
    
    def test_01(self):
        pass
    
    def test_02(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
