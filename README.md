# code_review

`code_review` is the replication package of the work *"Towards Automating Code Review Activities"*.

The purpose of this repository is to provide everythig necessary to replicate our results.

### TODO: add an introduction.

### TODO: Dependencies -> OpenNMT-tf

## Contents

In `datasets` folder both datasets for the two Transformer models are provided. The data are splitted in `training set`, `validation set` and `test set`; each of them can be found in the relative folder.

The dataset of the `1-encoder` model is composed by *Reviewed Code Pairs* (RCPs). A RCP is a <m_s, m_r> pair composed by the abstracted code of the method extracted from the Java file submitted by a contributor for review (m_s) and by the abstracted code of its revised version (m_r). Therefore, for each set two files are provided: 
  - the `src` file contains the m_s instances; 
  - the `tgt` file cntains the m_r instances.
  


