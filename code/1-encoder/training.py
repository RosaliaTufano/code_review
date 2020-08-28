import subprocess

# DATA

path_src_train = '../../../datasets/1-encoder/train/src-train.txt'
path_tgt_train = '../../../datasets/1-encoder/train/tgt-train.txt'

path_src_val = '../../../datasets/1-encoder/eval/src-val.txt'
path_tgt_val = '../../../datasets/1-encoder/eval/tgt-val.txt'

# BUILD VOCAB

f = open('./build_vocab.sh', 'w')
f.close()
subprocess.run('chmod a+x build_vocab.sh', shell=True)

f = open('build_vocab.sh', 'w')
f.write('#!/usr/bin/env bash\n')
f.write('onmt-build-vocab --size 50000 --save_vocab src-vocab.txt ' + path_src_train + '\n')
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
f_sh.write('onmt-main --model custom_1encoder_transformer.py --gpu_allow_growth --config data.yml --auto_config train --with_eval')
f_sh.close()

subprocess.run('./train_model.sh')
