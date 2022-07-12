import PySimpleGUI as sg
from stored import Data

sg.theme('Dark Blue 1')

layout = [[sg.Text('Choose the type of exercise')],
          [sg.OptionMenu(['Dumbbell', 'Barbell', 'Calisthenics'], s=(40, 1))],
          [sg.Text('Input the weight')],
          [sg.InputText('Enter', key='-WEIGHT-')],
          [sg.Text('Input the sets')],
          [sg.InputText('Enter', key='-SETS-')],
          [sg.Text('Input the reps')],
          [sg.InputText('Enter', key='-REPS-')],
          [sg.Button('Submit'), sg.Exit()]]

window = sg.Window('Progressive Overload Calculator', layout, no_titlebar=True, grab_anywhere=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
        break
    gathereddata = Data(values[0],values['-WEIGHT-'],values['-SETS-'],values['-REPS-'])
    checked = gathereddata.checkdata()
    if checked == False:
        sg.popup('Your input is incorrect, please ensure you put in numbers.')
        continue
    podata = gathereddata.overload()
    if podata == False:
        sg.popup('Unfortunately, we are still working on a computing model for calisthenic exercises.')
        continue
    sg.popup(f'You should be doing {gathereddata.sets} sets of {podata[1]} reps each, with {podata[0]} pounds.')
window.close()