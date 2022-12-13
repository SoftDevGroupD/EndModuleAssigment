import filecmp
import unittest
   
def read_deserialized(fileDesencrypted, file_to_compare):  
    # Path of file desencrypted
    file1 = fileDesencrypted
    # Path of file to test again 
    file2 = file_to_compare
# Compare the
# contents of both files
    comp = filecmp.cmp(fileDesencrypted, file2, shallow = True)  
# Print the result of comparison
    return comp
read_deserialized(fileDesencrypted = 'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3.txt',
                  file_to_compare = 'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample4.txt'
                  )

#UnitTest to compare the contents of the file Desencrypted vs what should be desencrypted.

class TestsDeserialize(unittest.TestCase):
    def test(self):
            self.assertTrue(read_deserialized(
                fileDesencrypted = 'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3.txt',
                  file_to_compare = 'C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample4.txt'
            ))
if __name__=='__main__':
    unittest.main()



'''
class TestsDeserialize(unittest.TestCase):
    def test(self):
            self.assertSequenceEqual(print(read()),"this is a module assigment testtttt")
if __name__=='__main__':
    unittest.main()
'''