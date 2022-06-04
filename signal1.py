import matplotlib.pyplot as plt
import numpy as np


def get_time(data : list):
    return ([i / 500 for i in range(len(data))])[:90001]


def signal_print(x: list, y: list) -> None:
    y = y[:90001]
    plt.figure()
    # plt.title('ЕЕГ сигнал')
    # plt.xlabel('t, c')
    # plt.ylabel('A, V')
    plt.plot(x, y)
    plt.grid()
    # plt.savefig('EEG_signal')
    plt.show()


def amplitude_spectre(sign: list) -> list:
    # sign = sign[:90001]
    T = len(sign) / 500
    k = 2 * np.fft.rfft(sign)
    a = abs(k) / len(sign)
    return a


def remove_freqs(sign: list, freqs: list):
    new_sign = []
    new_freqs = []
    for i, j in zip(sign, freqs):
        if 1 <= j <= 100:
            new_sign.append(i)
            new_freqs.append(j)
    return new_sign, new_freqs


def norm(sign: list) -> list:
    return [i / sum(sign) for i in sign]


def correlate_func(sign1: list, sign2: list) -> list:
    return np.correlate(sign1, sign2, 'same')


def coherence(sign1: list, sign2: list) -> tuple:
    sign1 = correlate_func(sign1, sign1)
    sign2 = correlate_func(sign2, sign2)
    sign_12 = correlate_func(sign1, sign2)
    freqs = np.fft.rfftfreq(len(sign1), 1 / 500)
    sign1 = amplitude_spectre(sign1)
    sign2 = amplitude_spectre(sign2)
    sign_12 = amplitude_spectre(sign_12)
    # sign1, freq = remove_freqs(sign1, freqs)
    # sign2, freq = remove_freqs(sign2, freqs)
    # sign_12, freq = remove_freqs(sign_12, freqs)
    res = sign_12 ** 2 / (sign1 * sign2)
    return res, freqs

