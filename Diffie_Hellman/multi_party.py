
def diffie_hellman(prime, base, private_key):
    return pow(base, private_key, prime)


def main():
    prime = 23
    base = 5

    private_key_A = 6
    private_key_B = 15
    private_key_C = 13

    public_key_A = diffie_hellman(prime, base, private_key_A)
    public_key_B = diffie_hellman(prime, base, private_key_B)
    public_key_C = diffie_hellman(prime, base, private_key_C)

    print(f"Public Key of Party A: {public_key_A}")
    print(f"Public Key of Party B: {public_key_B}")
    print(f"Public Key of Party C: {public_key_C}")

    intermediate_A_B = diffie_hellman(prime, public_key_B, private_key_A)

    intermediate_B_C = diffie_hellman(prime, public_key_C, private_key_B)

    intermediate_C_A = diffie_hellman(prime, public_key_A, private_key_C)

    print(f"Intermediate Key A-B: {intermediate_A_B}")
    print(f"Intermediate Key B-C: {intermediate_B_C}")
    print(f"Intermediate Key C-A: {intermediate_C_A}")

    final_key_A = diffie_hellman(prime, intermediate_B_C, private_key_A)

    final_key_B = diffie_hellman(prime, intermediate_C_A, private_key_B)

    final_key_C = diffie_hellman(prime, intermediate_A_B, private_key_C)

    print(f"Final Shared Key (calculated by Party A): {final_key_A}")
    print(f"Final Shared Key (calculated by Party B): {final_key_B}")
    print(f"Final Shared Key (calculated by Party C): {final_key_C}")


if __name__ == "__main__":
    main()
