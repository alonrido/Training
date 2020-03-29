import pickle
from collections import OrderedDict


def lru_cache(cache_limit=2):
    if cache_limit < 1 or not isinstance(cache_limit, int):
        raise Exception("lru cache limit must be greater or equal 1, also its type must be an integer")

    def lru_cache_with_defined_limit(function):
        cache = OrderedDict()

        def decorator(*args, **kwargs):
            pickled_arguments = pickle.dumps([args, kwargs])
            if pickled_arguments in cache:
                return cache[pickled_arguments]
            elif len(cache) == cache_limit:
                cache.pop(cache.keys()[0])
            result = function(*args, **kwargs)
            cache[pickled_arguments] = result
            return result
        return decorator
    return lru_cache_with_defined_limit
