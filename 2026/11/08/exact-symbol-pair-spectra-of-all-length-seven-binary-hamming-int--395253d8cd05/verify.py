"""Exhaustive independent check of length-seven binary Hamming pair spectra."""
from collections import Counter
from itertools import permutations


def pair_weight(word):
    return sum(word[i] != 0 or word[(i + 1) % 7] != 0 for i in range(7))


def code_for_columns(columns):
    result = []
    for mask in range(128):
        check = 0
        for i, column in enumerate(columns):
            if (mask >> i) & 1:
                check ^= column
        if check == 0:
            result.append(mask)
    return tuple(result)


indexed_codes = {}
counts_orders = Counter()
for columns in permutations(range(1, 8)):
    code = code_for_columns(columns)
    assert len(code) == 16
    spectrum = Counter()
    for mask in code:
        vector = tuple((mask >> i) & 1 for i in range(7))
        spectrum[pair_weight(vector)] += 1
    a = spectrum.get(4, 0)
    expected = {0: 1, 4: a, 5: 7-a, 6: 7-a, 7: a+1}
    assert dict(spectrum) == {k: v for k, v in expected.items() if v}
    assert a in (0, 1, 2)
    counts_orders[a] += 1
    if code in indexed_codes:
        assert indexed_codes[code] == a
    else:
        indexed_codes[code] = a
assert dict(counts_orders) == {0: 336, 1: 2352, 2: 2352}
assert len(indexed_codes) == 30
assert dict(Counter(indexed_codes.values())) == {0: 2, 1: 14, 2: 14}
print("DIRECT_VERIFY_OK 5040 orders, 30 distinct indexed codes, spectra 2/14/14")
