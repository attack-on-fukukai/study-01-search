### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import pandas as pd

def readCsv(faileName):
    wrk_list = []
    df = pd.read_csv(faileName)
    for item in df:
        wrk_list.append(item)
    return wrk_list


### 検索ツール
def search(word,sourceList):  
    # 入力されたワードとリストを比較する
    if word in sourceList:
        print(f"{word}が見つかりした")
    else:
        print(f"{word}が見つかりませんでした\n見つからなかったのでリストに追加します")
        sourceList.append(word)        

    df = pd.DataFrame(sourceList)
    df.to_csv("out.csv",header=False)


if __name__ == "__main__":
    
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

    sourceList = readCsv("source.csv")
    search(word,sourceList)
