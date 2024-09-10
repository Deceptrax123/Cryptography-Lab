
def diffie_hellman(prime, base, private_key):
    return pow(base, private_key, prime)


def main():
    prime = 23
    base = 5

    private_key_A = 6
    private_key_B = 15

    public_key_A = diffie_hellman(prime, base, private_key_A)
    public_key_B = diffie_hellman(prime, base, private_key_B)

    print(f"Public Key of Party A: {public_key_A}")
    print(f"Public Key of Party B: {public_key_B}")

    shared_secret_A = diffie_hellman(prime, public_key_B, private_key_A)
    shared_secret_B = diffie_hellman(prime, public_key_A, private_key_B)

    print(f"Shared Secret Key (calculated by Party A): {shared_secret_A}")
    print(f"Shared Secret Key (calculated by Party B): {shared_secret_B}")


if __name__ == "__main__":
    main()
