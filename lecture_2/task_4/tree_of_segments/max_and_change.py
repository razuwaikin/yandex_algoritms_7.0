import matplotlib.pyplot as plt
import networkx as nx


class max_tree:
    def __init__(self, data):
        self.n = len(data)
        self.data = data[:]
        self.tree = [None] * (4 * self.n)
        self.build(0, 0, self.n - 1)

    def build(self, node, start, end):
        if start == end:
            self.tree[node] = (self.data[start], 1, start)
        else:
            mid = (start + end) // 2
            self.build(2 * node + 1, start, mid)
            self.build(2 * node + 2, mid + 1, end)
            self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

    def merge(self, left, right):
        if left[0] > right[0]:
            return left
        elif left[0] < right[0]:
            return right
        else:
            return (left[0], left[1] + right[1], min(left[2], right[2]))

    def query(self, l_, r_):
        return self.query_recursive(0, 0, self.n - 1, l_, r_)

    def query_recursive(self, node, start, end, l_, r_):
        if r_ < start or l_ > end:
            return (float('-inf'), 0, self.n)
        if l_ <= start and end <= r_:
            return self.tree[node]
        mid = (start + end) // 2
        left_result = self.query_recursive(2 * node + 1, start, mid, l_, r_)
        right_result = self.query_recursive(2 * node + 2, mid + 1, end, l_, r_)
        return self.merge(left_result, right_result)

    def update(self, idx, value):
        self._update_recursive(0, 0, self.n - 1, idx, value)

    def _update_recursive(self, node, start, end, idx, value):
        if start == end:
            self.data[idx] = value
            self.tree[node] = (value, 1, idx)
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update_recursive(2 * node + 1, start, mid, idx, value)
            else:
                self._update_recursive(2 * node + 2, mid + 1, end, idx, value)
            self.tree[node] = self.merge(self.tree[2 * node + 1], self.tree[2 * node + 2])

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
        labels = {
            i: f"{self.tree[i][0]} (L{self.tree[i][1]})"
            for i in range(len(self.tree)) if self.tree[i] is not None
        }
        nx.draw_networkx_labels(G, pos, labels=labels)
        plt.title("Бинарное дерево (max_tree)")
        plt.axis('off')
        plt.show()


if __name__ == "__main__":
    N = int(input())
    data = list(map(int, input().split()))
    tree = max_tree(data)

    Q = int(input())
    for _ in range(Q):
        parts = input().split()
        if parts[0] == 's':
            L, R = int(parts[1]) - 1, int(parts[2]) - 1
            val, count, idx = tree.query(L, R)
            print(val, end=' ')
        elif parts[0] == 'u':
            pos, val = int(parts[1]) - 1, int(parts[2])
            tree.update(pos, val)
