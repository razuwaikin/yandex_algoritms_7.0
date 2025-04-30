class sparce_table_on_max:
    def __init__(self, input_n, input_data):
        self.N = input_n
        self.table = [[None] * (self.N - i) for i in range(self.N)]
        self.build(input_data)

    def build(self, input_data):
        for i in range(self.N):
            if i == 0:
                for j in range(self.N):
                    self.table[0][j] = (input_data[j], 1)

            else:
                for j in range(len(self.table[i])):
                    self.table[i][j] = self.max_from_two_elements(self.table[i-1][j], self.table[0][j+i])

    def max_from_two_elements(self, first_element, second_element):
        if first_element[0] > second_element[0]:
            return first_element
        elif first_element[0] < second_element[0]:
            return second_element
        else:
            return (first_element[0], first_element[1] + second_element[1])

    def call_me__mommy_please(self, left_index, right_index):
        # return max on segment [left_index, right_index]
        length = right_index - left_index
        return self.table[length][left_index]

    def print_sparce_table(self):
        for i in range(self.N):
            print(self.table[i])
        print()


if __name__ == "__main__":
    N = int(input())
    # print('N: ', N)
    data = list(map(int, input().split()))
    # print('data: ', data, '\n\n')

    result_tree = sparce_table_on_max(N, data)
    # result_tree.print_sparce_table()

    K = int(input())
    # print('K: ', K)

    for _ in range(K):
        L, R = map(int, input().split())
        # print('L: ', L, '   R: ', R)
        result = result_tree.call_me__mommy_please(L - 1, R - 1)
        print(f"{result[0]} {result[1]}")
