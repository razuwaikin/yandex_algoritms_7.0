import pytest
from max_on_record import max_tree

@pytest.fixture
def sample_data():
    return [1, 3, 2, 3, 5, 5, 1]

def test_build_and_query_entire_range(sample_data):
    tree = max_tree(sample_data)
    max_val, count = tree.query(0, len(sample_data) - 1)
    assert max_val == 5
    assert count == 2

def test_query_single_element(sample_data):
    tree = max_tree(sample_data)
    max_val, count = tree.query(2, 2)
    assert max_val == 2
    assert count == 1

def test_query_range_with_duplicates(sample_data):
    tree = max_tree(sample_data)
    max_val, count = tree.query(1, 3)
    assert max_val == 3
    assert count == 2

def test_query_max_only_once(sample_data):
    tree = max_tree(sample_data)
    max_val, count = tree.query(4, 4)
    assert max_val == 5
    assert count == 1

def test_query_range_outside(sample_data):
    tree = max_tree(sample_data)
    result = tree.query_recursive(0, 0, tree.n - 1, 10, 15)
    assert result == (float('-inf'), 0)

def test_query_full_left_half(sample_data):
    tree = max_tree(sample_data)
    max_val, count = tree.query(0, 3)
    assert max_val == 3
    assert count == 2

def test_query_full_right_half(sample_data):
    tree = max_tree(sample_data)
    max_val, count = tree.query(3, 6)
    assert max_val == 5
    assert count == 2

def test_all_elements_equal():
    data = [7] * 10
    tree = max_tree(data)
    max_val, count = tree.query(0, 9)
    assert max_val == 7
    assert count == 10

def test_large_input():
    data = [i % 100 for i in range(100000)]
    tree = max_tree(data)
    max_val, count = tree.query(0, 99999)
    assert max_val == 99
    assert count == 1000

@pytest.mark.parametrize("data, queries, expected_results", [
    (
        [1, 3, 2, 3, 5, 5, 1],
        [
            (0, 6), (0, 3), (1, 3), (4, 6), (4, 5), (2, 2), (0, 0), (6, 6), (3, 5), (2, 4),
        ],
        [
            (5, 2), (3, 2), (3, 2), (5, 2), (5, 2), (2, 1), (1, 1), (1, 1), (5, 2), (5, 1),
        ]
    ),
    (
        [7] * 10,
        [
            (0, 9), (0, 0), (3, 5), (1, 1), (5, 9), (2, 8), (4, 6), (0, 3), (6, 6), (0, 6),
        ],
        [
            (7, 10), (7, 1), (7, 3), (7, 1), (7, 5), (7, 7), (7, 3), (7, 4), (7, 1), (7, 7),
        ],
    ),
    (
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1],
        [
            (0, 9), (0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (9, 9),
        ],
        [
            (10, 1), (10, 1), (9, 1), (8, 1), (7, 1), (6, 1), (5, 1), (4, 1), (3, 1), (1, 1),
        ],
    ),
    (
        [1, 3, 2, 5, 5, 4],
        [(0, 5), (0, 2), (0, 3), (4, 5), (5, 5)],
        [(5, 2), (3, 1), (5, 1), (5, 1), (4, 1)],
    )
])
def test_max_tree_queries(data, queries, expected_results):
    tree = max_tree(data)
    for (left, right), expected in zip(queries, expected_results):
        result = tree.query(left, right)
        assert result == expected