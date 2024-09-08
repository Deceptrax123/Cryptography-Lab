def ksa(key):
    key_length = len(key)
    S = list(range(256))
    j = 0

    for i in range(256):
        j = (j + S[i] + key[i % key_length]) % 256
        S[i], S[j] = S[j], S[i]

    return S


def prga(S):
    i = 0
    j = 0
    while True:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        yield K


def rc4(key, plaintext):
    key = [ord(c) for c in key]
    S = ksa(key)
    keystream = prga(S)

    ciphertext = ''.join([chr(ord(c) ^ next(keystream)) for c in plaintext])
    return ciphertext


key = "21bai1394"
plaintext = "Srinitish Srinivasan"

ciphertext = rc4(key, plaintext)
print(f"Encrypted: {ciphertext}")

decrypted = rc4(key, ciphertext)
print(f"Decrypted: {decrypted}")
