
#Python

s_box = {
    '0': '3', '1': '4', '2': '1', '3': '2',
    '4': '0', '5': '9', '6': '7', '7': '6',
    '8': '5', '9': '8', 'A': 'D', 'B': 'C',
    'C': 'F', 'D': 'A', 'E': 'B', 'F': 'E'
}

inv_s_box = {value: key for key, value in s_box.items()}


def encrypt(block):
    result = ""
    for char in block.upper():
        result += s_box[char]
    return result


def decrypt(block):
    result = ""
    for char in block.upper():
        result += inv_s_box[char]
    return result


text = "FA01AD"

encrypted = encrypt(text)
print("а) Първоначален блок:", text)
print("   Криптиран блок:", encrypted)

encrypted_again = encrypt(encrypted)
print("б) Повторно криптиран блок:", encrypted_again)

decrypted = decrypt(encrypted)
print("в) Декриптиран блок:", decrypted)

current = text
iterations = 0

while True:
    current = encrypt(current)
    iterations += 1

    print("Итерация", iterations, ":", current)

    if current == text:
        break

print("Брой итерации до връщане на оригинала:", iterations)

