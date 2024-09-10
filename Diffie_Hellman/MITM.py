
def diffie_hellman(prime, base, private_key):
    return pow(base, private_key, prime)


def main():
    prime = 23
    base = 5

    private_key_A = 6
    private_key_B = 15

    private_key_eve = 10

    public_key_A = diffie_hellman(prime, base, private_key_A)
    public_key_B = diffie_hellman(prime, base, private_key_B)

    public_key_eve = diffie_hellman(prime, base, private_key_eve)

    public_key_A_received_by_eve = public_key_eve

    public_key_B_received_by_eve = public_key_eve

    print(f"Public Key of Party A (intercepted by Eve): {
          public_key_A_received_by_eve}")
    print(f"Public Key of Party B (intercepted by Eve): {
          public_key_B_received_by_eve}")

    shared_secret_A_eve = diffie_hellman(
        prime, public_key_A_received_by_eve, private_key_A)

    shared_secret_B_eve = diffie_hellman(
        prime, public_key_B_received_by_eve, private_key_B)

    shared_secret_eve_A = diffie_hellman(prime, public_key_A, private_key_eve)
    shared_secret_eve_B = diffie_hellman(prime, public_key_B, private_key_eve)

    print(f"Shared Secret A (calculated by A with Eve): {shared_secret_A_eve}")
    print(f"Shared Secret B (calculated by B with Eve): {shared_secret_B_eve}")
    print(f"Shared Secret (calculated by Eve with A): {shared_secret_eve_A}")
    print(f"Shared Secret (calculated by Eve with B): {shared_secret_eve_B}")


if __name__ == "__main__":
    main()
