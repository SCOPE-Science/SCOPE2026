#!/usr/bin/env python3
"""Reproduce a finite factor-closure certificate for a ternary morphic word.

The infinite conclusion follows from the lemma in RESULT.md; this program
checks the finite, exact premises of that lemma and the short factor spectrum.
"""

H = {'0': '01', '1': '21', '2': '0'}
EXPECTED_F8 = (
    '01021012', '01210102', '01210210', '02101021',
    '02101210', '10102101', '10121010', '10121021',
    '10210102', '10210121', '12101021', '12102101',
    '21010210', '21012101', '21012102', '21021010',
    '21021012',
)
EXPECTED_REFLECTED = {
    1: ('0', '1', '2'),
    2: ('01', '10', '12', '21'),
    3: ('010', '012', '101', '121', '210'),
    4: ('0121', '1012', '1210', '2101'),
    5: ('01210', '10121', '12101', '21012'),
    6: ('012101', '101210'),
    7: ('1012101',),
    8: (),
}
EXPECTED_PALINDROMES = {
    1: ('0', '1', '2'),
    2: (),
    3: ('010', '101', '121'),
    4: (),
    5: ('01210', '21012'),
    6: (),
    7: ('1012101',),
    8: (),
}
EXPECTED_REFLECTION_COMPLEXITY = (3, 3, 6, 7, 10, 12, 15, 17)


def apply_h(word):
    return ''.join(H[ch] for ch in word)


def factors(word, length):
    return {word[i:i+length] for i in range(len(word)-length+1)}


def main():
    seed = '0'
    for _ in range(6):
        seed = apply_h(seed)
    assert len(seed) == 37
    assert seed == '0121021010210121010210121021012101021'
    f8 = factors(seed, 8)
    assert tuple(sorted(f8)) == EXPECTED_F8
    assert len(f8) == 17
    # Finite all-factor image closure: every length-eight factor of h(u)
    # with u in F8 belongs to F8.
    checked_windows = 0
    for u in f8:
        image = apply_h(u)
        for i in range(len(image) - 7):
            assert image[i:i+8] in f8, (u, i, image[i:i+8])
            checked_windows += 1
    assert all(u[::-1] not in f8 for u in f8)
    for n in range(1, 9):
        fn = set().union(*(factors(u, n) for u in f8))
        reflected = tuple(sorted(u for u in fn if u[::-1] in fn))
        pal = tuple(sorted(u for u in fn if u == u[::-1]))
        assert reflected == EXPECTED_REFLECTED[n], (n, reflected)
        assert pal == EXPECTED_PALINDROMES[n], (n, pal)
        assert len(fn) == 2*n+1, (n, len(fn))
        r = len(fn) - (len(reflected)-len(pal))//2
        assert r == EXPECTED_REFLECTION_COMPLEXITY[n-1], (n, r)
    # Extra independent prefix cross-checks; not an infinite proof.
    word = seed
    for _ in range(5):
        word = apply_h(word)
        assert factors(word, 8) == f8
    print('VERIFY_OK', 'factor8=', len(f8), 'closure_windows=', checked_windows,
          'short_lengths=', 8, 'long_prefix_length=', len(word))


if __name__ == '__main__':
    main()
