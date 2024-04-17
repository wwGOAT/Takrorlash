def even_numbers_generator(start, end):
    current = start
    while current <= end:
        if current % 2 == 0:
            yield current
        current += 1


# 10 dan 20 gacha bo'lgan juft sonlar ketma-ketligini ekranga chiqaramiz
even_nums = even_numbers_generator(10, 20)
for num in even_nums:
    print(num)
