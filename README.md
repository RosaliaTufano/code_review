# code_review

`code_review` is the replication package of the work *"Towards Automating Code Review Activities"*.

The purpose of this repository is to provide everythig necessary to replicate our results.

### TODO: add an introduction.

### TODO: Dependencies -> Python, OpenNMT-tf

## Contents

### Datasets

In `datasets` folder both datasets for the two Transformer models are provided. The data are splitted in `training set`, `validation set` and `test set`; each of them can be found in the relative folder.

The dataset for the `1-encoder` model is composed by *Reviewed Code Pairs* (RCPs). A RCP is a <m_s, m_r> pair composed by the abstracted code of the method extracted from the Java file submitted by a contributor for review (m_s) and by the abstracted code of its revised version (m_r). Therefore, for each set two files are provided: 
  - `src` file contains the m_s instances; 
  - `tgt` file contains the m_r instances.
  
The dataset for the `2-encoders` model is instead composed by *Reviewed Commented Code Triplets* (RCCTs), each having the form  <m_s, m_r, r_nl> where m_r is the abstracted code of the method implementing the natural language recommendation (r_nl) provided by a reviewer for the method in the code submitted (m_s). Therefore, for each set three files are provided:
  - `src1` file contains the r_nl instances;
  - `src2` file contains the m_s instances;
  - `tgt` file contains the m_r instances.
  
The natural language recommendations are cleaned and abstracted as described in our work.
  
### Code

The `code` folder contains all the necessary to *train* the models and to *test* them.

For both models, the best configuration we found through the tuning of the hyperparameters is provided in the respective folders. To start the training of a model it is sufficient to run the `training/trainin.py` file. It first will create the vocabularies needed and then it will start the training. The model trained will be saved in the `run` folder.

Once the model is trained, it is possible to test it on the test set by running the `run-on-test/infer.py` file. It will create the `predictions.txt` file containing all the model predictions.

It is possible to change the *beam search size* modifying the `beam_width` and `num_hypotheses` parameters in the `training/data.yml` file.

