import numpy as np
#this dictionary hold keys and values neccesary for our conversion
#this convention is found from internet and chatgpt
morse_code_dict = {
    '._': 'A', '_...': 'B', '_._.': 'C', '_..': 'D', '.': 'E',
    '.._.': 'F', '__.': 'G', '....': 'H', '..': 'I', '.___': 'J',
    '_._': 'K', '._..': 'L', '__': 'M', '_.': 'N', '___': 'O',
    '.__.': 'P', '__._': 'Q', '._.': 'R', '...': 'S', '_': 'T',
    '.._': 'U', '..._': 'V', '.__': 'W', '_.._': 'X', '_.__': 'Y',
    '__..': 'Z',

    '_____': '0', '.____': '1', '..___': '2', '...__': '3', '...._': '4',
    '.....': '5', '_....': '6', '__...': '7', '___..': '8', '____.': '9',

    '._._._': '.', '__..__': ',', '..__..': '?', '.____.': "'",
    '_._.__': '!', '_.._.': '/', '_.__.': '(', '_.__._': ')',
    '._...': '&', '___...': ':', '_._._.': ';', '_..._': '=',
    '._._.': '+', '_...._': '-', '..__._': '_', '._.._.': '"',
    '..._.._': '$', '._._.': '@',

   # '': ' '
}

def morse_code_converter(morse_code):
    global morse_code_dict
    decrypted_words = []

    morse_list = morse_code.split("   ")  # Splits words by three spaces,three space corresponds to seperate to different words

    for morse_chunk in morse_list:   #processing one word at a time by combining each character given my the morse code
        decrypted_words.append(''.join(morse_code_dict.get(value) for value in morse_chunk.split(' ')))

    return decrypted_words

morse_code = input("Enter the morse code: ")

morse_code_array = np.array(list(morse_code))
#checking whether any other irrelavant character is present in the morse code
if np.all(np.isin(np.unique(morse_code_array), ['.', '_', ' '])):
    decrypted_list = morse_code_converter(morse_code)
    print(f"The decrypted message is {' '.join(decrypted_list)}") #joining the words with spaces
else:
    print("Invalid Morse Code input.")
