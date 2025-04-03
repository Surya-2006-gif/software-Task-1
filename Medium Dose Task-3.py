import numpy as np


#getting the encrypted code from rover

Encrypted_code=input("Enter the encrypted code: ")




#checking whether the encrypted message is correct(alphabets only)
 
if Encrypted_code.isalpha():

     #converting all characters to upper case
    Encrypted_code=Encrypted_code.upper()

    code=list(Encrypted_code)
    
    #decrypting the message received
    # The edge case of alphabet 'A' is handles by the circular shifting 

    decrypted_code=[chr(((ord(character)-(i+1)-65)%26)+65)  for i,character in enumerate(Encrypted_code)]



    print(f"The decryption of the message received is {"".join(decrypted_code)}")

else:
    print("Encrypted code is damaged or not encrypted properly")    