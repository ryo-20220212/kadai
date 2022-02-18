### 検索ツールサンプル
### これをベースに課題の内容を追記してください
import os.path

# 検索ソース
BASE_RESERCH_SOURCE=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]

# ファイルパス
FILE_PATH = r'C:\Users\arika\Desktop\lesson\source.csv'

# ファイルパスにリストの中身をcsvで書き込む
def write_source(file_path, source_list):
    with open(file_path, encoding='UTF-8',mode='w') as f:
        source_list = '\n'.join(source_list)
        f.write(source_list)
    
### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    #ファイルパスが存在しないとき、ベースの検索ソースリストをもとにcsvファイルを作成する
    if not(os.path.exists(FILE_PATH)): 
        write_source(FILE_PATH, BASE_RESERCH_SOURCE)
    
    #  ファイルパスを読み込む
    with open(FILE_PATH,'r',encoding='UTF-8') as f:
        source_list = f.read().splitlines()
        
    ### ここに検索ロジックを書く
    
    if(word in source_list):
        print(f"{word}が見つかりました")
    else: #検索ワードが見つからない場合は、登録するか登録しないかを選び、それに応じた対応をする
        print(f"{word}が見つかりませんでした")
        while True:
            regi =input(f"{word}を登録しますか? yes or no >>>")
            print(regi.lower())
            if(regi.lower() == 'yes'): #大文字小文字どちらも対応できるようlower()を使用
                source_list.append(word)
                write_source(FILE_PATH, source_list)
                break
            elif(regi.lower() == 'no'):
                break
            else:
                print('もう一度入力してください')
                
if __name__ == "__main__":
    search()