import unittest

class BasicUnitTest(unittest.TestCase):
    def test_string_upper(self):
        self.assertEquals("foo".upper(), "FOO")

    def test_string_isupper(self):
        self.assertTrue("FOO".isupper())
        self.assertFalse("Foo".isupper())

    def test_string_split(self):
        s = "Hello World"
        self.assertTrue(s.split(), [ "Hello", "World" ])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == "__main__":
    unittest.main()
