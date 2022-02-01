def bubble_plus(rand: list) -> list:
    # バブルソートの改良版も
    length = len(rand)
    for i in range(length):
        # バブルソートは毎回末尾が決まるのでリストの要素数が最大の実行回数
        moved = False
        for j in range(length - i - 1):
            if rand[j] > rand[j + 1]:
                rand[j], rand[j + 1] = rand[j + 1], rand[j]
                moved = True
        if not moved:
            # ソートが発生しなかった場合は終了
            break
    return rand


if __name__ == '__main__':
    print(bubble_plus([2, 3, 1, 9, 4, 0, 7]))