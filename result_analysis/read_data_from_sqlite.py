# -*- coding: utf-8 -*-
# @Time    : 2021/8/19 19:56 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
import sqlite3 as db


# 从SQLite文件中读取数据
def readFronSqllite(db_path, exectCmd):
    conn = db.connect(db_path)  # 该 API 打开一个到 SQLite 数据库文件 database 的链接，如果数据库成功打开，则返回一个连接对象
    cursor=conn.cursor()        # 该例程创建一个 cursor，将在 Python 数据库编程中用到。
    conn.row_factory=db.Row     # 可访问列信息
    cursor.execute(exectCmd)    #该例程执行一个 SQL 语句
    rows=cursor.fetchall()      #该例程获取查询结果集中所有（剩余）的行，返回一个列表。当没有可用的行时，则返回一个空的列表。
    return rows


# 解析ARPA 单帧信息
def readfromAppaFrame(ARPAFrame):
    subARPA=ARPAFrame.split(',')
    print(subARPA)

'''
PH14:
'/root/nni-experiments/OVapkj3T/db/nni.sqlite'
order = {8:"learn", 7:"constant", 6:"cosine",  25:"decrease", 41:"increase"}
color = {6:"#9fb083", 7:"#ffb549", 8:"#ff585d", 25:"#41b6e6", 41:"#001871"}
linesty = {6:"-.", 7:"--", 8:"-", 25:"-.", 41:":"}
markersty = {6:".", 7:"", 8:"", 25:"", 41:""}


ASLG: 
'/root/nni-experiments/xj80LMmX/db/nni.sqlite'
order = {1:"learn", 3:"decrease", 4:"increase",  5:"constant"}
color = {1:"#ff585d", 3:"#ffb549", 4:"#9fb083", 5:"#41b6e6"}
linesty = {1:"-", 3:"--", 4:"-.", 5:"-."}
markersty = {1:"", 3:"", 4:".", 5:""}
'''

if __name__=="__main__":

    order = {8: "learn", 7: "constant", 6: "cosine", 25: "decrease", 41: "increase"}
    color = {6: "#9fb083", 7: "#ffb549", 8: "#ff585d", 25: "#41b6e6", 41: "#001871"}
    linesty = {6: "-.", 7: "--", 8: "-", 25: "-.", 41: ":"}
    markersty = {6: ".", 7: "", 8: "", 25: "", 41: ""}
    data = {}
    order = {0: "learn", 3: "constant", 4: "cosine", 10: "decrease", 13: "increase"}
    for item in order.keys():
        data[item] = []
        rows=readFronSqllite('/root/nni-experiments/nHBp3OP5/db/nni.sqlite', "select * from MetricData where parameterId=="+str(item))
        for i in range(len(rows)):
            data[item].append(float(rows[i][5].replace("\"", "")))
    import matplotlib.pyplot as plt
    import numpy as np
    from scipy.interpolate import make_interp_spline, interp1d

    np.save("ph14_data_5lines", data)

    # with plt.style.context(['science',  'no-latex']):
    #     fig, ax = plt.subplots(figsize=(8, 6), dpi=300)
    #     x = [item for item in range(int(len(data[3])/3))]
    #     for index in order.keys():
    #         if index == 16:
    #             x_plot = np.array(x)
    #             y_plot = np.array(data[index][::3])[0:len(x_plot)]
    #             xnew = np.linspace(x_plot.min(), x_plot.max(), 100)
    #             f1 = interp1d(x_plot, y_plot, kind='linear')
    #             print("dd")
    #             ynew = f1(xnew)
    #         else:
    #             x_plot = np.array(x)
    #             y_plot = np.array(data[index][::3])[0:len(x_plot)]
    #             xnew = np.linspace(x_plot.min(), x_plot.max(), 100)
    #             ynew = make_interp_spline(x_plot, y_plot)(xnew)
    #         print(len(xnew), len(ynew))
    #         ax.plot(xnew, ynew, label=order[index], markersize=5, linewidth=1, linestyle=linesty[index], marker=markersty[index], color=color[index])
    #     ax.set(xlabel='Epoch')
    #     ax.set(ylabel='BLEU4 Value')
    #     plt.legend(loc='lower right', fontsize=12, frameon=True, fancybox=True, framealpha=1, borderpad=0.3,ncol=1, markerfirst=True, markerscale=1, numpoints=1, handlelength=3.5)
    #     plt.title("ASLG - Alpha Strategy Analysis")
    #     plt.savefig("aslg_alpha_strategy.jpg")
    #     plt.show()