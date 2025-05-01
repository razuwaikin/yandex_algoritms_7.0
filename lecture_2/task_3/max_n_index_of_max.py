class SparseTableMaxIndex:
    def __init__(self, input_N, data):
        self.N = input_N
        self.data = data[:self.N]
        self.K = self.N.bit_length()
        self.st = [[0] * self.N for _ in range(self.K)]
        self._build()

    def _build(self):
        for i in range(self.N):
            self.st[0][i] = i

        for k in range(1, self.K):
            for i in range(self.N - (1 << k) + 1):
                left_idx = self.st[k - 1][i]
                right_idx = self.st[k - 1][i + (1 << (k - 1))]
                self.st[k][i] = self._combine_indices(left_idx, right_idx)

    def _combine_indices(self, idx1, idx2):
        if self.data[idx1] > self.data[idx2]:
            return idx1
        elif self.data[idx1] < self.data[idx2]:
            return idx2
        else:
            return max(idx1, idx2)

    def call_me__mommy_please(self, left_index, right_index):
        length = right_index - left_index + 1
        k = length.bit_length() - 1
        left_idx = self.st[k][left_index]
        right_idx = self.st[k][right_index - (1 << k) + 1]
        best_idx = self._combine_indices(left_idx, right_idx)
        return (self.data[best_idx], best_idx + 1)


if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    st = SparseTableMaxIndex(N, data)

    K = int(input())
    for _ in range(K):
        L, R = map(int, input().split())
        result, best_idx = st.call_me__mommy_please(L - 1, R - 1)
        print(result, best_idx)
