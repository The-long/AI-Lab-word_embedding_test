# AI-Lab词库测试
全量数据下载地址（16G）：https://ai.tencent.com/ailab/nlp/en/embedding.html 
部分数据（4万5，10万，100万，200万）下载地址：:https://pan.baidu.com/s/1meeKUBKbGMyTGrx664F4Ng
密码:xfh1

## 1.业务词理解对比
针对商店业务，分别使用4万5，50万，200万版本词库

### （1）200万

测试结果：

![image](https://user-images.githubusercontent.com/63181009/117914318-ac387b80-b315-11eb-8281-9cd61125351a.png)

后羿和鲁班相似度较高

![image](https://user-images.githubusercontent.com/63181009/117914365-cbcfa400-b315-11eb-94df-70c69a8f6256.png)

国王+女人-男人能得到王后。

![image](https://user-images.githubusercontent.com/63181009/117914436-eefa5380-b315-11eb-94cf-2cdc8431e256.png)

后羿的召回结果中，中国文化传说人物排在前列，同样是射手英雄的鲁班七号和虞姬紧随其后。


![image](https://user-images.githubusercontent.com/63181009/117914502-12250300-b316-11eb-9ae3-a9a1d59cc76d.png)
          
狄仁杰的召回结果不理想，同时代的武则天相似度较高，但在游戏中这两个英雄是有差距的。

![image](https://user-images.githubusercontent.com/63181009/117914588-3c76c080-b316-11eb-8feb-b0bc0ade3f2a.png)

猴子到是能找到孙悟空。

![image](https://user-images.githubusercontent.com/63181009/117914596-40a2de00-b316-11eb-95ad-b8f61fdc03d7.png)

搜索单机游戏名称效果很好

![image](https://user-images.githubusercontent.com/63181009/117914613-47315580-b316-11eb-9b71-5643c9159997.png)

搜索英雄联盟英雄的效果较好，搜索热门、中路、物理、刺客英雄亚索，召回的也都是热门、中路、物理、刺客类的英雄名字和外号。

![image](https://user-images.githubusercontent.com/63181009/117914628-4e586380-b316-11eb-9dac-7e88c047bc2e.png)

搜索亚索的官方名称疾风剑豪召回的也是官方名称

问题：
集中在近义词和反义词
召回反义词
近义词也没什么用，没有英雄
适合用实体去找实体，而不能用来用实体找标签、用标签找实体

### （2）50万

后羿

![image](https://user-images.githubusercontent.com/63181009/117914700-6def8c00-b316-11eb-836c-b418bc7ea7dd.png)

鲁班

![image](https://user-images.githubusercontent.com/63181009/117914720-76e05d80-b316-11eb-8145-abb0cad6682b.png)

ak-47

![image](https://user-images.githubusercontent.com/63181009/117914734-7ea00200-b316-11eb-9ac1-de811b373233.png)

国王+女人-男人

![image](https://user-images.githubusercontent.com/63181009/117914801-9d05fd80-b316-11eb-8045-3911ba2bb929.png)



### （3）45000
鲁班等词没有在词库中出现。


## 2.长语义理解等对比

以下测试由于内存问题使用50万词库，与45000词库对照

### （1）测试短句子：

![image](https://user-images.githubusercontent.com/63181009/117914903-c45cca80-b316-11eb-8cd9-c7c4c5f759aa.png)

相似度均较高。50万词库更准确


### （2）剔除异类词

![image](https://user-images.githubusercontent.com/63181009/117914930-cfaff600-b316-11eb-8eb8-8fb92d5560fe.png)

英雄联盟英雄被成功剔除。

### （3）计算内容相似度

读取有关后羿的两篇文章，计算相似度：

![image](https://user-images.githubusercontent.com/63181009/117914972-e3f3f300-b316-11eb-8c09-2bfc5a4cec65.png)

![image](https://user-images.githubusercontent.com/63181009/117914983-e8b8a700-b316-11eb-9925-2bbcc8124d17.png)

![image](https://user-images.githubusercontent.com/63181009/117915301-95932400-b317-11eb-982b-3c165f36eafa.png)

词库表现不错，相似度非常高。45000词库更准确。


#测试后羿内容与典韦内容的相似度
典韦内容：

![image](https://user-images.githubusercontent.com/63181009/117915314-9c219b80-b317-11eb-996c-743f72fe6f5c.png)

![image](https://user-images.githubusercontent.com/63181009/117915326-a2177c80-b317-11eb-83e6-150d474efae9.png)

50万词库判定后羿内容与典韦内容比45000词库判定的相似度更高。


测试王者荣耀攻略内容与凤凰新闻内容相似度：
凤凰新闻内容：

![image](https://user-images.githubusercontent.com/63181009/117915341-a8a5f400-b317-11eb-981e-75ddcc6615d5.png)

![image](https://user-images.githubusercontent.com/63181009/117915350-aba0e480-b317-11eb-952b-2b078c12b841.png)

50万词库更能判别出王者荣耀与新闻内容的区别。可以用于文章分类。


测试王者荣耀攻略内容与DNF内容相似度

![image](https://user-images.githubusercontent.com/63181009/117915361-b22f5c00-b317-11eb-9a71-f637bdd181b5.png)

50万词库更能判别出王者荣耀与新闻内容的区别。




