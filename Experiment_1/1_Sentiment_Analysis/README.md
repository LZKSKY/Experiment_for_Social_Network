### Task

​	This Experiment is for social network and opinion analysis course.

​	The Task is Sentiment Analysis using **Naive Bayes**.

​	**You Need To Write The NAIVE BAYES Code By Your Self, Do Not Use Written Library.**

​	Hope you will enjoy it.

### Data Format

​	First, you need to download the dataset in [link](https://share.weiyun.com/5yBGMQq-g). Dataset name: `aclImdb_v1.tar.gz`

​	Then,  unzip the file by `tar -xzvf aclImdb_v1.tar.gz` in linux or some software in Windows.

​	The directory contains five files or directories with a README file. You need to use data in `train/` to train and `test/` to evaluate your model.

​	In these two file, you can use two directories `neg/` and `pos/` which contains data with negative and positive label respectively. Each txt file contains raw text as one data.

### Preprocessing

#### File Read 

```python
import os
path = './aclImdb/'
pos_path = path + 'pos/'
neg_path = path + 'neg/'
pos_files = [pos_path + x for x in 
			 filter(lambda x: x.endswith('.txt'), os.listdir(pos_path))]
neg_files = [neg_path + x for x in 
			 filter(lambda x: x.endswith('.txt'), os.listdir(neg_path))]
pos_list = [open(x, 'r', encoding='utf-8').read().lower() for x in pos_files]
neg_list = [open(x, 'r', encoding='utf-8').read().lower() for x in neg_files]
data_list = pos_list + neg_list
labels_list = [1] * len(pos_list) + [0] * len(neg_list)
# shuffle if you'd like ===========================
from random import shuffle
merged_data = list(zip(data_list, label_list))
shuffle(merged_data)
data_list, label_list = list(zip(*merged_data))
# =================================================
# well you can also write as a function
# Write this by yourself if you find a better way
```

#### Tokenize

```python
from keras.preprocessing.text import Tokenizer
max_vocab_size = 50000
tokenizer = Tokenizer(num_words=max_vocab_size, oov_token='<UNK>')
tokenizer.fit_on_texts(data_list)
# tokenizer.texts_to_matrix() input a list of raw text, return a numpy matrix
# for one text to test
tf_idf_data_121 = tokenizer.texts_to_matrix([data_list[121]], mode='tfidf') 
# for total text
tf_idf_data = tokenizer.texts_to_matrix(data_list, mode='tfidf')
# ===================================================
# Implement this by yourself without this Tokenizer, it's also really easy. ^_^
# Well you can just use it, enjoy!
```

### Evaluation

We take accuracy as the only metric. 



### Additional Resource

1. word vocabulary with sentiment  `NRC-Emotion-Lexicon-Wordlevel-v0.92.txt` . 

   It's format is `word label Associated_label` . You can only extract `label` with positive and negative, and check its corresponding `Associated_label`,  1 meaning this word is belong to this label, 0 meaning not.





