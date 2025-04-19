import matplotlib.pyplot as plt
import networkx as nx


class index_of_max__tree:
    def __init__(self, data, N):
        self.n = N
        self.data = data
        self.tree = [None] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = start
        else:
            middle = (start + end) // 2
            self.build(2*node + 1, start, middle)
            self.build(2*node + 2, middle + 1, end)
            self.tree[node] = self.merge(self.tree[2*node + 1], self.tree[2*node + 2])

    def merge(self, left, right):
        if self.data[left] > self.data[right]:
            return left
        elif self.data[left] < self.data[right]:
            return right
        else:
            return right

    def query(self, left, right):
        return self.query_recursive(0, 0, self.n - 1, left, right)

    def query_recursive(self, node, start, end, left, right):
        if right < start or left > end:
            return -1
        if left <= start and right >= end:
            return self.tree[node]

        middle = (start + end) // 2
        left_result = self.query_recursive(2*node + 1, start, middle, left, right)
        right_result = self.query_recursive(2*node + 2, middle + 1, end, left, right)

        if left_result == -1:
            return right_result
        if right_result == -1:
            return left_result
        return self.merge(left_result, right_result)

    def print(self):
        G = nx.DiGraph()
        labels = {}
        pos = {}

        def build_graph(node, depth, x_offset):
            if node >= len(self.tree) or self.tree[node] is None:
                return 0
            left = 2 * node + 1
            right = 2 * node + 2

            left_width = build_graph(left, depth + 1, x_offset)
            center = x_offset + left_width
            pos[node] = (center, -depth)
            idx = self.tree[node]
            labels[node] = f"idx:{idx}\nval:{self.data[idx]}"
            right_width = build_graph(right, depth + 1, center + 1)

            if left < len(self.tree) and self.tree[left] is not None:
                G.add_edge(node, left)
            if right < len(self.tree) and self.tree[right] is not None:
                G.add_edge(node, right)

            return left_width + 1 + right_width

        build_graph(0, 0, 0)

        plt.figure(figsize=(16, 8))
        nx.draw(G, pos, with_labels=True, node_size=1800, node_color='lightblue', font_size=10)
        nx.draw_networkx_labels(G, pos, labels=labels, font_size=12, font_color="black")
        plt.title("Max Tree — Индексы и значения", fontsize=14)
        plt.axis('off')
        plt.tight_layout()
        plt.show()


if __name__ == "__main__":
    N = int(input())
    # print('N: ', N)
    data = list(map(int, input().split()))
    # print('data: ', data)
    K = int(input())
    # print('K: ', K)

    result_tree = index_of_max__tree(data, N)
    # result_tree.print()

    for _ in range(K):
        L, R = map(int, input().split())
        idx = result_tree.query(L - 1, R - 1)
        print(f"{idx + 1}")
