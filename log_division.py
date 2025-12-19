import re
import os

# 出力先フォルダ
output_folder = "C:\\Users\\y_hashimoto\\selfpy\\log"
os.makedirs(output_folder, exist_ok=True)

# シナリオ名の正規表現
scenario_pattern = re.compile(r"シナリオ「([A-Za-z0-9_.]+)」")

# 現在のシナリオ情報
current_scenario_name = ""
current_scenario_file = None

# その他ログファイル
other_log_path = os.path.join(output_folder, "その他ログ.log")
other_log_file = open(other_log_path, "w", encoding="cp932")

# 元ログファイル
with open("C:\\Users\\y_hashimoto\\selfpy\\log\\test_20251111.log", encoding="cp932") as log_file:

    for line in log_file:

        # シナリオ名を探す
        found = scenario_pattern.search(line)

        if found:
            new_scenario_name = found.group(1)
            print("シナリオ取得:", new_scenario_name)

            # シナリオが切り替わった場合
            if new_scenario_name != current_scenario_name:

                # 前のシナリオファイルを閉じる
                if current_scenario_file is not None:
                    current_scenario_file.close()

                # シナリオ名を更新
                current_scenario_name = new_scenario_name

                # 新しいシナリオファイルを開く（追記）
                scenario_file_path = os.path.join(
                    output_folder, current_scenario_name + ".log"
                )
                current_scenario_file = open(scenario_file_path, "a", encoding="cp932")

            # シナリオ行を書き込む
            current_scenario_file.write(line)

        else:
            # シナリオが始まっていれば、そのシナリオへ
            if current_scenario_file is not None:
                current_scenario_file.write(line)
            # まだシナリオが始まっていなければその他ログへ
            else:
                other_log_file.write(line)

# 後処理
if current_scenario_file is not None:
    current_scenario_file.close()

other_log_file.close()
