import unittest
import pickle

a_dictionary = {"a": 1, "b": 2}

def serialize():
    file_to_write = open("a_dictionary.pickle", "wb")
    pickle.dump(a_dictionary,file_to_write)
    file_to_write.close()

def deserialize():
    file_to_read= open("a_dictionary.pickle","rb")
    dictionary_2 = pickle.load(file_to_read)
    return dictionary_2

def read_binary():
    file_to_read_binary= open("a_dictionary.pickle","rb")
    dictionary_to_read_binary = pickle.load(file_to_read_binary)
    file_to_read_binary.close()
    return (dictionary_to_read_binary)

#Unit Test for testing the correct deserialization of a dictionary for the function deserialize

class TestsDeserialize(unittest.TestCase):
    def test(self):                                
        self.assertEqual(read_binary(),{'a': 1, 'b': 2},)
if __name__=='__main__':
    unittest.main()

#Unit Test for testing the correct deserialization of a dictionary for the function read_binary
    
class TestsBinary(unittest.TestCase):
    def test(self):                                
        self.assertEqual(read_binary(),{'a': 1, 'b': 2},)
if __name__=='__main__':
    unittest.main()
