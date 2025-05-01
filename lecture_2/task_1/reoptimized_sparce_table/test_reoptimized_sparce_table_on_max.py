import pytest
from reoptimized_sparce_table_on_max import SparseTableMaxWithFreq


@pytest.fixture
def factory():
    def _create(data):
        return SparseTableMaxWithFreq(len(data), data)
    return _create


def test_example_case(factory):
    data = [2, 2, 2, 1, 5]
    st = factory(data)
    assert st.call_me__mommy_please(1, 2) == (2, 2)
    assert st.call_me__mommy_please(1, 4) == (5, 1)


def test_all_equal(factory):
    data = [7] * 10
    st = factory(data)
    assert st.call_me__mommy_please(0, 9) == (7, 10)
    assert st.call_me__mommy_please(3, 6) == (7, 4)


def test_single_element(factory):
    data = [42]
    st = factory(data)
    assert st.call_me__mommy_please(0, 0) == (42, 1)


def test_two_elements_same(factory):
    data = [5, 5]
    st = factory(data)
    assert st.call_me__mommy_please(0, 1) == (5, 2)


def test_two_elements_different(factory):
    data = [3, 8]
    st = factory(data)
    assert st.call_me__mommy_please(0, 1) == (8, 1)
    assert st.call_me__mommy_please(0, 0) == (3, 1)
    assert st.call_me__mommy_please(1, 1) == (8, 1)


def test_large_segment(factory):
    data = list(range(1, 1001))
    st = factory(data)
    assert st.call_me__mommy_please(0, 999) == (1000, 1)
    assert st.call_me__mommy_please(500, 999) == (1000, 1)


def test_max_at_edges(factory):
    data = [10, 1, 1, 1, 10]
    st = factory(data)
    assert st.call_me__mommy_please(0, 4) == (10, 2)
    assert st.call_me__mommy_please(1, 3) == (1, 3)


def test_repeated_max_spread(factory):
    data = [1, 9, 3, 9, 5, 9]
    st = factory(data)
    assert st.call_me__mommy_please(0, 5) == (9, 3)
    assert st.call_me__mommy_please(1, 3) == (9, 2)
    assert st.call_me__mommy_please(2, 4) == (9, 1)


def test_full_range(factory):
    data = [1, 3, 5, 7, 9, 7, 5, 3, 1]
    st = factory(data)
    assert st.call_me__mommy_please(0, 8) == (9, 1)
    assert st.call_me__mommy_please(3, 5) == (9, 1)


def test_minimal_range_queries(factory):
    data = [2, 4, 6, 8, 10]
    st = factory(data)
    for i in range(len(data)):
        assert st.call_me__mommy_please(i, i) == (data[i], 1)
