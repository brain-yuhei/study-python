name = '橋本'

# 名前を表示
print(name)

# 改行（文の継続を「\」でPythonに伝える
print \
(name)

# もしくは行継続中の場合は以下でも可能
print('こんにちは',
      'こんばんは')

# 区切り文字の使い方
print('Hello', name, 'さん', sep='+')

# 疑似的に複数行のコメントを使う方法（あまり推奨されない）
"""
複数行のコメント
使ってみた
"""

# フォーマット文字列
name_test = '橋本'
print(f'こんにちは、{name_test}さん！')

# リスト　 ［0，1，2，3，4］
data = ['山田', '佐藤', '田中', '大谷', '山本']
print(data[2])

# 変数の破棄
test = 'テストだよ'
print(test) # 削除前
del test
print(test) # 削除後（変数値がないためエラー）


