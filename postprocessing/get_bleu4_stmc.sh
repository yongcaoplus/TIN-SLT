# please config data and model path
data_dir=/haotianshuv/caoyong/temp/be-slt/dataset/processed/stmc_add_text_to_gloss_0.9/
ckpt_path=/haotianshuv/caoyong/temp/be-slt/checkpoint_save/stmc_0.9_spslV_0.2/checkpoint_2613.pt
goal_test_file=/haotianshuv/caoyong/temp/be-slt/dataset/raw/ph14_clean/test.de

# please config log save dir
if [ ! -d "/haotianshuv/caoyong/tin_rebuild/log" ]; then
  mkdir /haotianshuv/caoyong/tin_rebuild/log
fi
if [ ! -d "/haotianshuv/caoyong/tin_rebuild/tin_stmc" ]; then
  mkdir /haotianshuv/caoyong/tin_rebuild/log/tin_stmc
fi
store_file=/haotianshuv/caoyong/tin_rebuild/log/tin_stmc/result_test.out
clean_text_file=/haotianshuv/caoyong/tin_rebuild/log/tin_stmc/result_test.txt
score_text=/haotianshuv/caoyong/tin_rebuild/log/tin_stmc/score_test.txt
# end condig


python generate.py $data_dir --gen-subset 'test' --alpha_mode 'constant' --remove-bpe '@@ ' --criterion 'cross_entropy' --path $ckpt_path --beam 9 | tee $store_file
grep ^H $store_file | sort -n -k 2 -t '-' | cut -f 3 > $clean_text_file

python3 ./../utils/bleu.py 1 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/bleu.py 2 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/bleu.py 3 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/bleu.py 4 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/rouge.py $clean_text_file $goal_test_file | grep 'rouge-l' | grep -Po '\d+\.\d+$' >> $score_text
python3 ./../utils/meteor.py $clean_text_file $goal_test_file >> $score_text
