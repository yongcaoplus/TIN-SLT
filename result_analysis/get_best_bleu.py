# -*- coding: utf-8 -*-
# @Time    : 2021/7/23 10:07 上午 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
"""
批量遍历一次实验的epoch，输出bleu4指标
"""
import os
import re

############# 配置路径和epoch范围 #################
trial_path = "/li_wei/bert-nmt/checkpoints/ph14_XF0eh_e2_d2_0.5"
dataset_path = "ph14_gloss_de"
epoch_range = [20,50]
beam = 5
save_path = "result-81.out"
################################################


if os.path.exists(save_path):
    os.remove(save_path)

cmd = "python generate.py " + dataset_path + " --beam " + str(beam) + " --path " + trial_path + "/checkpoint"
cmd_extend = ".pt --batch-size 128 -s gloss -t de --remove-bpe --bert-model-name bert-base-german-dbmdz-uncased | tee -a " + save_path
for i in range(epoch_range[0], epoch_range[1] + 1):
    os.system(cmd + str(i) + cmd_extend)
with open(save_path, 'r') as f:
    text = f.read()
    bleu_list = re.findall(r" BLEU4 = ([\d.]+)", text)

# assert len(bleu_list) == epoch_range[1] - epoch_range[0] + 1
# 打印结果
print("The result(bleu4) of trial {} is : ".format(trial_path.split("/")[1]))
print(bleu_list)
result = {}
for i in range(epoch_range[1] - epoch_range[0] + 1):
    result["epoch " + str(epoch_range[0] + i)] = bleu_list[i]
print(sorted(result.items(), key=lambda kv: (kv[1], kv[0]), reverse=True))
