import jieba


#赶工1.0版本

def load():
        all_score=0
        all_ne=0 
        all_po=0
        f=open('type.ini', encoding='gbk') #加载type字符库
        text=[]
        score=[]
        sort=[]        
        print("=========================================")
        for line in f:
                get_tx=line.split(",")
                for i in range(0, len(get_tx)):
                        if get_tx[i][0:5]=="text=":
                                text.append(get_tx[i][5:])                
                        if get_tx[i][0:6]=="score=":
                                score.append(eval(get_tx[i][6:]))
                                all_score=all_score+eval(get_tx[i][6:])
                        if get_tx[i][0:5]=="sort=":  #获取分类可以是很多类
                                sort.append(get_tx[i][5:])
                                if "negative" in get_tx[i][5:]:
                                        all_ne=all_ne+1
                                elif "positive" in get_tx[i][5:]:
                                        all_po=all_po+1
		
                '''
                if len(text) == len(score): //测试ini错误的代码
                        pass
                else:
                        print(len(text))
                '''
        print("正面情感词数:"+str(all_po))
        print("负面情感词数:"+str(all_ne))
        print("总分数:"+str(all_score))
        print("=========================================")
        return text,score


def seg_word(sentence): #jieba分词
	seg_list = jieba.cut(sentence)
	seg_result = []
	for i in seg_list:
		seg_result.append(i)
	stopwords = set()
	with open('sws.ini','r') as fr:
		for i in fr:
			stopwords.add(i.strip())
	return list(filter(lambda x :x not in stopwords,seg_result))



get_str="年轻一辈是有信仰的一辈"
get_list= seg_word(get_str)
t_x,s_i=load()
all_score=0
for i in range(0, len(get_list)):
        for j in  range(0, len(t_x)):
                if t_x[j] in get_list[i]:
                        all_score=all_score + s_i[j]
print ("语句:"+get_str+",得分:"+str(all_score))






