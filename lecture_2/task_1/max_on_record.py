import matplotlib.pyplot as plt
import networkx as nx

class max_tree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [None] * (4 * self.n)
        self.build(0, 0, self.n - 1, data)

    def build(self, node, start, end, data):
        if start == end:
            self.tree[node] = (data[start], 1)
        else:
            middle = (start + end)//2
            self.build(2*node + 1, start, middle, data)
            self.build(2*node + 2, middle + 1, end, data)
            self.tree[node] = self.merge(self.tree[2*node + 1], self.tree[2*node + 2])

    def merge(self, left, right):
        if left[0] > right[0]:
            return left
        elif left[0] < right[0]:
            return right
        else:
            return (left[0], left[1] + right[1])

    def query(self, left, right):
        return self.query_recursive(0, 0, self.n - 1, left, right)

    def query_recursive(self, node, start, end, left, right):
        if right < start or left > end:
            return (float('-inf'), 0)
        if left <= start and right >= end:
            return self.tree[node]

        middle = (start + end) // 2
        left_result = self.query_recursive(2*node + 1, start, middle, left, right)
        right_result = self.query_recursive(2*node + 2, middle + 1, end, left, right)
        return self.merge(left_result, right_result)

    def get_pos(self, node=0, depth=0, pos_dict=None, x=0):
        if pos_dict is None:
            pos_dict = {}
        if node >= len(self.tree) or self.tree[node] is None:
            return x
        x = self.get_pos(2 * node + 1, depth + 1, pos_dict, x)
        pos_dict[node] = (x, -depth)
        x += 1
        x = self.get_pos(2 * node + 2, depth + 1, pos_dict, x)
        return x

    def print(self):
        G = nx.DiGraph()
        edges = []

        for i in range(len(self.tree)):
            if self.tree[i] is not None:
                left = 2 * i + 1
                right = 2 * i + 2
                if left < len(self.tree) and self.tree[left] is not None:
                    edges.append((i, left))
                if right < len(self.tree) and self.tree[right] is not None:
                    edges.append((i, right))

        G.add_edges_from(edges)
        pos = {}
        self.get_pos(pos_dict=pos)
        plt.figure(figsize=(14, 8))
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=10)
        labels = {i: f"{self.tree[i][0]} (L{self.tree[i][1]})" for i in range(len(self.tree)) if self.tree[i] is not None}
        nx.draw_networkx_labels(G, pos, labels=labels)
        plt.title("Бинарное дерево (max_tree)")
        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    N = int(input())
    print('N: ', N)
    data = list(map(int, input().split()))
    print('data: ', data)
    K = int(input())
    print('K: ', K)

    result_tree = max_tree(data)
    result_tree.print()

    for _ in range(K):
        L, R = map(int, input().split())
        result = result_tree.query(L - 1, R - 1)
        print(f"{result[0]} {result[1]}")
