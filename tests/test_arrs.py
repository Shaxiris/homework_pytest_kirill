from utils import arrs
from utils.arrs import get, my_slice


def test_get():
    assert get([1, 2, 3], 0) == 1
    assert get([1, 2, 3], 2) == 3
    assert get([1, 2, 3], 3, "default") == "default"
    assert get([1, 2, 3], 3, None) is None
    assert get([], 0, "default") == "default"
    assert get([1, 2, 3], -1, "default") == "default"
    assert get([1, 2, 3], 4, "default") == "default"

def test_my_slice():
    assert my_slice([1, 2, 3], 0, 1) == [1]
    assert my_slice([1, 2, 3], 0, 3) == [1, 2, 3]
    assert my_slice([1, 2, 3], 1, 2) == [2]
    assert my_slice([1, 2, 3], 1, 5) == [2, 3]
    assert my_slice([1, 2, 3], 0, -1) == [1, 2]
    assert my_slice([1, 2, 3], -2) == [2, 3]

def test_get_out_of_range():
    assert get([1, 2, 3], 3, "default") == "default"
    assert get([1, 2, 3], 4, "default") == "default"

def test_get_negative_index():
    assert get([1, 2, 3], -1) is None



def test_my_slice_negative_start():
    assert my_slice([1, 2, 3], -2) == [2, 3]

def test_my_slice_end_out_of_range():
    assert my_slice([1, 2, 3], 0, 5) == [1, 2, 3]
    assert my_slice([1, 2, 3], 0, 10) == [1, 2, 3]

def test_my_slice_start_and_end_out_of_range():
    assert my_slice([1, 2, 3], 5, 7) == []
    assert my_slice([1, 2, 3], -5, 7) == [1, 2, 3]
    assert my_slice([1, 2, 3], 5, 10) == []
