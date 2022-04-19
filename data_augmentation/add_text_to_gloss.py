# -*- coding: utf-8 -*-
# @Time    : 2021/8/13 15:13 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
import os
import numpy as np
from utils.tools import file_to_lower
from shutil import copyfile

# gloss_file = 'ph14/train.gloss'
# text_file = 'ph14/train.de'

gloss_file = 'ph14_stmc/train.gloss'
text_file = 'ph14/train.de'

gloss_data = []
# 读数据
with open(gloss_file, 'r') as f:
    gloss_sentence = [item.strip().lower() for item in f.read().split('\n')]
    for item in gloss_sentence:
        words = item.split()
        gloss_eff = []
        for word in words:
            if "__" not in word:
                gloss_eff.append(word)
        gloss_data.append(" ".join(gloss_eff))

with open(text_file, 'r', encoding='utf-8') as f:
    text_data = [item.strip() for item in f.read().split('\n')]

print(gloss_data[-1])
gloss_data.pop(-1)
print(len(gloss_data), len(text_data))
print(gloss_data[-1])

ratio = int(0.9 * len(gloss_data))
index = np.random.randint(low=0, high=len(gloss_data)-1, size=ratio)

for item in index:
    gloss_data.append(text_data[item][0:-2])
    text_data.append(text_data[item])


file_to_lower("ph14_stmc/valid.gloss", "stmc_add_text_to_gloss_0.9/valid.gloss")
file_to_lower("ph14_stmc/test.gloss", "stmc_add_text_to_gloss_0.9/test.gloss")
copyfile("ph14_stmc/valid.de", "stmc_add_text_to_gloss_0.9/valid.de")
copyfile("ph14_stmc/test.de", "stmc_add_text_to_gloss_0.9/test.de")


with open("stmc_add_text_to_gloss_0.9/train.gloss", 'w', encoding="utf-8") as f:
    for i in range(len(gloss_data)):
        f.write(gloss_data[i] + '\n')

with open("stmc_add_text_to_gloss_0.9/train.de", 'w', encoding='utf-8') as f:
    for i in range(len(text_data)):
        f.write(text_data[i] + '\n')