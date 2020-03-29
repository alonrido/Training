def get_char_generator(base_char, last_char, empty):
    yield empty
    for char in xrange(ord(base_char), ord(last_char) + 1):
        yield chr(char)

def brute_force(max_size=2, base_char='0', last_char='z', empty=''):
    if max_size <= 1:
        for char in get_char_generator(base_char, last_char, empty):
            yield char
        return
    for char in get_char_generator(base_char, last_char, empty):
        if char == empty:
            yield char
        else:
            for suffix in brute_force(max_size - 1):
                 yield char + suffix

