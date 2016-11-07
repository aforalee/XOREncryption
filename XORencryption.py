def encryptDecrypt(input):
    key = ['K', 'C', 'Q','E', 'R', 'T']  # Can be any chars, and any size array
    output = []

    for i in range(len(input)):
        xor_num = ord(input[i]) ^ ord(key[i % len(key)])
        output.append(chr(xor_num))

    return ''.join(output)


def main():
    encrypted = encryptDecrypt("data-to-encrypt");
    print("Encrypted:" + encrypted);

    decrypted = encryptDecrypt(encrypted);
    print("Decrypted:" + decrypted);
    pass


if __name__ == '__main__':
    main()
