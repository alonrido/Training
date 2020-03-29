from brute_force import brute_force


def test_brute_force():
    gen = brute_force(base_char='0', last_char='2' , max_size=5)
    lst_brt = []
    for combination in gen:
        lst_brt.append(combination)
    assert len(set(lst_brt)) == len(lst_brt)
    assert len(lst_brt) == 4**5