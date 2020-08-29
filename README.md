# code_review

`code_review` is the replication package of the work *"Towards Automating Code Review Activities"*.

The purpose of this repository is to provide everything necessary to replicate our results.

## Requirements

- Python >= 3.5
- OpenNMT-tf

Use the following commands to install the dependencies. 

```
pip install --upgrade pip
pip install OpenNMT-tf
```

## Content

### Datasets

The `datasets` folder contains two datasets used for experimenting with two Transformer models. Both datasets are split in three parts `training` (80%), `validation` (10%), and `test` (10%) sets;
Each Transformer model (I.e., `1-encoder` and `2-encoders` folders) has three sub-folders `train`, `eval`, and `test` with the actual data.  

 - The dataset for the `1-encoder` model is composed of *Reviewed Code Pairs* (RCPs). A RCP is a <m<sub>s</sub>, m<sub>r</sub>> pair composed by the abstracted code of the method extracted from the Java file submitted by a contributor for review (m<sub>s</sub>) and by the abstracted code of its revised version (m<sub>r</sub>).
 We provide data in the form of textual file organized per row, therefore, a pair <m<sub>s</sub>, m<sub>r</sub>> refers to the same line number of the following two files:   
    - `src` file contains the m<sub>s</sub> instances; 
    - `tgt` file contains the m<sub>r</sub> instances.
  
 - The dataset for the `2-encoders` model is, instead, composed of *Reviewed Commented Code Triplets* (RCCTs), each triple have the form <m<sub>s</sub>, m<sub>r</sub>, r<sub>nl</sub>>, where m<sub>r</sub> is the abstracted code of the method implementing the natural language recommendation (r<sub>nl</sub>) provided by a reviewer for the method in the code submitted (m<sub>s</sub>).
 Therefore, to build a triple <m<sub>s</sub>, m<sub>r</sub>, r<sub>nl</sub>> three files are provided:
    - `src1` file contains the r<sub>nl</sub> instances;
    - `src2` file contains the m<sub>s</sub> instances;
    - `tgt` file contains the m<sub>r</sub> instances.
  
NOTE. The natural language recommendations have been cleaned and abstracted as described in our manuscript.
  
### Code

The `code` folder contains all scripts used to *train* and *test* the models.

For both models, the best configuration we found through the tuning of the hyperparameters is provided in the respective folders. To start the training of a model it is sufficient to run the `trainin.py` file. It first will create the vocabularies needed and then it will start the training. The trained model will be saved in the `run` folder.

Once the model is trained, it is possible to test it on the test set by running the `infer.py` file. This script creates the `predictions.txt` file containing all the model's predictions.

It is, also, possible to change the *beam search size* modifying the `beam_width` and `num_hypotheses` parameters in the `training/data.yml` file.

### Other files

This repository also contains:

  - `idioms.csv` : the list of idioms we used during abstraction phase;
  - `is_relevant.ipynb` : a jupyter file showing the logic used to remove the not relevant comments;
  - `1_encoder_perfect_predictions.xlsx` and `2_encoders_perfect_predictions.xlsx` : the qualitative analysis of perfect predictions.