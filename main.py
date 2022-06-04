from files import *
from signal1 import coherence, signal_print
from TE import symbolic_transfer_entropy as te1
import random
import scipy.signal
import pprint
import matplotlib.pyplot as plt
from matplotlib import cm
from freq_lib import sign_1
from copent import transent, ci
from TE_own import te_calc
import time

files = file_reader()
file = files[0]
print(files[0])
signals, info = get_datum(file)
ch_names = info['ch_names']
ch_names = [i[4:] for i in ch_names]
print(ch_names)

# time = get_time(signals[0])
# am_spec1, freqs = amplitude_spectre(signals[0])
# am_spec2, _  = amplitude_spectre(signals[6])
# am_spec1, freqs = remove_freqs(am_spec1, freqs)
# am_spec2, _ = remove_freqs(am_spec2, _)
# am_spec1 = norm(am_spec1)
# am_spec2 = norm(am_spec2)
# print('Entropy calculating started ...')
# TE_dict = {}
# for i in range(20):
#     for j in range(i + 1, 20):
#         TE_dict[f'{i}_to_{j}'] = symbolic_transfer_entropy(signals[i], signals[j])
# file = files[1]
# signals = get_datum(file)
# TE_dict2 = {}
# print('Entropy calculating started ...')
# for i in range(20):
#     for j in range(i + 1, 20):
#         TE_dict2[f'{i}_to_{j}'] = symbolic_transfer_entropy(signals[i], signals[j])
# for i in TE_dict.keys():
#     print(f"{i}\n Test 1: {TE_dict[i]}\n Test 2: {TE_dict2[i]}")
# print(te1(signals[0], signals[1]))
# print(te1(signals[1], signals[0]))
# coh_12, freq = coherence(signals[1], signals[19])
# signal_print(freq, coh_12)
# print(te1(signals[0], signals[1]))
# te_l = {}
# te_l['a'] = {}
# te_l['a']['b'] = 0
# te_l['a']['c'] = 4
# te_l['a']['q'] = 2
# te_l['c'] = {}
# te_l['c']['a'] = 1
# te_l['c']['b'] = 3
# te_l['c']['v'] = 5
# te_l['c']['x'] = 7
# te_l['a']['x'] = 9
# for numb, i in enumerate(te_l):
#     print(numb)
#     for j in te_l[i].keys():
#         print(te_l[i][j])
# TE_list = {}
# for i in range(19):
#     TE_list[f'{ch_names[i]}'] = {}
#     for j in range(19):
#         if i == j:
#             continue
#         print(i, j)
#         TE_list[f'{ch_names[i]}'][f'{ch_names[j]}'] = te1(signals[i], signals[j])
#         freq_lib, coh_12_lib = scipy.signal.coherence(signals[i], signals[j], 500)
#         signal_print(freq_lib, coh_12_lib) 
# pprint.pprint(TE_list)
# TE_list = sign_1
# fig, ax = plt.subplots(nrows=5, ncols=4, figsize=(25,3))
# fig.suptitle('TE')
# j = 0
# for i, _from in enumerate(TE_list):
#     data = {}
    
#     for _to in TE_list[_from].keys():
#         data.update({_to: TE_list[_from][_to]})
#     print(data)
#     vmin = min(data.values())
#     vmax = max(data.values())
#     im = viz_one_head(map=data, axes=ax[i % 5][j], vmin=1.85, vmax=2.1, title=_from)
#     j += 1
#     if j > 3:
#         j = 0
 

# fig.subplots_adjust(right=0.8, top=0.9)
# cbar_ax = fig.add_axes([0.85, 0.1, 0.01, 0.8])
# norm = cm.colors.Normalize(vmin=1.85, vmax=2.1)
# fig.colorbar(cm.ScalarMappable(norm=norm, cmap='RdBu_r'), cax=cbar_ax, shrink=0.6)
# plt.show()

# coherence_map(coh_dict=TE_list, line_color='green', line_width=0.4)
# te_1 = te1([1, 2, 3, 4, 5], [4, 1, 2, 3, 5])
# print(te_1)
# te_2 = transent(signals[0], signals[1], mode=2)
# print(te_2)
# print(time.time())
# te_3 = te_calc(signals[0][:30000], signals[1][:30000])
# print(te_3)
# print(time.time())
_dict = {{}}
_dict['a']['b'] = 1
print(_dict)