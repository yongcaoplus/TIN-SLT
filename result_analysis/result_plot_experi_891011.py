# -*- coding: utf-8 -*-
# @Time    : 2021/8/21 16:20 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, interp1d

result = []
with open('./db/result_experi891011', 'r') as f:
    for data in f.readlines():
        data = data.split()
        result.append([float(item) for item in data])


order = {1: "learn", 5: "constant", 16:"cosine", 3: "decrease", 4: "increase"}
color = {1: "#ff585d", 3: "#41b6e6", 4: "#001871", 5: "#ffb549", 16:"#9fb083"}
linesty = {1: "-", 3: "-.", 4: ":", 5: "--", 16:"-."}
markersty = {1: "", 3: "", 4: "", 5: "", 16:"."}


index = 1
with plt.style.context(['science', 'ieee']):
    fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    xnew = result[9]
    ynew = result[10]
    ynew_2 = result[11]
    ax.plot(xnew, ynew, label=order[index], markersize=5, linewidth=1, linestyle=linesty[index],
            marker=markersty[index], color=color[index])
    ax.plot(xnew, ynew_2, label=order[index], markersize=5, linewidth=1, linestyle=linesty[index],
            marker=markersty[index], color=color[index])
    ax.set(xlabel='Epoch')
    ax.set(ylabel='BLEU4 Value')
    plt.legend(loc='lower right', fontsize=12, frameon=True, fancybox=True, framealpha=1, borderpad=0.3, ncol=1,
               markerfirst=True, markerscale=1, numpoints=1, handlelength=3.5)
    plt.title("ASLG - Alpha Strategy Analysis")
    # plt.savefig("aslg_alpha_strategy.jpg")
    plt.show()