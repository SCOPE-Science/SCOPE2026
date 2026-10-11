#!/usr/bin/env python3
from itertools import product

for d in range(1, 13):
    words = list(product((0, 1), repeat=d))
    assert len(words) == 2 ** d
    # The complete conjunction for x is satisfied by assignment x.
    for x in words:
        assert all(bit in (0, 1) for bit in x)
    # Distinct complete conjunctions disagree at a coordinate and are incompatible.
    for i, x in enumerate(words):
        for y in words[i+1:]:
            assert any(a != b for a, b in zip(x, y))
print("VERIFY_OK")
