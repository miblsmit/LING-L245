import sys

# A list of substitutions, the clear text side of the substitution is
# in capitals so we can distinguish which characters we have decrypted
# and which ones remain to be decrypted.
substitutions={'ა':'ɑ', 'ბ':'b', 'გ':'ɡ', 'დ':'d', 'ე':'ɛ', 'ვ':'v',

 'ზ':'z', 'თ':'tʰ', 'ი':'i', 'კ':'kʼ', 'ლ':'l', 'მ':'m', 'ნ':'n',

 'ო':'ɔ', 'პ':'pʼ', 'ჟ':'ʒ', 'რ':'r', 'ს':'s', 'ტ':'tʼ', 'უ':'u',

 'ფ':'pʰ', 'ქ':'kʰ', 'ღ':'ɣ', 'ყ':'qʼ', 'შ':'ʃ', 'ჩ':'tʃʰ', 'ც':'tsʰ',

 'ძ':'dz', 'წ':'tsʼ', 'ჭ':'tʃʼ', 'ხ':'χ', 'ჯ':'dʒ', 'ჰ':'h',}
# For each of the lines in the input
for line in sys.stdin.readlines():
    # A variable to contain the result of decoding this line
    result = ''
    # For each of the characters in the line except newline
    for c in line.strip():
        # If the character is in our list of substitutions
        if c in substitutions:
            # append the character to the result variable
            result += substitutions[c]
        else:
            # otherwise append the cypher character
            result += c
    # Print out the line
    print(result)


