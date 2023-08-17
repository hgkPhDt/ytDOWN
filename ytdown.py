import PySimpleGUI as sg
from pytube import YouTube

SAVE_PATH = "C:\\Users\\apus5\\Downloads\\"

#Layout
sg.theme('DarkAmber')
layout = [
    [sg.Text('======================== Baixe vídeos e áudios do youtube! ========================' )],
    [sg.Text('Baixar vídeo:', size=(10,1)), sg.Input(key='-VIDEO-', size=(56, 1)), sg.Button('Baixar video', size=(10,1))],
    [sg.Text('Baixar áudio:', size=(10,1)), sg.Input(key='-AUDIO-', size=(56, 1)), sg.Button('Baixar audio', size=(10,1))],
    [sg.Text('by: Philip Torres')]
]
#Janela
janela = sg.Window('ytDOWN!', layout)
#Eventos

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break

    if eventos == 'Baixar video':
        url = valores['-VIDEO-']
        yt = YouTube(url)
        #filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        yt.streams.get_highest_resolution().download(SAVE_PATH)
        print(yt.title)
    
    if eventos == 'Baixar audio':
        url = valores['-AUDIO-']
        yt = YouTube(url)
        yt.streams.filter(only_audio=True)[0].download(SAVE_PATH)

janela.close()