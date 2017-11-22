import unittest
from collector import showFilteredFiles

class CollectorTest(unittest.TestCase):

    def test_filtered_python_files(self):
        src = '/Users/gostendorf/PycharmProjects/filecollector/tests/testfiles'
        filetype = '.py'
        filtered_files = showFilteredFiles(src, filetype)
        self.assertEqual(len(filtered_files), 2, 'The number of files should be 2')

    def test_filtered_pdf_files(self):
        src = '/Users/gostendorf/PycharmProjects/filecollector/tests/testfiles'
        filetype = '.pdf'
        filtered_files = showFilteredFiles(src, filetype)
        self.assertEqual(len(filtered_files), 3, 'The number of files should be 3')

    def test_filtered_jpg_files(self):
        src = '/Users/gostendorf/PycharmProjects/filecollector/tests/testfiles'
        filetype = '.jpg'
        filtered_files = showFilteredFiles(src, filetype)
        self.assertEqual(len(filtered_files), 2, 'The number of files should be 2')

    def test_filtered_png_files(self):
        src = '/Users/gostendorf/PycharmProjects/filecollector/tests/testfiles'
        filetype = '.png'
        filtered_files = showFilteredFiles(src, filetype)
        self.assertEqual(len(filtered_files), 1, 'The number of files should be 1')

            # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())


if __name__ == '__main__':
    unittest.main()