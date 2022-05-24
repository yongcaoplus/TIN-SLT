#!/usr/bin/env bash
src=gloss
tgt=de
ARCH=transformers2
DATAPATH=/haotianshuv/caoyong/temp/be-slt/dataset/processed/ph14_add_text_to_gloss_0.9/
SAVEDIR=../checkpoints/tmp_${src}_${tgt}_tmp
mkdir -p $SAVEDIR

python train.py $DATAPATH \
-a $ARCH --optimizer adam --lr 0.0003 -s $src -t $tgt --label-smoothing 0.3 \
--dropout 0.45 --max-tokens 4000 --min-lr '1e-09' --lr-scheduler inverse_sqrt --weight-decay 0.0001 --bert-ratio 0.65 \
--alpha_mode "learn" --alpha_bert_strategy "cosine" --alpha_bert_max 1.0 --alpha_bert 1.0 --max-epoch 100 \
--encoder-layers 4 --decoder-layers 4 --bert-model-name /haotianshuv/caoyong/pretrained_model/bert-base-german-dbmdz-uncased/ \
--criterion label_smoothed_cross_entropy --max-update 150000 --warmup-updates 4000 --warmup-init-lr '1e-07' \
--adam-betas '(0.9,0.98)' --save-dir $SAVEDIR --share-all-embeddings $warmup