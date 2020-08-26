import subprocess

path_datayml = '../trainin/data.yml'

# 1 encoder
features_file = 

path_tgt_test = 
path_pred = 'predictions.txt'

# INFER

infer_command = 'onmt-main --config ' + path_datayml + ' --auto_config infer --features_file ' \
       + features_file + ' --predictions_file ' + path_pred

f = open(path_folder + 'infer.sh', 'w')
f.close()

subprocess.run('chmod a+x infer.sh', shell=True)

f = open(path_folder + 'infer.sh', 'w')
f.write('#!/usr/bin/env bash\n')
f.write(infer_command)
f.close()

subprocess.run(path_folder + 'infer.sh')
