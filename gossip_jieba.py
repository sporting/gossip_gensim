import json
import jieba

def main():
    jieba.set_dictionary('./res/dict.txt.big')
    stopwordset = set()

    with open('./res/stopwords.txt','r') as sw:
        for line in sw:
            stopwordset.add(line.strip('\n'))

    output = open('./output/jieba_extract.txt','w')

    with open('./res/gossip.corpus.s2tw.json','r') as input:
        jdata = json.load(input)
        sdata = jdata.get('gossip')
        for sd in sdata:
            for s in sd:
                words = jieba.cut(s,cut_all=False)
                for word in words:
                    if word not in stopwordset:
                        output.write(word+' ')
    output.close()


if __name__ == "__main__":
    main()
            
