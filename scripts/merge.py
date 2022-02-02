# クイックソート等と同様、完全に細分化せずにスレッショルドとして適度に大きい個数を設定し、
# それ以下になった時点でなんらかの「ごく少数の対象専用の高速なコードによるソート」を併用するという高速化手法がある[1]。
# 手順として書き出すと次のようになる。
#
# 1. データ列を分割する（通常、二等分する）
# 2. 分割された各データ列で、含まれるデータが設定個数以下ならそれを別の高速なアルゴリズムでソートして返し、
#    設定個数超ならステップ1から3を再帰的に適用してマージソートする
# 3. 二つのソートされたデータ列をマージする
# https://ja.wikipedia.org/wiki/%E3%83%9E%E3%83%BC%E3%82%B8%E3%82%BD%E3%83%BC%E3%83%88#%E3%82%A2%E3%83%AB%E3%82%B4%E3%83%AA%E3%82%BA%E3%83%A0
# この手順を再現する


import bubble_plus


def merge_sort(rand: list) -> list:
    # 分割された各データ列で、含まれるデータが設定個数以下ならそれを別の高速なアルゴリズムでソートして返す
    if len(rand) <= 3:
        # 高速？
        return bubble_plus.bubble_plus(rand)
    # データ列を分割する（通常、二等分する）
    # 再帰的に適用してマージソートする
    left = merge_sort(rand[:len(rand)//2])
    right = merge_sort(rand[len(rand)//2:])
    # マージする
    return merge(left, right)


# マージ部分の実装
def merge(left, right):
    merged = []
    while True:
        # left, right の左端同士を比較し、小さい方を取得していく
        if len(left) == 0 and len(right) == 0:
            break
        elif len(left) == 0 or (len(right) > 0 and left[0] >= right[0]):
            merged.append(right[0])
            del right[0]
        else:
            merged.append(left[0])
            del left[0]
    return merged


if __name__ == '__main__':
    print(merge_sort([2, 3, 1, 3, 14, 5, 9, 11, 4, 8, 0, 7, 20, 5, 22, -1]))
