# For lulz only (this is not a secure means of encryption)

import emoji, string

# Setting up alphabet : emoji shortname mappings
alphabet = string.ascii_lowercase
mappings = {}
shortNames = ['grinning face with smiling eyes', 'grinning face', 'beaming face with smiling eyes', 'grinning squinting face',
    'grinning face with sweat', 'rolling on the floor laughing', 'face with tears of joy', 'slightly smiling face', 'upside-down face',
    'winking face', 'winking face with tongue', 'smiling face with halo', 'relieved face', 'smiling face with heart-eyes',
    'face with crossed-out eyes', 'face blowing a kiss', 'kissing face', 'pouting face', 'kissing face with closed eyes', 'kissing face with smiling eyes',
    'smirking face', 'face savoring food', 'face with tongue', 'unamused face', 'squinting face with tongue',
    'money-mouth face']

for idx, char in enumerate(alphabet):
    tempStr = shortNames[idx].replace(" ", "_")
    tempStr = f":{tempStr}:"
    mappings[char] = tempStr

# Function to encode plaintext to ciphertext
def convertToCipher(plaintext):
    outStr = ''
    for char in plaintext:
        if char not in alphabet:
            outStr += char
        else:
            outStr += emoji.emojize(mappings[char])
    return outStr

# Function to decode
def convertToPlaintext(ciphertext):
    outStr = ''
    for char in ciphertext:
        if emoji.demojize(char) not in mappings.values():
            outStr += emoji.demojize(char)
        else:
            for k, v in mappings.items():
                if v == emoji.demojize(char):
                    outStr += k
    return outStr

originalText = "ur bad at apex!"
cipherText = convertToCipher(originalText)
print(f"Encoded '{originalText}' as: {cipherText}")
print()
print("Attempting to decode...")
print()
backToPlaintext = convertToPlaintext(cipherText)
print(f"Decoded '{cipherText}' as: {backToPlaintext}")