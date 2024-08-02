import numpy as np


def key_matrix():
    enc_key = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]

    return enc_key


def removeSpaces(text):
    newText = ""
    for i in text:
        if i == " ":
            continue
        else:
            newText = newText + i
    return newText


def Trigraph(text):
    Trigraph = []
    group = 0
    text = text.replace(" ", "")
    for i in range(3, len(text), 3):
        Trigraph.append(text[group:i])

        group = i
    Trigraph.append(text[group:])

    return Trigraph


def encrypt(text, key):
    encrypted = list()
    trigraph = Trigraph(text)

    for tri in trigraph:
        row = list()
        for letter in tri:
            pos = ord(letter)-65
            row.append(pos)

        row = np.array(row)
        key = np.array(key)

        # Matrix Multiplication
        res = (np.dot(row, key)) % 26

        # Re-map
        res = list(res)

        enc = ""
        for p in res:
            p_chr = chr(p+65)
            enc += p_chr
        encrypted.append(enc)

    return encrypted


def decrypt(encrypted, key):
    key = np.array(key)
    det = np.mod(np.linalg.det(key), 26)
    k_inv = np.round(np.linalg.inv(key)*np.linalg.det(key))
    modulo_inv = np.mod((np.where(np.round(k_inv) < 0, np.round(
        k_inv)+26, np.round(k_inv))*pow(int(det), -1, 26)), 26)
    # print(modulo_inv)
    decrypted = list()
    for enc in encrypted:
        row = list()

        for letter in enc:
            pos = ord(letter)-65
            row.append(pos)

        row = np.array(row)
        res = np.dot(row, modulo_inv)
        res_mod = np.mod(np.round(res), 26)
        # print(res_mod)
        dec = ""
        for p in res_mod:
            p_chr = chr(int(p)+65)
            dec += p_chr
        decrypted.append(dec)

    return decrypted


if __name__ == '__main__':
    keys = key_matrix()

    word = input("Enter some text: ")
    encrypted = encrypt(word, keys)
    print(encrypted)

    decrypted = decrypt(encrypted, keys)
    print(' '.join(decrypted))
