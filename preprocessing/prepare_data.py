# -*- coding: utf-8 -*-
# @Time    : 2021/12/22 15:23 
# @Author  : Yong Cao
# @Email   : yongcao_epic@hust.edu.cn
import os
import shutil
################# Configuration  ####################
source_language = "gloss"
target_language = "de"
source_path = "./../dataset/raw/ph14_stmc"
destdir = "./../dataset/processed/ph14_stmc"
bert_model_path = "/haotianshuv/caoyong/pretrained_model/bert-base-german-dbmdz-uncased/"
################# End Configuration  ################

index = ["python preprocess.py", "--source-lang", source_language, "--target-lang", target_language, "--trainpref",
         os.path.join(source_path, "train"), "--validpref", os.path.join(source_path, "valid"), "--testpref",
         os.path.join(source_path, "test"), "--destdir", destdir, "--joined-dictionary", "--bert-model-name",
         bert_model_path]

if os.path.exists(destdir):
    shutil.rmtree(destdir)
if not os.path.exists(destdir):
    os.mkdir(destdir)

cmd = " ".join(index)
os.system(cmd)
print("Finished Precessing, data stored in {}".format(destdir))
