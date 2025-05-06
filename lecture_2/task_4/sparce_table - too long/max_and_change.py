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

    def query(self, left_index, right_index):
        length = right_index - left_index + 1
        k = length.bit_length() - 1
        left_idx = self.st[k][left_index]
        right_idx = self.st[k][right_index - (1 << k) + 1]
        best_idx = self._combine_indices(left_idx, right_idx)
        return (self.data[best_idx], best_idx + 1)

    def update(self, index, value):
        self.data[index] = value
        self._build()  # full rebuild ?


if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    st = SparseTableMaxIndex(N, data)

    Q = int(input())
    for _ in range(Q):
        parts = input().split()
        if parts[0] == 's':
            L, R = int(parts[1]), int(parts[2])
            result, best_idx = st.query(L - 1, R - 1)
            print(result, end=' ')
        elif parts[0] == 'u':
            pos, val = int(parts[1]), int(parts[2])
            st.update(pos - 1, val)