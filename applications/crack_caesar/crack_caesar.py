# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
f = open(r"applications\crack_caesar\ciphertext.txt")
cypher = f.read()

encode_table = {
    'A': 'H',
    'B': 'Z',
    'C': 'Y',
    'D': 'W',
    'E': 'O',
    'F': 'R',
    'G': 'J',
    'H': 'D',
    'I': 'P',
    'J': 'T',
    'K': 'I',
    'L': 'G',
    'M': 'L',
    'N': 'C',
    'O': 'E',
    'P': 'X',
    'Q': 'K',
    'R': 'U',
    'S': 'N',
    'T': 'F',
    'U': 'A',
    'V': 'M',
    'W': 'B',
    'X': 'Q',
    'Y': 'V',
    'Z': 'S'
}


decode_table = {value:key for key, value in encode_table.items()}

decode_table  = {}
for key, value in encode_table.items():
    decode_table[value] = key

def enctypt(s):
    result = ""
    for c in s:
        c = c.upper()
        if c.isalpha():
            result += encode_table[c]
        else:
            result += c

    return result



def decrypt(s):
    result = ""
    for c in s:
        c = c.upper()
        # print(c)
        if c.isalpha():
            result += decode_table[c]
            # print(result)
        else:
            result += c

    return result

# print(enctypt("HELLO, WORLD"))

print(decrypt("DOGGE, BEUGW"))
# ID EWKKF WDQSMDU ID JCW JIEW XB XSU, OCWD QXXU PIDQ CWDKF


# print(decrypt(cypher))

