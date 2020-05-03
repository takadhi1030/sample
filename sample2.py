from sample1 import warikan


# 目標:calculate_warikanの挙動が正しいかどうかを調べるコードを書く
# 入力と出力のパターン
# 例1:1500円で3人 -> "1人あたり: 500円, 端数: 0円"
def check_warikan():
    result = warikan(1500, 3) == "1人あたり: 500円, 端数: 0円"

    if result == True:
        print("OK")
    else:
        print("NG")


check_warikan()
