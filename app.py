
import PySimpleGUI as sg
import math
import random
import docx
import hashlib
from docx import Document
import docx2txt
import chardet
from unidecode import unidecode
from docx.shared import RGBColor
class RsaDigitalSignature:
    sg.set_options(font=("Arial Bold", 12))
    def __init__(self):

        self.layout = [
            # row 1
            [sg.Text("Tạo Khóa")],
            # row 2
            [sg.Text("P:"), sg.Input(key='-P-')],
            # row 3
            [sg.Text("Q:"), sg.Input(key='-Q-')],
            # row 4
            [
                sg.Column([
                    [sg.Button('Tạo khóa', button_color='blue'), sg.Button('Reset', button_color='red')]
                ], justification='left'),
            ],
            # row 5
            [
                # col 1 - row 5
                sg.Column([
                    [sg.Button('Public key', size=(10, 1))],
                    [sg.Button('Private key', size=(10, 1), button_color='red')]
                ]),
                # col 2 - row 5
                sg.Column([
                    [sg.Input(key='-PublicKey-', readonly=True, size=(33, None))],
                    [sg.VerticalSeparator()],
                    [sg.Input(key='-PrivateKey-', readonly=True, size=(33, None))]
                ]),
            ],
            [
                sg.Column([
                    [sg.Text("Văn bản cần ký")],
                    [sg.Multiline('', size=(45,5), key='-Input-'), sg.Button('File', button_color='blue')],
                    [
                        sg.Column([
                            [sg.Button('Ký', size=(10, 1))]
                        ], justification="center")
                    ],
                    [
                        sg.Text('Hàm băm'), sg.Input('', key='-MD5-', readonly=True, size=(43, None))
                    ],
                    [sg.Text("Chữ ký")],
                    [sg.Multiline('', size=(45, 5), key='-OutputText-')],
                    [
                        sg.Column([
                            [sg.Button('Chuyển', button_color='blue'), sg.Button('Save', button_color='blue')]
                        ],justification='center')
                    ],
                ], justification='left'),
                sg.VerticalSeparator(),
                sg.Column([
                    [sg.Text("Văn bản ký")],
                    [sg.Multiline('', size=(45, 5), key='-Input-'), sg.Button('File văn bản', button_color='blue', size=(10, 1))],
                    [sg.Text("Chữ ký")],
                    [sg.Multiline('', size=(45, 5), key='-OutputText-'), sg.Button('File chữ ký', button_color='blue', size=(10, 1))],
                    [sg.Button('Kiểm tra', button_color='blue')],
                ], justification='top'),

            ],

        ]

        self.window = sg.Window('RSA Digital Signature', self.layout, size=(1200, 650))
        self.is_running = True
        self.default_values = {
            '-P-': "",
            '-Q-': "",
            '-PublicKey-': "",
            '-PrivateKey-': "",
        }
    # gcd
    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a
    # số nguyên tố
    def is_prime(self, n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True
    # random số nguyên tố
    def random_prime(self, phi):
        while True:
            num = random.randint(2, phi)
            if self.is_prime(num):
                return num
    # hàm tạo khóa
    def generate_keypair(self, p, q):
        n = p * q
        phi = (p - 1) * (q - 1)
        e = self.random_prime(phi)
        d = self.multiplicative_inverse(e, phi)
        return e, n, d

    # Eculid mở rộng để tìm nghịch đảo nhân modulo
    def multiplicative_inverse(self, e, phi):
        def extended_gcd(a, b):
            if b == 0:
                return a, 1, 0
            gcd, x1, y1 = extended_gcd(b, a % b)
            x = y1
            y = x1 - (a // b) * y1
            return gcd, x, y

        gcd, x, y = extended_gcd(e, phi)
        if gcd == 1:
            return x % phi
        return None

    # hàm đọc file
    def read_file(self, file_path):

        if file_path.endswith('.txt'):
            with open(file_path, 'rb') as file:
                raw_data = file.read()
                detected_result = chardet.detect(raw_data)
                detected_encoding = detected_result['encoding']
                file_content = raw_data.decode(detected_encoding)
                return file_content

        elif file_path.endswith('.docx'):
            doc = Document(file_path)
            paragraphs = doc.paragraphs

            formatted_text = []
            for paragraph in paragraphs:
                text = paragraph.text
                formatted_text.append(text)

            return '\n'.join(formatted_text)
        else:
            return "Unsupported file format."
    # 10 -> nhị phân
    def decimal_to_binary(self, number):
        if number == 0:
            return "0"  # Xử lý khi số đầu vào là 0
        binary = ""
        while number > 0:
            binary = str(number % 2) + binary  # Lấy phần dư của số cho 2 và thêm vào phía trước chuỗi kết quả
            number //= 2  # Chia số cho 2 để lấy phần nguyên
        return binary
# `   bình phương và nhân
    def square_and_multiply(self, value, e, n):
        result = 1
        binary_exponent = self.decimal_to_binary(e)
        for bit in binary_exponent:
            result = (result ** 2) % n
            if bit == '1':
                result = (result * value) % n
        return result

    # hàm băm MD5
    def MD5(self, mess):
        mess_bytes = mess.encode('utf-8')
        # Tính toán giá trị băm
        hash_object = hashlib.md5(mess_bytes)
        toHex = hash_object.hexdigest()
        return toHex
    #
    def input(self, values):
        p = int(values['-P-'])
        q = int(values['-Q-'])
        e, n, d = self.generate_keypair(p, q)
    def MD5toDecimal(self, values):
        p = int(values['-P-'])
        q = int(values['-Q-'])
        e, n, d = self.generate_keypair(p, q)
        arr = []
        string = str(self.MD5)
        for char in string:
            decimal_element = self.hex_to_decimal(char)
            res = self.square_and_multiply(decimal_element, e, n)
            arr.append(res)
    # chuyển từ hệ 16 -> 10
    def hex_to_decimal(self, hex_number):
        decimal = int(hex_number, 16)
        return decimal
    # hàm ký
    def Ky(self, values):
        mess = values['-Input-']
        messToHex = self.MD5(mess)
        self.window['-MD5-'].update(messToHex)

    # run
    def run(self):

        while self.is_running:

            event, values = self.window.read()
            if event == sg.WINDOW_CLOSED:
                self.is_running = False

            elif event == 'Tạo khóa':
                p = int(values['-P-'])
                q = int(values['-Q-'])
                if p <= 1 or q <= 1:
                    sg.popup('P và Q phải là số nguyên lớn hơn 1')
                    continue
                if not self.is_prime(p) or not self.is_prime(q):
                    sg.popup('P và Q phải là số nguyên tố')
                    continue
                e, n, d = self.generate_keypair(p, q)
                public_key = f'e: {e}, n: {n}'
                private_key = f'd: {d}, n: {n}'
                self.window['-PublicKey-'].update(public_key)
                self.window['-PrivateKey-'].update(private_key)

            elif event == 'Reset':
                for key in self.default_values:
                    self.window[key].update(self.default_values[key])

            elif event == 'File':
                file_path = sg.popup_get_file('Select a file',
                                              file_types=(('Text Files', '*.txt'),
                                                          ('Word Documents', '*.docx')))
                if file_path:
                    file_content = self.read_file(file_path)
                    self.window['-Input-'].update(file_content)
            elif event == "Ký":
                self.Ky(values)

            elif event == "Kiểm tra":
                sg.popup("Thông báo ra màn hình", title="Check RSA", background_color='lightblue', text_color='red')
        self.window.close()

rsa = RsaDigitalSignature()
rsa.run()
