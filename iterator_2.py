class SquaresIterator:
    def __init__(self, end):
        self.current = 0
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        result = self.current ** 2
        self.current += 1
        return result


# 10 ta sonning kvadratlar ketma-ketligini ekranga chiqaramiz
squares_iterator = SquaresIterator(10)
for num in squares_iterator:
    print(num)
