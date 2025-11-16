class Solution:
    def countDistinct(self, n: int) -> int:
        number = n
        
        if number < 10:
            return number
        
        numbers = [0] + [0] * number
        
        power = 0
        while number >= 10:
            number /= 10
            power += 1
        
        div = int(n / (10 ** power))

        for i in range(10, len(numbers)):
            if i % 10 == 0:
                numbers[i] = 1
            if power >= 2:
                for m in range(1, div + 1):
                    for k in range(10):
                        if i == m * (10 ** power) + k:
                            numbers[i] = 1
                            break
        return numbers.count(0) - 1