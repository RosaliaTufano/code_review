import subprocess


# DATA

path_datayml = 'data.yml'
src_file = '../../datasets/2-encoders/test/src1-test.txt ../../datasets/2-encoders/test/src2-test.txt'
path_pred = 'predictions.txt'

# INFER

infer_command = 'onmt-main --config ' + path_datayml + ' --auto_config infer --features_file ' + src_file + ' --predictions_file ' + path_pred

f = open('./infer.sh', 'w')
f.close()

subprocess.run('chmod a+x infer.sh', shell=True)

f = open('./infer.sh', 'w')
f.write('#!/usr/bin/env bash\n')
f.write(infer_command)
f.close()

subprocess.run('./infer.sh')
