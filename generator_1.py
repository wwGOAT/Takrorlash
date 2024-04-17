def square_generator(n):
    for i in range(n):
        yield i ** 2


# 10 ta sonning kvadratlar ketma-ketligini ekranga chiqaramiz
squares = square_generator(10)
for num in squares:
    print(num)
