import math
import random
import hashlib
import chardet
from unidecode import unidecode
import docx
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def phi_n(p, q):
    if is_prime(p) and is_prime(q):
        phi = (p - 1) * (q - 1)
        return phi
def euclid(e, phi):
    x1, x2, y1, y2 = 1, 0, 0, 1
    a, b = e, phi
    while b != 0:
        q = a // b
        a, b = b, a - q * b
        x1, x2 = x2, x1 - q * x2
        y1, y2 = y2, y1 - q * y2
    if a == 1:
        return x1 % phi
    else:
        raise ValueError("The multiplicative inverse does not exist")


def public_key(p, q):
    phi = phi_n(p, q)
    while True:
        b = random.randrange(2, phi)
        if gcd(b, phi) == 1:
            return b


def MD5(mess):
    mess_bytes = mess.encode('utf-8')
    hash_object = hashlib.md5(mess_bytes)
    toHex = hash_object.hexdigest()
    return toHex


def PowMod(base, exponent, modulus):
    if exponent == 0:
        return 1

    result = 1
    baseValue = base % modulus
    exp = exponent

    while exp > 0:
        if exp % 2 == 1:
            result = (result * baseValue) % modulus

        baseValue = (baseValue * baseValue) % modulus
        exp = exp // 2

    if result < 0:
        result = (result + modulus) % modulus

    return result


def decimal(hex):
    res = ""
    for val in hex:
        value = int(val, 16)
        res = res + str(value) + '-'
    return res[:-1]


def chu_ky(text, p, q):
    res = MD5(text)
    dcm = decimal(res)
    elements = dcm.split('-')
    a = []
    for el in elements:
        if '-' not in el:
            val = PowMod(int(el), public_key(p, q), p*q)
            a.append(val)
    return a

def save_data_to_file(file_path, data):
    if file_path.endswith('.txt'):
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(data)
        print(f"File saved successfully: {file_path}")
    elif file_path.endswith('.docx'):
        doc = docx.Document()
        doc.add_paragraph(data)
        doc.save(file_path)
        print(f"File saved successfully: {file_path}")
    else:
        print("Invalid file format. Please select a valid file type.")

if __name__ == "__main__":
    p = 17
    q = 19
    res = MD5("xin chào các bạn")
    dcm = decimal(res)
    e = public_key(p, q)
    n = p * q
    print(res)
    print(dcm)
    print(chu_ky("xin chào các bạn", 61, 53))
    b = "a-b-c-a-d"
    c = b.split("-")
    print(c)
    p = 19  # Giá trị p
    q = 17  # Giá trị q
    input_text = "xin chào các bạn"
    arr = [311, 63, 177, 269, 9, 14, 213, 1, 155, 316, 1, 179, 268, 93, 48, 53, 54, 297, 253, 1, 15, 44, 215, 184, 98,
           280, 159, 197, 109, 0, 175, 235]

    # Chuyển đổi mảng số nguyên thành chuỗi kết quả
    result = ""
    for num in arr:
        inverse = pow(public_key(p, q), -1, (p - 1) * (q - 1))
        decrypted_num = PowMod(num, inverse, p * q)
        hex_str = hex(decrypted_num)[2:]  # Chuyển đổi thành chuỗi số thập lục phân
        hex_str = hex_str.zfill(2)  # Đảm bảo chuỗi có 2 ký tự
        result += hex_str

    # So sánh chuỗi kết quả với giá trị băm MD5
    if result == MD5(input_text):
        print("Kết quả chính xác:", result)
    else:
        print("Kết quả không chính xác.", result)







