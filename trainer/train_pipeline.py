# -*- coding: utf-8 -*-
# @Time    : 2021/7/23 10:27 下午 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
import os
import nni
from trainer.train import cli_main


# 定义初始化参数
src = 'gloss'
tgt = 'de'
# DATAPATH = '/haotianshuv/caoyong/temp/be-slt/dataset/processed/aslg_add_text_to_gloss_0.38/'
# DATAPATH = '/haotianshuv/caoyong/temp/be-slt/dataset/processed/ph14_add_text_to_gloss_0.9/'

# 从搜索空间获得解
trial_no = nni.get_trial_id()
params = nni.get_next_parameter()

bedropout = params['encoder_bert_dropout_ratio']
en_layers = params['encoder_layers']
de_layers = params['decoder_layers']

layers = min(en_layers, de_layers)
params['encoder_layers'] = layers
params['decoder_layers'] = layers


if not os.path.exists('./../checkpoint/'):
    os.mkdir('./../checkpoint/')
# 将每次实验的模型保存到对应的文件夹
SAVEDIR = './../checkpoint/ph14_stmc_new_{}_e{}_{}'.format(str(trial_no), layers, bedropout)
store_model_path = SAVEDIR + "/checkpoint_best.pt"
if not os.path.exists(SAVEDIR):
    os.mkdir(SAVEDIR)

# 构造传参
args = {'save_dir': SAVEDIR, 'adam_betas': '(0.9,0.98)', 'source_lang': src, 'target_lang': tgt}

######################  需要配置  ########################
# 添加或者删除模型自定义的参数
if params['arch'] == "transformer_s2_iwslt_de_en":
    pass
#########################################################
params.update(args)

# 训练
cli_main(params)

# # 测试结果
# assert os.path.exists(store_model_path)
# args_test = {"data": DATAPATH, "path": store_model_path, "beam": "5", "batch_size": 128, "remove_bpe": "", "bert_model_name": "bert-base-german-dbmdz-uncased"}
# params.update(args_test)
# nni_test_main(params)
