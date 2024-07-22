def encrypt(text,key):
    res=""

    for k in text:
        if k.isupper():
            res+=chr((ord(k)+key-65)%26+65)
        elif k.islower():
            res+=chr((ord(k)+key-97)%26+97)
        elif k.isdigit():
            res+=chr((ord(k)+key-58)%10+48)
    return res

def decrypt(env,key):
    res=""
    for k in env:
        if k.isupper():
            res+=chr((ord(k)-key-65)%26+65)
        elif k.islower():
            res+=chr((ord(k)-key-97)%26+97)
        elif k.isdigit():
            res+=chr((ord(k)-key-48)%10+48)
    return res


if __name__=='__main__':
    message=input("Enter a message: ")
    shift=4

    res=encrypt(message,shift)
    print("Original: ",res)

    original=decrypt(res,shift)
    print("Decrypted: ",original)
