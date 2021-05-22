from typing import Sized
import PySimpleGUI
from PySimpleGUI import PySimpleGUI as sg

#Layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuario'),sg.Input(key='usuario', size=(20, 1))],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o Login?')],
    [sg.Button('Entrar')],
    [sg.Button('Cadastrar'),
    ]

]
#Janela
janela = sg.Window('CEU Engenharia', layout)
#Ler Eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['usuario'] == 'fabio' and valores['senha'] == '123456':
            print('Bem vindo a CEU!')
        else:
            print('Digite a Senha Correta!')
    if eventos == 'Cadastrar':
            print('Entre em nosso site e se cadastre!')