import re
import os

# ログ出力先フォルダ
output_folder = "C:\\Users\\y_hashimoto\\selfpy\\log"
# 元となるログファイル
source_log = r"C:\Users\y_hashimoto\selfpy\log\test_20251111.log"
# 出力先フォルダが無ければ作成
os.makedirs(output_folder, exist_ok=True)

# シナリオ名の正規表現
scenario_pattern = re.compile(r"シナリオ「([A-Za-z0-9_.]+)」")

# 新しいシナリオファイルを開く
def open_new_scenario_file(output_folder, scenario_name, current_file):

    # 前のシナリオファイルがあれば閉じる
    if current_file is not None:
        current_file.close()

    # ファイルパスを作成
    path = os.path.join(output_folder, scenario_name + ".log")
    # 追記モードでファイルを開き、呼び出し元へ返す
    return open(path, "a", encoding="cp932")

# ログファイルに書き込む処理
def write_log_line(line, scenario_file, other_file):

    # シナリオIDが読み込まれている場合
    if scenario_file is not None:
        scenario_file.write(line)
    else:
        other_file.write(line)

# 現在のシナリオ情報
current_scenario_name = ""
current_scenario_file = None

# その他ログファイル
other_log_path = os.path.join(output_folder, "その他ログ.log")
other_log_file = open(other_log_path, "w", encoding="cp932")        

# 元ログファイル
with open(source_log, encoding="cp932") as log_file:

    for line in log_file:

        # シナリオ名を探す
        found = scenario_pattern.search(line)

        if found:

            new_scenario_name = found.group(1)

            # シナリオが切り替わった場合のみファイルを開き直す
            if new_scenario_name != current_scenario_name:
                current_scenario_file = open_new_scenario_file(
                    output_folder, new_scenario_name, current_scenario_file
                )
                current_scenario_name = new_scenario_name

            # シナリオファイルへ書き込む
            current_scenario_file.write(line)

        else:
            write_log_line(line, current_scenario_file, other_log_file)

# 後処理
if current_scenario_file is not None:
    current_scenario_file.close()

other_log_file.close()
