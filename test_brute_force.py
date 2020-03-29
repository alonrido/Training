from brute_force import brute_force


def test_brute_force():
    gen = brute_force(base_char='0', last_char='2' , max_size=3)
    lst_brt = []
    for combination in gen:
        lst_brt.append(combination)
    assert len(set(lst_brt)) == len(lst_brt)
    # 3**3 are the number of permutation without the empty. +1 for empty + 4 options for every printable char
    assert len(lst_brt) == 3**3 + 1 + 3*4