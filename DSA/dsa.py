import random

p = 23
g = 5


def key_generation():
    x = random.randint(1, p - 2)
    y = pow(g, x, p)
    return x, y


def sign(message, p, g, x):
    k = random.randint(1, p - 2)
    r = pow(g, k, p)
    k_inv = pow(k, -1, p - 1)

    h = hash(message) % (p - 1)

    s = (h - x * r) * k_inv % (p - 1)

    return (r, s)


def verify(message, p, g, y, signature):
    r, s = signature

    if not (0 < r < p):
        return False

    h = hash(message) % (p - 1)

    v1 = pow(g, h, p)
    v2 = (pow(y, r, p) * pow(r, s, p)) % p

    return v1 == v2


message = "Srinitish"

private_key, public_key = key_generation()

signature = sign(message, p, g, private_key)

is_valid = verify(message, p, g, public_key, signature)

print("Signature:", signature)
print("Is the signature valid?", is_valid)
