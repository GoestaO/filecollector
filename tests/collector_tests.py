import unittest
from collector import showFilteredFiles, findAllFiles


class CollectorTest(unittest.TestCase):

    def setUp(self):
        self.src = '/Users/gostendorf/PycharmProjects/filecollector/tests/testfiles'

    ## Check, if all files in the folder and subfolder have been found
    def test_find_all_files(self):
        file_list = findAllFiles(self.src)
        self.assertIsNotNone(file_list, "[findAllFiles] The file list is null, this is not good!")
        self.assertEqual(len(file_list), 9, "[findAllFiles] The file list should contain 9 elements!")

    def test_filtered_python_files(self):
        src = '/Users/gostendorf/PycharmProjects/filecollector/tests/testfiles'
        filetype = '.py'
        filtered_files = showFilteredFiles(src, filetype)
        self.assertEqual(len(filtered_files), 2, 'The number of files should be 2')

    def test_filtered_pdf_files(self):
        src = '/Users/gostendorf/PycharmProjects/filecollector/tests/testfiles'
        filetype = '.pdf'
        filtered_files = showFilteredFiles(src, filetype)
        self.assertEqual(len(filtered_files), 4, 'The number of files should be 4')

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

if __name__ == '__main__':
    unittest.main()