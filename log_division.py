import re
import os

# 出力先フォルダ
output_folder = "C:\\Users\\y_hashimoto\\selfpy\\log"
os.makedirs(output_folder, exist_ok=True) # フォルダがない場合は作成

# シナリオ名の正規表現（reが正規表現の宣言）
scenario_name = re.compile(r"シナリオ「([A-Za-z0-9_.]+)」")

# 書き込み中のシナリオ名とファイル
current_scenario_name = ""
current_scenario_file = ""

# その他ログファイルを開く（最初のシナリオが出るまでここへ書く）※osでフォルダにアクセス
other_log_path = os.path.join(output_folder, "その他ログ.log")
other_log_file = open(other_log_path, "w", encoding="cp932")

# 分割元のログファイルを開く
with open("C:\\Users\\y_hashimoto\\selfpy\\log\\test_20251111.log", encoding="cp932") as log_file:

    # 1行ずつ読む
    for line in log_file:

        # 行の中にシナリオ名があるかチェック
        found = scenario_name.search(line)

        # シナリオがある場合
        if found:
            print("シナリオ取得:", found.group(1))

            # シナリオ名を取得
            new_scenario_name = found.group(1)

            # シナリオ名が変わった場合
            if new_scenario_name != current_scenario_name :

                # 前のログファイルは閉じる            

                # シナリオ名を更新
                current_scenario_name = scenario_name

                # 新しいログファイルを開く（追記できるようにする）

            # シナリオ行を書き込む

        # それ以外     
        else:
            print("なし:", line.strip())
            
            # シナリオを保持している場合は現ログファイルに書き込む

            # シナリオ未保持の場合はその他ログファイルに書き込む

# ファイルを閉じる
