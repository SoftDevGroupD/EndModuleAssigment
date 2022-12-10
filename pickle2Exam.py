#Erase Self
import pickle
import unittest

def creat_dictionary():
        fruits = ["apple", "banana", "cherry", "pear", "avocado"]
        prices = [100, 50, 150, 80, 120]
        dictionary_fruits_price = {fruit:price for (fruit, price) in zip(fruits, prices)}
        print(dictionary_fruits_price)

#I add a variable that references to the creation of the dictionary.
a_dictionary=creat_dictionary()
        
def serialize_binary():
    file_to_write = open("a_dictionary", "wb")
    pickle.dump(a_dictionary,file_to_write)
    file_to_write.close()
 
def deserialize_binary():
    file_to_read= open("a_dictionary.pickle","rb")
    dictionary_2 = pickle.load(file_to_read)
    return dictionary_2

class TestsDeserialize(unittest.TestCase):
    def test(self):                                
        self.assertEqual(deserialize_binary(),{'a': 1, 'b': 2},)
if __name__=='__main__':
    unittest.main()
