### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import pandas as pd

def readCsv(faileName):
    wrk_list = []
    df = pd.read_csv(faileName)
    for item in df:
        wrk_list.append(item)
    return wrk_list

### 文字比較関数
def matching(word,source):
    for item in source:
        if item == word:
            return True
    return False

### 検索ツール
def search(word,sourceList):  
    # 入力されたワードとリストを比較する
    if matching(word,sourceList) == True:
        print("{}が見つかりした".format(word))
    else:
        print("{}が見つかりませんでした\n見つからなかったのでリストに追加します".format(word))
        sourceList.append(word)        

    df = pd.DataFrame(sourceList)
    df.to_csv("out.csv",header=False)

if __name__ == "__main__":

    sourceList = readCsv("source.csv")
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    search(word,sourceList)


