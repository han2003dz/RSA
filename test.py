import math
import hashlib


hash_object = hashlib.md5(b'xin chao cac ban')
print(hash_object.hexdigest())

# import pandas as pd
# import PySimpleGUI as sg
# import math
# import random
# import main
# layout = [
#     # row 1
#     [
#         sg.Column([
#             [sg.Text("Tạo Khóa", text_color="blue", justification="center", background_color="#fff", size=(30, 1), font=("Arial", 16))]
#         ], background_color="#fff")
#     ],
#     # row 2
#     [
#         sg.Column([
#             [sg.Text("Chọn 2 số nguyên bất kỳ")],
#             [sg.Text("p"), sg.InputText(key="p_", size="40")],
#             [sg.Text("q"), sg.InputText(key="q_", size="40")],
#             [sg.Button("Tạo khóa", button_color = "blue"), sg.Button("Reset", button_color = "red")]
#         ], vertical_alignment='top'),
#         sg.Column([
#             [sg.Text("Khóa công khai", text_color = "blue")],
#             [sg.Text("e"), sg.Input(key="e_", size="40")],
#             [sg.Text("n"), sg.Input(key="n_", size="40")]
#         ], vertical_alignment='top'),
#         sg.Column([
#             [sg.Text("Khóa bí mật", text_color="blue")],
#             [sg.Text("d"), sg.Input(key="d_", size="40")],
#             [sg.Text("n"), sg.Input(key="n__", size="40")]
#         ], vertical_alignment='top'),
#     ],
#     # row 3
#     [
#         sg.Column([
#             [
#                 sg.Text("Phát sinh chữ kí", text_color="blue", justification="center", background_color="#fff")
#             ]
#         ], background_color="#fff", justification="center")
#     ],
#     # row 4
#     [
#         sg.Column([
#             [
#                 sg.Text("Văn bản cần kí:"),
#                 sg.InputText(key="-URL-", enable_events=True),
#                 sg.Button("Insert")
#             ]
#         ], justification='left', pad=(10, 0)),
#         sg.Column([
#             [
#                 sg.Text("Hàm băm:"),
#                 sg.Text("", size=(40, 1), key="-OUTPUT-"),
#                 sg.Button("Xóa", button_color="red")
#             ]
#         ], justification='left', pad= (10, 0)),
#     ],
#     # [
#     #     sg.Column([
#     #         [sg.Text("Chữ ký")],
#     #         [sg.Text("", size = (40, 10), key = "Chu_ky")]
#     #     ], justification='center'),
#     #     sg.Column([
#     #         [sg.Button("Save"), sg.Button("Chuyển")]
#     #     ], justification='center'),
#     # ]
#     [
#         sg.Column([
#             [sg.Button("Ký")]
#         ], background_color="#fff"),
#         sg.Column([
#             [
#                 sg.Text("Chữ ký")
#             ],
#             [
#                 sg.Text("", size=(40, 10), key="Chu_ky", background_color="white")
#             ]
#         ], justification='center'),
#         sg.Column([
#             [
#                 sg.Button("Save")
#             ],
#             [
#                 sg.Button("Chuyển")
#             ]
#         ], justification='center', background_color="#FFF"),
#     ]
# ]
# win = sg.Window("RSA", layout, background_color = "#FFF", size=(1000, 600))
#
# default_values = {
#     "p_": "",
#     "q_": "",
#     "e_": "",
#     "n_": "",
#     "d_": "",
#     "n__": "",
# }
# while True:
#     event, values = win.read()
#
#     if (event == sg.WIN_CLOSED or event == "Exit"):
#         break
#
#     elif (event == "Tạo khóa"):
#         p_value = int(values["p_"])
#         q_value = int(values["q_"])
#         e_value, n_value, d_value, n_value_2 = main.generate_keypair(p_value, q_value)
#         win["e_"].update(e_value)
#         win["n_"].update(n_value)
#         win["d_"].update(d_value)
#         win["n__"].update(n_value_2)
#     elif (event == "Reset"):
#         for key in default_values:
#             win[key].update(default_values[key])
#     elif event == "Insert":
#         url = values["-URL-"]
#         win["-OUTPUT-"].update(url)
#     elif event == "Xóa":
#         win["-OUTPUT-"].update("")
#
#
#
# #
# import PySimpleGUI as sg
# import hashlib
# import math
# import random
# class Rsa_DigitalSignature:
#     def __init__(self):
#         self.layout = [
#             [sg.Text("Tạo Khóa")],
#             [sg.Text("P:"), sg.Input(key='-P-')],
#             [sg.Text("Q:"), sg.Input(key='-Q-')],
#             [sg.Button('Tạo khóa'), sg.Button('Reset')],
#             [
#                 sg.Column([
#                     [sg.Button('Public key')],
#                     [sg.Button('Private key')]
#                 ]),
#                 sg.Column([
#                     [sg.Input(key='-PublicKey-', readonly=True)],
#                     [sg.Input(key='-PrivateKey-', readonly=True)]
#                 ])
#             ]
#         ]
#         self.window = sg.Window('RSA Digital Signature', self.layout)
#         self.is_running = True
#         self.default_values = {
#             '-P': "",
#             '-Q': "",
#             '-PublicKey-': "",
#             '-PrivateKey-': "",
#         }
#     # gcd
#     def gcd(self, a, b):
#         if b == 0:
#             return a
#         return self.gcd(b, a % b)
#     # số nguyên tố
#     def is_prime(self, n):
#         if n <= 1:
#             return False
#         for i in range(2, int(math.sqrt(n)) + 1):
#             if n % i == 0:
#                 return False
#         return True
#     # random số nguyên tố
#     def random_prime(self, phi):
#         while True:
#             num = random.randint(2, phi)  # Sinh số nguyên ngẫu nhiên trong khoảng từ 2 đến phi
#             if self.is_prime(num):  # Kiểm tra xem số đó có phải là số nguyên tố
#                 return num
#     # tạo khóa
#     def generate_keypair(self, p, q):
#         n = p * q
#         phi = (p-1)*(q-1)
#         e = self.random_prime(phi)
#         d = self.multiplicative_inverse(e, phi)
#         return e, n, d
#     # hàm nghịch đảo modulo
#     def multiplicative_inverse(self, e, phi):
#         def extended_gcd(a, b):
#             if b == 0:
#                 return a, 1, 0
#             gcd, x1, y1 = extended_gcd(b, a % b)
#             x = y1
#             y = x1 - (a // b) * y1
#             return gcd, x, y
#         gcd, d, _ = extended_gcd(e, phi)
#         if gcd == 1:
#             return d % phi
#         return None
#     def run(self):
#         while self.is_running:
#             event, values = self.window.read()
#             if event == sg.WINDOW_CLOSED:
#                 self.is_running = False
#             elif event == 'Tạo khóa':
#                 p = int(values['-P-'])
#                 q = int(values['-Q-'])
#                 e, n, d = self.generate_keypair(p, q)
#                 public_key = f'e: {e}, n: {n}'
#                 private_key = f'd: {d}, n:{n}'
#                 self.window['-PublicKey-'].update(public_key)
#                 self.window['-PrivateKey-'].update(private_key)
#             elif event == 'Reset':
#                 for key in self.default_values:
#                     self.window[key].update(self.default_values[key])
#         self.window.close()
# rsa = Rsa_DigitalSignature()
# rsa.run()


# doc = Document(file_path)
            # paragraphs = doc.paragraphs
            #
            # formatted_text = []
            # for paragraph in paragraphs:
            #     runs = paragraph.runs
            #     for run in runs:
            #         text = run.text
            #         font_name = run.font.name
            #         font_size = run.font.size
            #         font_color = run.font.color.rgb
            #         is_bold = run.font.bold
            #         is_italic = run.font.italic
            #         is_underline = run.font.underline
            #
            #         # Do something with the extracted formatting information
            #         formatted_text.append({
            #             'text': text,
            #             'font_name': font_name,
            #             'font_size': font_size,
            #             'font_color': font_color,
            #             'is_bold': is_bold,
            #             'is_italic': is_italic,
            #             'is_underline': is_underline
            #         })
            #
            # return formatted_text