import os
import mne


def file_reader():
    files = []
    for i in os.listdir(os.getcwd() + '\\EEG\\files'):
        if i[-3:] == 'edf':
            files.append(i)
    return files


def get_datum(file):
    path = os.getcwd() + '\\EEG\\files\\' + file
    data = mne.io.read_raw_edf(path)
    raw_data = data.get_data()
    info = data.info
    return raw_data, info


# print(get_datum('Анохин_АЮ_6.07.2015_1.edf'))