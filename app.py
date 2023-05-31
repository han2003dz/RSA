import pandas as pd
import PySimpleGUI as sg
import math
import random
from main import *
layout = [
    # row 1
    [
        sg.Column([
            [sg.Text("Tạo Khóa", text_color="blue", justification="center", background_color="#fff", size=(30, 1))]
        ], background_color="#fff")
    ],
    # row 2
    [
        sg.Column([
            [sg.Text("Chọn 2 số nguyên bất kỳ")],
            [sg.Text("p"), sg.InputText(key="p_", size="40")],
            [sg.Text("q"), sg.InputText(key="q_", size="40")],
            [sg.Button("Tạo khóa", button_color = "blue"), sg.Button("Reset", button_color = "red")]
        ], vertical_alignment='top'),
        sg.Column([
            [sg.Text("Khóa công khai", text_color = "blue")],
            [sg.Text("e"), sg.Input(key="e_", size="40")],
            [sg.Text("n"), sg.Input(key="n_", size="40")]
        ], vertical_alignment='top'),
        sg.Column([
            [sg.Text("Khóa bí mật", text_color="blue")],
            [sg.Text("d"), sg.Input(key="d_", size="40")],
            [sg.Text("n"), sg.Input(key="n__", size="40")]
        ], vertical_alignment='top'),
    ],
    # row 3
    [
        sg.Column([
            [
                sg.Text("Phát sinh chữ kí", text_color="blue", justification="center", background_color="#fff")
            ]
        ], background_color="#fff", justification="center")
    ],
    # row 4
    [
        sg.Column([
            [
                sg.Text("Văn bản cần kí:"),
                sg.InputText(key="-URL-", enable_events=True),
                sg.Button("Insert")
            ]
        ], justification='left'),
        sg.Column([
            [
                sg.Text("Hàm băm:"),
                sg.Text("", size=(40, 1), key="-OUTPUT-"),
                sg.Button("Xóa", button_color="red")
            ]
        ], justification='left'),
    ],
    # [
    #     sg.Column([
    #         [sg.Text("Chữ ký")],
    #         [sg.Text("", size = (40, 10), key = "Chu_ky")]
    #     ], justification='center'),
    #     sg.Column([
    #         [sg.Button("Save"), sg.Button("Chuyển")]
    #     ], justification='center'),
    # ]
    [
        sg.Column([
            [
                sg.Text("Chữ ký")
            ],
            [
                sg.Text("", size=(40, 10), key="Chu_ky", background_color="white")
            ]
        ], justification='center'),
        sg.Column([
            [
                sg.Button("Ký")
            ],
            [
                sg.Button("Save")
            ],
            [
                sg.Button("Chuyển")
            ]
        ], justification='center', background_color="#FFF"),
    ]
]
win = sg.Window("RSA", layout, background_color = "#FFF", size=(1000, 600))

default_values = {
    "p_": "",
    "q_": "",
    "e_": "",
    "n_": "",
    "d_": "",
    "n__": "",
}

while True:
    event, values = win.read()

    if (event == sg.WIN_CLOSED or event == "Exit"):
        break

    elif (event == "Tạo khóa"):
        p_value = int(values["p_"])
        q_value = int(values["q_"])
        e_value, n_value, d_value, n_value_2 = generate_keypair(p_value, q_value)
        win["e_"].update(e_value)
        win["n_"].update(n_value)
        win["d_"].update(d_value)
        win["n__"].udate(n_value_2)
    elif (event == "Reset"):
        for key in default_values:
            win[key].update(default_values[key])
    elif event == "Insert":
        url = values["-URL-"]
        win["-OUTPUT-"].update(url)
    elif event == "Xóa":
        win["-OUTPUT-"].update("")




