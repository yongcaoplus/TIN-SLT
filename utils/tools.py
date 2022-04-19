# -*- coding: utf-8 -*-
# @Time    : 2021/8/5 9:28 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
def file_to_lower(file_path, dst_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = [item.strip().lower() for item in f.read().split('\n')]
    with open(dst_path, 'w', encoding='utf-8') as f:
        for i, item in enumerate(data):
            if i == len(data) - 1:
                f.write(item)
            else:
                f.write(item + "\n")


# def plot_cysytle(y, fontsize,x=[], x_label="", y_label=""):

