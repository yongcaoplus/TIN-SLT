data_dir=./../dataset/processed/stmc_add_text_to_gloss_0.9/
ckpt_path=./../checkpoint_save/stmc_0.9_spslV_0.2/checkpoint_2613.pt
store_file=./../log/tian_stmc/result_test.out
clean_text_file=./../log/tian_stmc/result_test.txt
python generate.py $data_dir --gen-subset 'test' --alpha_mode 'constant' --remove-bpe '@@ ' --criterion 'cross_entropy' --path $ckpt_path --beam 9 | tee $store_file
grep ^H $store_file | sort -n -k 2 -t '-' | cut -f 3 > $clean_text_file

score_text=./../log/tian_stmc/score_test.txt
goal_test_file=./../dataset/raw/ph14_clean/test.de
python3 ./../utils/bleu.py 1 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/bleu.py 2 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/bleu.py 3 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/bleu.py 4 $clean_text_file $goal_test_file >> $score_text
python3 ./../utils/rouge.py $clean_text_file $goal_test_file | grep 'rouge-l' | grep -Po '\d+\.\d+$' >> $score_text
python3 ./../utils/meteor.py $clean_text_file $goal_test_file >> $score_text
