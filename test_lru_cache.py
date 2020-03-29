from lru_cache import lru_cache
from random import randint

@lru_cache(5)
def foo(bar, bar2=5):
    """
    Basic function for returning a random number.
    If lru_cache works the function want be called again and the result shall be identical.
    """
    return randint(0, 1000000)

def test_lru_cache():
    """Using foo to test the lru cache"""
    result = foo([2], bar2={'a': 'b'})
    assert result == foo([2], bar2={'a': 'b'})
    foo(1, 2)
    foo((1, 2), bar2=4)
    foo(bar=[1, 2], bar2="pastennnn")
    foo([], [])
    assert result == foo([2], bar2={'a': 'b'})
    foo("pasten", 123)
    assert result != foo([2], bar2={'a': 'b'})

