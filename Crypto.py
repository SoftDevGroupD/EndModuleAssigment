# import required module
from cryptography.fernet import Fernet


#Above code will generate a file with the name filekey.key. The file will contain one line, 
# which is a string acting as a key i.e. J64ZHFpCWFlS9zT7y5zxuQN1Gb09y7cucne_EhuWyDM=

# key generation
key = Fernet.generate_key()
 
# string the key in a file
with open('filekey.key', 'wb') as filekey:
   filekey.write(key)

'''
   Encrypt the file using the key generated
Now we have an encrypted key and file to be encrypted. Now write code to encrypt this file:

Open the file that contains the key.
Initialize the Fernet object and store it in the fernet variable.
Read the original file.
Encrypt the file and store it into an object.
Then write the encrypted data into the same file nba.csv.
'''

# opening the key
with open('filekey.key', 'rb') as filekey:
    key = filekey.read()
 
# using the generated key
fernet = Fernet(key)
 
# opening the original file to encrypt
with open('C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3.txt', 'rb') as file:
    original = file.read()
     
# encrypting the file
encrypted = fernet.encrypt(original)
 
# opening the file in write mode and
# writing the encrypted data
with open('C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3_encrypted.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)
    

###############Decrypt

# using the key
fernet = Fernet(key)
 
# opening the encrypted file
with open('C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3_encrypted.txt', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# decrypting the file
decrypted = fernet.decrypt(encrypted)
 
# opening the file in write mode and
# writing the decrypted data
with open('C:/Users/esmer/OneDrive/Desktop/Liverpool/Software Development/Week8/txt/sample3_desencrypted.txt', 'wb') as dec_file:
    dec_file.write(decrypted)

