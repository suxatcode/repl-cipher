def cipher(alphabets, plaintext):
    a1, a2 = alphabets
    assert len(a1) == len(a2), "length of alphabets should be equal"
    ciphertext = ""
    for char in plaintext:
        try:
            i = a1.index(char)
            ciphertext += a2[i]
        except ValueError:
            ciphertext += char
    return ciphertext
