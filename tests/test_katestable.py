import typing
import pytest

from katestable import KTestable


K: int = 3


@pytest.fixture
def language() -> typing.List[str]:
    return ['a', 'aa', 'abba', 'abbbba', 'aaabbbbba']


@pytest.fixture
def kt(language) -> KTestable:
    return KTestable.build(K, language)


@pytest.mark.parametrize(
    "word, expected",
    [
        ('aba', False),
        ('abc', False),
        ('aaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaa', False),
        ('aabbbaaac', False),
        ('aaaaabbbbbbbbba', True),
        ('a', True),
        ('aa', True),
        ('abba', True),
        ('abbbba', True),
        ('aaabbbbba', True),
    ]
)
def test_detect(kt, word, expected):
    assert kt.detect(word) == expected
