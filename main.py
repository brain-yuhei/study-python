from collections import Counter

# ログを読み取る（エンコード：SJIS）
with open("C:\\Users\\y_hashimoto\\selfpy\\log\\test_20251111.log", encoding='cp932') as f:

    # 全行をリスト型で取得し格納
    lines = f.readlines()

# 各行のステータスを取得
status = [line.split(' ')[2] for line in lines] # 空白３番目の要素を取得

# ステータスのカウント
status_Count = Counter(status)

# 結果出力（
print("ログレベル別件数：")
for Status, num in status_Count.items():

    # フォーマット文字列で出力
    print(f"{Status}: {num}件")

# ERRORメッセージだけ抽出
print("\n--- エラーログ一覧 ---")
for line in lines:
    if "[ERROR]" in line:
        print(line.strip())

# INFOメッセージだけ抽出
print("\n--- インフォログ一覧 ---")
for line in lines:
    if "[INFO]" in line:
        print(line.strip())

# WARNINGメッセージだけ抽出
print("\n--- ワーニングログ一覧 ---")
for line in lines:
    if "[WARNING]" in line:
        parts = line.split() # 行データをsplitを使って分割
        message = " ".join(parts[3:]) # 分割したパーツを指定して格納
        print(message)
 