text='Hello Zaira'
custom_key='python'
def vignere(message, key):
    key_index=0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text=''
    for char in message.lower():
        #Append space to the message
        if char==' ':
            encrypted_text+=char
    else:
        index=alphabet.find(char)
        new_index=(index+offset)%len(alphabet)
        encrypted_text += alphabet[new_index]
    print('plain text:', message)
    print('encrypted_text:', encrypted_text)