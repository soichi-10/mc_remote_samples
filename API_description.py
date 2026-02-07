import time
from easy_ui import MultiNumericUI

# 1. ボタンが押された時に実行したい処理（関数）を定義
def print_values1(v):
    print(v["パワー"], v["スピード"])

def print_values2(v):
    print(v["回数"])

MultiNumericUI(
    title="パラメータ調整ツール",
    items={
        "パワー": 10,
        "スピード": 5,
        "回数": 1
    },
    buttons={
        "現在の値を表示1": print_values1,
        "現在の値を表示2": print_values2
    }
)

# 3. メインプログラムの待機
while True:
    time.sleep(1)