class Numbers:

    def __init__(self) -> None:
        pass

    def prime_factorization(self, num):
        x = num - 1
        while x > 1:
            if num % x == 0:
                self.prime_factorization(x)
                self.prime_factorization(num / x)
                return
            x -= 1
        print(int(num))