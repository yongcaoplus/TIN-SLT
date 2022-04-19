# Explore More Guidance: A Task-aware Instruction Network for Sign Language Translation Enhanced with Data Augmentation

by [Yong Cao](https://yongcaoplus.github.io/), Wei Li, [Xianzhi Li](https://nini-lxz.github.io/), [Min Chen](https://people.ece.ubc.ca/~minchen/), [Guangyong Chen](https://guangyongchen.github.io/), Zhengdao Li, [Long Hu](https://people.ece.ubc.ca/~minchen/longhu/), [Kai Hwang](https://myweb.cuhk.edu.cn/hwangkai).

## 1. Introduction

 This repository is for our Findings of NAACL 2022 paper '[Explore More Guidance: A Task-aware Instruction Network for Sign Language Translation Enhanced with Data Augmentation
](https://arxiv.org/abs/2204.05953)'. In this paper, we propose a task-aware instruction network, namely TIN-SLT, for sign language translation, by introducing the instruction module and the learning-based feature fuse strategy into a Transformer network. 
 In this way, the pre-trained model's language ability can be well explored and utilized to further boost the translation performance. 
 Moreover, by exploring the representation space of sign language glosses and target spoken language, we propose a multi-level data augmentation scheme to adjust the data distribution of the training set. 
 We conduct extensive experiments on two challenging benchmark datasets, PHOENIX-2014-T and ASLG-PC12, on which our method outperforms former best solutions by 1.65 and 1.42 in terms of BLEU-4.


## 2. Dataset and Trained models
* Dataset can be downloaded in [Google Drive](https://drive.google.com/file/d/1wghNY3Z5XOQmkyVHh8o8zGAuGvaDRIYJ/view?usp=sharing) and processed version is here：[Google Drive](https://drive.google.com/file/d/1lwtO8qnEuGaUaiBw6d0d3ZLufXDacxYC/view?usp=sharing).       
* Our trained model can be downloaded in [Google Drive](https://drive.google.com/drive/folders/1s26goE0Rh4T9L_d-6XDfHKYP_FPGPveR?usp=sharing). 
If the trained model doesn't work or if there are any issues, please feel free to contact us.

## 3. Execute Steps

#### Step 1 install dependencies

```shell
pip install --editable .      
python prepare_data.py
```

#### Step 2 Train by AutoML

```shell
nnictl create --config automl/config.yml -p 11111
```

#### Step 3 Obtain Mertrix

```shell
cd postprocessing       
sh get_bleu4.sh
```

## 4. Questions
Please contact [yongcao_epic@hust.edu.cn]().