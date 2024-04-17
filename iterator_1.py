class EvenNumbersIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        while self.start % 2 != 0:
            self.start += 1
        result = self.start
        self.start += 2
        return result


# 10 dan 20 gacha bo'lgan juft sonlar ketma-ketligini ekranga chiqaramiz
even_nums_iterator = EvenNumbersIterator(10, 20)
for num in even_nums_iterator:
    print(num)
