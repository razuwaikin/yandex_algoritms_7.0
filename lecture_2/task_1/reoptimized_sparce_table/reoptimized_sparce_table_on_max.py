class SparseTableMaxWithFreq:
    def __init__(self, input_N, data):
        self.N = input_N
        self.data = data[: self.N]
        self.K = self.N.bit_length()
        self.st = [[(0, 0)] * self.N for _ in range(self.K)]
        self._build()

    def _build(self):
        for i in range(self.N):
            self.st[0][i] = (self.data[i], 1)

        for k in range(1, self.K):
            for i in range(self.N - (1 << k) + 1):
                left = self.st[k - 1][i]
                right = self.st[k - 1][i + (1 << (k - 1))]
                self.st[k][i] = self._combine(left, right)

    def _combine(self, a, b):
        if a[0] > b[0]:
            return a
        elif a[0] < b[0]:
            return b
        else:
            return (a[0], a[1] + b[1])

    def print_(self):
        print()
        for i in range(len(self.st)):
            print(self.st[i])
        print()

    def call_me__mommy_please(self, left_index, right_index):
        result = (float("-inf"), 0)
        power = self.K - 1
        while left_index <= right_index:
            while (1 << power) > right_index - left_index + 1:
                power -= 1
            result = self._combine(result, self.st[power][left_index])
            left_index += 1 << power
        return result


if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    st = SparseTableMaxWithFreq(N, data)
    st.print_()

    K = int(input())
    for _ in range(K):
        L, R = map(int, input().split())
        result = st.call_me__mommy_please(L - 1, R - 1)
        print(f"{result[0]} {result[1]}")
