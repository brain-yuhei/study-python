# ログファイルとノードハッシュファイルの比較処理

import csv

# ノードハッシュファイルのオブジェクト生成（ｆ）
with open("C:\\Users\\y_hashimoto\\selfpy\\log\\ノードハッシュ.txt", encoding='cp932') as f:

    # セットクラス（重複データ無し）のインスタンス生成
    node_hash_id = set()  

    # ファイルを1行ずつ読み込む
    for line in f:

        # 両端の空白や改行を削除
        clean_line = line.strip() 
        
        # ノードハッシュIDの追加
        node_hash_id.add(clean_line)  

# CSVファイルの作成（書き出しモードで）
with open("C:\\Users\\y_hashimoto\\selfpy\\log\\log.csv", "w", newline="", encoding="utf-8") as csvfile:

    writer = csv.writer(csvfile)

    # ログファイルのオブジェクト生成（ｆ）
    with open("C:\\Users\\y_hashimoto\\selfpy\\log\\test_20251111.log", encoding='cp932') as f:

        # ファイルを1行ずつ読み込む
        for line in f:

            # ノードIDを取り出す
            node_id = line.split("ノードID：")[-1].strip()

            # ノードハッシュIDと一致するノードID行を書き出す
            if node_id in node_hash_id:

                # 空行無しで書き出し処理
                print(line.strip())

                # CSVファイルに書き出し処理
                writer.writerow([line.strip(), node_id])
