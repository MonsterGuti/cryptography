def stream_cipher(text, key):
    result = ""

    for i in range(len(text)):
        char = ord(text[i])
        k = ord(key[i % len(key)])
        result += chr(char ^ k)

    return result


print("ИЗПРАЩАЧ")
text = input("Въведете текст: ")
key = input("Въведете таен ключ: ")

if key:
    encrypted = stream_cipher(text, key)
    print("Криптиран текст:", repr(encrypted))

    print("\nПОЛУЧАТЕЛ")
    receiver_key = input("Въведете ключ за декриптиране: ")

    if receiver_key == key:
        decrypted = stream_cipher(encrypted, receiver_key)
        print("Декриптиран текст:", decrypted)
    else:
        print("Грешен ключ!")
else:
    print("Ключът не трябва да бъде празен!")