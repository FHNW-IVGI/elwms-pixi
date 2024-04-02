from foo.bar import random


def test_random():
    assert random().shape == (10,)
    assert random().dtype == float

    assert random((5,), int).shape == (5,)
    assert random((5,), int).dtype == int
