# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 23:18 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
import re
import os
import numpy as np


'''
ASLG: "/root/nni-experiments/nHBp3OP5/trials/" "AQaEP"
PH14："/root/nni-experiments/xj80LMmX/trials/" "MeZoj"
'''

font_size = 18
# trial_path = "/haotianshuv/caoyong/temp/aslg_bert_compare_trials/trials/"
trial_path = "/haotianshuv/caoyong/temp/ph14_bert_compare_trials"
final_result = {}
for trial in os.listdir(trial_path):
    log_path = os.path.join(trial_path, trial, "trial.log")
    # if "MeZoj" in log_path:
    if os.path.exists(log_path):
        with open(log_path, 'r', encoding="utf-8") as f:
            content = f.read().split("loading model(s) from ")
        alpha_min = []
        alpha_avg = []
        alpha_mean = []
        bleu4 = []
        for item in content:
            pattern = re.compile(r'PRINT Encoder bert weight .  tensor([([\d+(\.\d+)?]+)')
            res = pattern.findall(item)
            data_valid = [float(item.split("[")[1]) if len(item) > 2 else 0.0 for item in res]
            alpha_mean.append(np.mean(data_valid))
            alpha_avg.append(np.var(data_valid))

            pattern = re.compile(r'Generate test with beam=5: BLEU4 = ([\d+(\.\d+)?]+)')
            res_bleu = pattern.findall(item)
            if len(res_bleu) > 0:
                bleu4.append(float(res_bleu[0]))
            else:
                bleu4.append(0)

        r1 = list(map(lambda x: x[0] - x[1], zip(alpha_mean, alpha_avg)))
        r2 = list(map(lambda x: x[0] + x[1], zip(alpha_mean, alpha_avg)))
        import matplotlib.pyplot as plt
        # with plt.style.context(['science', 'no-latex']):

        fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
        plt.rc('font', family='Times New Roman')
        x = [item for item in range(len(alpha_mean))]
        ax.plot(x, alpha_mean, color="#F0B775", label="alpha weight", markersize=8, linewidth=3)
        ax.fill_between(x, r1, r2, color="#F0B775", alpha=0.3)
        # 设置刻度字体大小
        import matplotlib.ticker as mtick
        ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%.2f'))
        plt.xticks(fontsize=font_size)
        plt.yticks(fontsize=font_size)
        # 设置坐标标签字体大小
        ax.set_xlabel(xlabel='Epoch', fontsize=font_size)
        ax.set_ylabel(ylabel='Alpha Value', fontsize=font_size)
        plt.legend(loc='upper right', fontsize=font_size, frameon=True, fancybox=True, framealpha=1,
                   borderpad=0.3, ncol=1,
                   markerfirst=True, markerscale=1, numpoints=1, handlelength=3.5)
        plt.grid()
        # plt.title(trial + "  :  " +  str(np.mean(bleu4[-20:]))[0:5])
        plt.savefig("./db/" +  str(np.mean(bleu4[70:100]))[0:5]+ "_" + trial + "_ph14.png")
        plt.show()
        print("----- : 123", trial)
        print(alpha_mean)
