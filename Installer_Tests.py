__author__ = 'svalleru'
import unittest
from Installer import Installer


class NodeTest(unittest.TestCase):
    def setUp(self):
        self.testpkg1 = Installer('testpkg1')
        self.testpkg2 = Installer('testpkg2')
        self.testpkg3 = Installer('testpkg3')

    def test_make_dep(self):
        self.testpkg1.make_dep(self.testpkg2)
        self.assertEqual(len(self.testpkg1.deps), 1)

    def test_install(self):
        self.testpkg1.make_dep(self.testpkg2)
        self.testpkg2.make_dep(self.testpkg3)
        self.testpkg1.install()
        self.assertTrue(self.testpkg1.name in Installer.installed)
        self.assertTrue(self.testpkg2.name in Installer.installed)
        self.assertTrue(self.testpkg3.name in Installer.installed)

    def test_remove(self):
        self.testpkg1.make_dep(self.testpkg2)
        self.testpkg1.make_dep(self.testpkg3)
        self.testpkg1.install()
        self.testpkg1.remove()
        self.assertFalse(self.testpkg1.name in Installer.installed)
        self.assertFalse(self.testpkg2.name in Installer.installed)
        self.assertFalse(self.testpkg3.name in Installer.installed)

    def test_resolver(self):
        self.testpkg1.make_dep(self.testpkg2)
        self.testpkg2.make_dep(self.testpkg1)
        self.assertRaises(Exception, lambda: self.testpkg1.resolver([], []))

    def tearDown(self):
        del self.testpkg1
        del self.testpkg2


if __name__ == '__main__':
    unittest.main()
