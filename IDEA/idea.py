MOD = 0x10000
MASK = 0xFFFF


def mod_mul(x, y):
    if x == 0:
        x = MOD
    if y == 0:
        y = MOD
    res = (x * y) % 0x10001
    return res if res != MOD else 0


def mod_add(x, y):
    return (x + y) % MOD


def mod_sub(x, y):
    return (x - y) % MOD


def generate_subkeys(key):
    subkeys = []
    for i in range(0, 8):
        subkeys.append((key >> (112 - 16 * i)) & MASK)

    for i in range(8, 52):
        key = ((key << 25) | (key >> 103)) & (
            (1 << 128) - 1)
        subkeys.append((key >> 112) & MASK)

    return subkeys


def mul_inv(x):
    if x == 0:
        return 0
    else:
        for i in range(1, 0x10001):
            if mod_mul(x, i) == 1:
                return i
    return 0


def add_inv(x):
    return MOD - x


def idea_encrypt_block(plaintext, subkeys):
    x1 = (plaintext >> 48) & MASK
    x2 = (plaintext >> 32) & MASK
    x3 = (plaintext >> 16) & MASK
    x4 = plaintext & MASK

    for round in range(8):
        k = round * 6
        x1 = mod_mul(x1, subkeys[k])
        x2 = mod_add(x2, subkeys[k + 1])
        x3 = mod_add(x3, subkeys[k + 2])
        x4 = mod_mul(x4, subkeys[k + 3])

        t1 = x1 ^ x3
        t2 = x2 ^ x4

        t1 = mod_mul(t1, subkeys[k + 4])
        t2 = mod_add(t2, t1)
        t2 = mod_mul(t2, subkeys[k + 5])
        t1 = mod_add(t1, t2)

        x1 ^= t2
        x4 ^= t1
        x2 ^= t1
        x3 ^= t2

        x2, x3 = x3, x2

    x1 = mod_mul(x1, subkeys[48])
    x2 = mod_add(x3, subkeys[49])
    x3 = mod_add(x2, subkeys[50])
    x4 = mod_mul(x4, subkeys[51])

    ciphertext = (x1 << 48) | (x2 << 32) | (x3 << 16) | x4
    return ciphertext


def idea_decrypt_block(ciphertext, subkeys):
    inv_keys = [0] * 52
    for i in range(0, 48, 6):
        inv_keys[i] = mul_inv(subkeys[48 - i])
        inv_keys[i + 1] = add_inv(subkeys[49 - i])
        inv_keys[i + 2] = add_inv(subkeys[50 - i])
        inv_keys[i + 3] = mul_inv(subkeys[51 - i])
        if i != 42:
            inv_keys[i + 4] = subkeys[46 - i]
            inv_keys[i + 5] = subkeys[47 - i]

    return idea_encrypt_block(ciphertext, inv_keys)


def string_to_blocks(text):
    byte_array = text.encode('utf-8')

    padding_len = (8 - len(byte_array) % 8) % 8
    byte_array += b'\x00' * padding_len

    blocks = []
    for i in range(0, len(byte_array), 8):
        block = int.from_bytes(byte_array[i:i+8], byteorder='big')
        blocks.append(block)

    return blocks, padding_len


def blocks_to_string(blocks, padding_len):
    byte_array = b''.join(block.to_bytes(8, byteorder='big')
                          for block in blocks)

    return byte_array[:-padding_len].decode('utf-8')


def idea_encrypt_string(plaintext, subkeys):
    blocks, padding_len = string_to_blocks(plaintext)
    encrypted_blocks = [idea_encrypt_block(block, subkeys) for block in blocks]
    return encrypted_blocks, padding_len


key = 0x2BD6459F82C5B300952C49104881FF48
plaintext = "Srinitish Srinivasan"

subkeys = generate_subkeys(key)

encrypted_blocks, padding_len = idea_encrypt_string(plaintext, subkeys)
print(f"Encrypted blocks: {encrypted_blocks}")
