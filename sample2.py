from symbol import parameters

from sample1 import warikan


# 目標:calculate_warikanの挙動が正しいかどうかを調べるコードを書く
# 入力と出力のパターン
# 例1:1500円で3人 -> "1人あたり: 500円, 端数: 0円"
def check_warikan():
    result = warikan(1500, 3) == "1人あたり: 500円, 端数: 0円"

    if result:
        print("OK")
    else:
        print("NG")


check_warikan()


def check_warikan2():
    result = warikan(2000, 3) == "1人あたり: 666円, 端数: 2円"

    if result:
        print("OK")
    else:
        print("NG")


check_warikan2()


def check_warikan():
    parameters = [
        (1500, 3, "1人あたり: 500円, 端数: 0円"),
        (2000, 3, "1人あたり: 666円, 端数: 2円"),
    ]

    for p in parameters:
        amount = p[0]
        number_of_people = p[1]
        expected = p[2]

        result = expected == warikan(amount, number_of_people)

        if result:
            print("OK!")
        else:
            print("NG!")


check_warikan()
