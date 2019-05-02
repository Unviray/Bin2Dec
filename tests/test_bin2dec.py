from bin2dec import convert


def test_bin2dec():
    assert convert([1, 0, 0, 1, 1, 0, 1, 1]) == 155
    assert convert([0, 1, 1, 0, 0, 1, 0, 0]) == 100
