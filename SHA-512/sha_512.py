K = [0x428a2f98d728ae22, 0x7137449123ef65cd]

H = [0x6a09e667f3bcc908, 0xbb67ae8584caa73b]


def right_rotate(value, bits):
    return ((value >> bits) | (value << (64 - bits))) & 0xFFFFFFFFFFFFFFFF

# Pad Message


def pad_message(message):
    original_byte_len = len(message)
    original_bit_len = original_byte_len * 8

    message += b'\x80'

    while (len(message) * 8) % 1024 != 896:
        message += b'\x00'

    message += original_bit_len.to_bytes(16, 'big')
    return message

# One round of operation


def sha512_one_round(message):
    padded_message = pad_message(message)

    chunks = [padded_message[i:i + 128]
              for i in range(0, len(padded_message), 128)]

    for chunk in chunks:
        w = [int.from_bytes(chunk[i:i + 8], 'big') for i in range(0, 128, 8)]

        for i in range(16, 18):
            s0 = right_rotate(
                w[i - 15], 1) ^ right_rotate(w[i - 15], 8) ^ (w[i - 15] >> 7)
            s1 = right_rotate(
                w[i - 2], 19) ^ right_rotate(w[i - 2], 61) ^ (w[i - 2] >> 6)
            w.append((w[i - 16] + s0 + w[i - 7] + s1) & 0xFFFFFFFFFFFFFFFF)

        a, b = H[0], H[1]

        for i in range(1):
            S1 = right_rotate(b, 14) ^ right_rotate(
                b, 18) ^ right_rotate(b, 41)
            ch = (b & a) ^ ((~b) & w[i])
            temp1 = (H[1] + S1 + ch + K[i] + w[i]) & 0xFFFFFFFFFFFFFFFF
            S0 = right_rotate(a, 28) ^ right_rotate(
                a, 34) ^ right_rotate(a, 39)
            maj = (a & b) ^ (a & w[i]) ^ (b & w[i])
            temp2 = (S0 + maj) & 0xFFFFFFFFFFFFFFFF

            b = (temp1 + temp2) & 0xFFFFFFFFFFFFFFFF

        H[0] = (H[0] + a) & 0xFFFFFFFFFFFFFFFF
        H[1] = (H[1] + b) & 0xFFFFFFFFFFFFFFFF

    return H


message = b"Srinitish Srinivasan"
print("Plain Text: ", message)
print("Message after Padding and Length Field: ", pad_message(message))
hashed_values = sha512_one_round(message)
print(f"Hashed output (1 round): {hashed_values}")
