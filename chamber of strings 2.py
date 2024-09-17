def decrypt_cryptogram(cryptogram, shift):
    decrypted_text = ''
    
    for char in cryptogram:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            ascii_value = ord(char)
            decrypted_ascii_value = (ascii_value - ascii_offset - shift) % 26 + ascii_offset
            decrypted_char = chr(decrypted_ascii_value)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char

    return decrypted_text

cryptogram = 'VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR'

for shift in range(1, 26):
    decrypted_text = decrypt_cryptogram(cryptogram, shift)
    print(f'Shift: {shift}, Decrypted Text: {decrypted_text}')
