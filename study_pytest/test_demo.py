import pytest


@pytest.mark.demo
def test_aaa():
    print("aaaaaaa")
    assert True


class TestAA:

    pytestmark = [pytest.mark.nmb, pytest.mark.demo]

    def test_bbb(self):
        print("bbbb")
        assert "hello" == "world"
