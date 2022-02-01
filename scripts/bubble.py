def bubble(rand: list) -> list:
    length = len(rand)
    for i in range(length):
        # バブルソートは毎回末尾が決まるのでリストの要素数が実行回数
        for j in range(length - i - 1):
            if rand[j] > rand[j + 1]:
                rand[j], rand[j + 1] = rand[j + 1], rand[j]
    return rand


print(bubble([2, 3, 1, 9, 4, 0, 7]))
