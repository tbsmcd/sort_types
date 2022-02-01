import math
import bubble_plus

# クイックソートは以下の手順で行われる。
#
# ピボットの選択：適当な値（ピボット（英語版）という）を境界値として選択する
# 配列の分割：ピボット未満の要素を配列の先頭側に集め、ピボット未満の要素のみを含む区間とそれ以外に分割する
# 再帰：分割された区間に対し、再びピボットの選択と分割を行う
# ソート終了：分割区間が整列済みなら再帰を打ち切る
# https://ja.wikipedia.org/wiki/%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%BD%E3%83%BC%E3%83%88


# 擬似的な中央値を返す
# https://ja.wikipedia.org/wiki/%E3%82%AF%E3%82%A4%E3%83%83%E3%82%AF%E3%82%BD%E3%83%BC%E3%83%88#%E6%9C%80%E6%82%AA%E8%A8%88%E7%AE%97%E9%87%8F%E3%81%AE%E5%9B%9E%E9%81%BF
def median(rand: list) -> int:
    if len(rand) <= 2:
        return rand[1]
    else:
        sample = [rand[0], rand[-1], rand[math.floor(len(rand)/2)]]
        sample = bubble_plus.bubble_plus(sample)
        return sample[math.floor(len(sample)/2)]


def quick(rand: list) -> list:
    if len(rand) <= 1:
        return rand
    # ピボットの選択：適当な値（ピボット（英語版）という）を境界値として選択する
    # statistics.median を使うのは若干反則に見えるので
    pivot = median(rand)
    big = []
    small = []
    med = []
    for i in rand:
        if i == pivot:
            med.append(i)
        elif i >= pivot:
            big.append(i)
        else:
            small.append(i)
    small = quick(small)
    big = quick(big)
    # 左から small, med, big の順に並べる
    small.extend(med)
    small.extend(big)
    return small


if __name__ == '__main__':
    print(quick([2, 3, 1, 3, 5, 9, 4, 0, 7]))
