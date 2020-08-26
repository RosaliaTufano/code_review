# code_review

`code_review` is the replication package of the work *"Towards Automating Code Review Activities"*.

The purpose of this repository is to provide everythig necessary to replicate our results.

### TODO: add an introduction.

### TODO: Dependencies -> OpenNMT-tf

## Contents

In `datasets` folder both datasets for the two Transformer models are provided. The data are splitted in `training set`, `validation set` and `test set`; each of them can be found in the relative folder.

The dataset for the `1-encoder` model is composed by *Reviewed Code Pairs* (RCPs). A RCP is a <m_s, m_r> pair composed by the abstracted code of the method extracted from the Java file submitted by a contributor for review (m_s) and by the abstracted code of its revised version (m_r). Therefore, for each set two files are provided: 
  - `src` file contains the m_s instances; 
  - `tgt` file contains the m_r instances.
  
The dataset for the `2-encoders` model is instead composed by *Reviewed Commented Code Triplets* (RCCTs), each having the form  <m_s, m_r, r_nl> where m_r is the abstracted code of the method implementing the natural language recommendation (r_nl) provided by a reviewer for the method in the code submitted (m_s). Therefore, for each set three files are provided:
  - 'src1' file contains the r_nl instances;
  - 'src2' file contains the m_s instances;
  - 'tgt' file contains the m_r instances.
  


