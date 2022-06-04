import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection, LineCollection
from matplotlib.colors import ListedColormap
import mne
from freq_lib import sign_1 as TE_list
import numpy as np
from matplotlib import colors as mcolors


def TE_map(main_key, te_dict, line_color, line_width, axes=None, fig=None, title=None, pos=None):
    SignalLabels = []
    SignalLabels.append(main_key)
    for key in te_dict.keys():
        SignalLabels.append(key)
    montage = mne.channels.read_montage(kind="standard_1020", unit='mm', ch_names=SignalLabels).get_pos2d()
    new_signal_labels = mne.channels.read_montage(kind="standard_1020", unit='mm', ch_names=SignalLabels).ch_names
    x_axis = montage[:, 0]
    y_axis = montage[:, 1]
    point_coords = np.array((x_axis, y_axis))
    patches = []
    color_list = []
    values_list = []
    ch_1 = []
    ch_2 = []

    for key_2 in SignalLabels:
        if key_2 == main_key:
            continue
        ch_1.append(main_key)
        ch_2.append(key_2)
        values_list.append(te_dict[key_2])
    vmin, vmax = min(values_list), max(values_list)

    te_dict = {'leads': [ch_1, ch_2], 'te_vals': values_list}
    param_values = te_dict["te_vals"]
    lead_names = te_dict["leads"]
    lead_nums = [[new_signal_labels.index(i) for i in lead_names[0]], [new_signal_labels.index(i) for i in lead_names[1]]]

    if axes is None and fig is None:
        fig, axes = plt.subplots(figsize=(5, 5))  # note we must use plt.subplots, not plt.subplot
    plt.grid(True)
    axes.axis('equal')
    lines = np.transpose(
        np.array([[x_axis[lead_nums[0]], x_axis[lead_nums[1]]],
                  [y_axis[lead_nums[0]], y_axis[lead_nums[1]]]]), (2, 1, 0))
    line_segments = LineCollection(lines,
                                   linewidths=values_list,
                                   linestyles='solid',
                                   zorder=1,
                                   colors=colors)
    axes.add_collection(line_segments)
    for x, y in zip(x_axis, y_axis):
        circle = Circle((x, y), radius=0.10, color='mediumseagreen', edgecolor='forestgreen', linewidth=1.5)
        circle.set_edgecolor('darkgreen')
        axes.add_artist(circle)
        color_list.append('forestgreen')
        patches.append(circle)
    font = {'family': 'serif',
            'color': 'black',
            'size': 7,
            }
    for i, label in enumerate(new_signal_labels):
        axes.text(point_coords[0][i] + 0.1, point_coords[1][i] + 0.1, label, fontdict=font)
    axes.set_title(title, fontsize=10)
    axes.set_xlim(-3, 3)
    axes.set_ylim(-3, 3)

    axes.axis('off')
    plt.grid(False)

    return axes



if __name__ == '__main__':
    fig, spaxs = plt.subplots(nrows=5, ncols=4, figsize=(36, 24))
    values = []
    for key_1 in TE_list.keys():
        for key_2 in TE_list[key_1].keys():
            values.append(TE_list[key_1][key_2])
    vmax = max(values)
    vmin = min(values)
    del values
    j = 0
    for q, key in enumerate(TE_list.keys()):
        dens_1 = [i - vmin / 2 for i in TE_list[key].values()]
        dens = [i / vmax for i in dens_1]
        colors = []
        for den in dens:
            colors.append((den, den, den, den))
        print(colors)
        te_axes = TE_map(key, TE_list[key], colors, 1, axes=spaxs[q % 5][j], fig=fig, title =f'From {key} to ...' )
        j += 1
        if j > 3:
            j = 0

    plt.show()
    # colors = [mcolors.to_rgba(c)
    #       for c in plt.rcParams['axes.prop_cycle'].by_key()['color']]
    # print(colors[0])


