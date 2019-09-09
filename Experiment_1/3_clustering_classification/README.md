### Task-3

This Experiment is for social network and opinion analysis course.

The Task is Clustering using **K-means**.

Hope you will enjoy it.

### Data Format

​	First, you need to download the dataset(Twitter_data) in [link](https://www.weiyun.com/disk/sharedir/ea51ad8c0a0c0133a882654baf779852).

​	And you can open the file with note book.

​	This file contains 29846 data,and each of them has 8 items("userName":用户名;"clusterNo":类别；"text":Twitter内容；"timeStr":时间戳；"tweeId":用户Id；"errorCode":状态码；"textCleaned":去除链接等特殊符号只保留文本的处理；"relevance":)

### Preprocessing

#### File Read

```python
import json
# 将数据读取成dict格式便于后续的操作
Twitter_data=[]
with open("Twitter_data")as f:
    for line in f:
        # print(line)
        Twitter_data.append(json.loads(line))

```

#### Tokenize

```python
#可以直接按空格进行分词
#implement by yourself
```

#### Vectoring

```python
#建议使用词袋模型
#implement by yourself
```

### k-Means

```python
#不允许调库，数据集中有200左右个类别
#implement by yourself
```