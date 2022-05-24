# please config data and model path
data_dir=/haotianshuv/caoyong/temp/be-slt/dataset/processed/aslg_add_text_to_gloss_0.38/
ckpt_path=/haotianshuv/caoyong/temp/be-slt/checkpoint_save/aslg_84.29/checkpoint74.pt
goal_test_file=/haotianshuv/caoyong/temp/be-slt/dataset/raw/aslg_clean/test.en

# please config log save dir
if [ ! -d "/haotianshuv/caoyong/tin_rebuild/log" ]; then
  mkdir /haotianshuv/caoyong/tin_rebuild/log
fi
if [ ! -d "/haotianshuv/caoyong/tin_rebuild/tin_aslg" ]; then
  mkdir /haotianshuv/caoyong/tin_rebuild/log/tin_aslg
fi
store_file=/haotianshuv/caoyong/tin_rebuild/log/tin_aslg/result_test.out
clean_text_file=/haotianshuv/caoyong/tin_rebuild/log/tin_aslg/result_test.txt
score_text=/haotianshuv/caoyong/tin_rebuild/log/tin_aslg/score_test.txt
# end condig

BEAM_SIZE=5
BATCH_SIZE=128
python generate.py $data_dir  --instruction_layer_num 1  --batch-size 128 --remove-bpe '' --criterion 'label_smoothed_cross_entropy'  --path $ckpt_path --beam 5 | tee $store_file
grep ^H $store_file | sort -n -k 2 -t '-' | cut -f 3 > $clean_text_file

python3 ./../utils/bleu.py 1 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/bleu.py 2 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/bleu.py 3 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/bleu.py 4 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/rouge.py $clean_text_file $goal_test_file | grep 'rouge-l' | grep -Po '\d+\.\d+$' >> $score_text
python3 ./../utils/meteor.py $clean_text_file $goal_test_file >> $score_text
