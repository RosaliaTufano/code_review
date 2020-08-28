import subprocess

# DATA

path_src1_train = '../../datasets/2-encoders/train/src1-train.txt'
path_src2_train = '../../datasets/2-encoders/train/src2-train.txt'
path_tgt_train = '../../datasets/2-encoders/train/tgt-train.txt'

path_src1_val = '../../datasets/2-encoders/eval/src1-val.txt'
path_src2_val = '../../datasets/2-encoders/eval/src2-val.txt'
path_tgt_val = '../../datasets/2-encoders/eval/tgt-val.txt'

# BUILD VOCAB

f = open('./build_vocab.sh', 'w')
f.close()
subprocess.run('chmod a+x build_vocab.sh', shell=True)

f = open('./build_vocab.sh', 'w')
f.write('#!/usr/bin/env bash\n')
f.write('onmt-build-vocab --size 50000 --save_vocab src1-vocab.txt ' + path_src1_train + '\n')
f.write('onmt-build-vocab --size 50000 --save_vocab src2-vocab.txt ' + path_src2_train + '\n')
f.write('onmt-build-vocab --size 50000 --save_vocab tgt-vocab.txt ' + path_tgt_train)
f.close()

print('Building vocabularies...')
subprocess.run('./build_vocab.sh')

# TRAINING

print('Starting Training...')
f_sh = open('./train_model.sh', 'w')
f_sh.close()

subprocess.run('chmod a+x train_model.sh', shell=True)

f_sh = open('./train_model.sh', 'w')
f_sh.write('#!/usr/bin/env bash\n')
f_sh.write('onmt-main --model custom_2encoders_transformer.py --gpu_allow_growth --config data.yml --auto_config train --with_eval')
f_sh.close()

subprocess.run('./train_model.sh')
